import requests 
import pymysql
import time
from sqlalchemy import create_engine, text
import pandas as pd
from datetime import datetime

# Conexão com banco de dados
engine = create_engine("mysql+pymysql://root:root@localhost/cnpj_ja")
conn = engine.connect()

# Lê os CNPJs da tabela original
df_cnpjs = pd.read_sql("SELECT CNPJ FROM dados", conn)

# Padroniza nomes e remove nulos
df_cnpjs.columns = df_cnpjs.columns.str.strip().str.lower()
df_cnpjs = df_cnpjs[df_cnpjs['cnpj'].notna()]
print("Colunas do DataFrame:", df_cnpjs.columns)

# Formata a data de abertura
def formatar_data(data_str):
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").strftime("%Y-%m-%d")
    except:
        return None

# Consulta a API com tratamento
def consultar_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, str(cnpj)))  # Apenas números
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 429:
            print(f"[{cnpj}] Limite atingido. Aguardando 60s...")
            time.sleep(60)
            return consultar_cnpj(cnpj)
        elif response.status_code != 200:
            print(f"[{cnpj}] Erro {response.status_code} ao consultar.")
            return None

        dados = response.json()
        if dados.get("status") == "ERROR":
            print(f"[{cnpj}] Erro na API: {dados.get('message')}")
            return None

        return {
            "cnpj": dados.get("cnpj"),
            "razao_social": dados.get("nome"),
            "nome_fantasia": dados.get("fantasia"),
            "abertura": formatar_data(dados.get("abertura")),
            "situacao": dados.get("situacao"),
            "tipo": dados.get("tipo"),
            "porte": dados.get("porte"),
            "telefone": dados.get("telefone"),
            "email": dados.get("email"),
            "logradouro": dados.get("logradouro"),
            "numero": dados.get("numero"),
            "bairro": dados.get("bairro"),
            "municipio": dados.get("municipio"),
            "uf": dados.get("uf"),
            "cep": dados.get("cep"),
            "cnae_principal": dados.get("atividade_principal", [{}])[0].get("code"),
            "cnae_principal_desc": dados.get("atividade_principal", [{}])[0].get("text"),
            "cnaes_secundarios": "; ".join(
                [f"{a.get('code')} - {a.get('text')}" for a in dados.get("atividades_secundarias", [])]
            ),
            "socios": "; ".join(
                [s.get("nome", "") for s in dados.get("qsa", [])]
            )
        }
    except Exception as e:
        print(f"[{cnpj}] Erro na requisição: {e}")
        return None

# Criação da tabela com nome "CNAE"
def create_table_for_all_cnpjs(engine):
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS CNAE (
                cnpj VARCHAR(20) PRIMARY KEY,
                razao_social VARCHAR(255),
                nome_fantasia VARCHAR(255),
                abertura DATE,
                situacao VARCHAR(50),
                tipo VARCHAR(50),
                porte VARCHAR(50),
                telefone VARCHAR(20),
                email VARCHAR(100),
                logradouro VARCHAR(255),
                numero VARCHAR(10),
                bairro VARCHAR(100),
                municipio VARCHAR(100),
                uf VARCHAR(2),
                cep VARCHAR(8),
                cnae_principal VARCHAR(20),
                cnae_principal_desc VARCHAR(255),
                cnaes_secundarios TEXT,
                socios TEXT
            )
        """))
    print("Tabela CNAE criada ou já existente.")

# Insere dados com segurança contra duplicatas
def insert_cnpj_data(engine, data):
    try:
        with engine.begin() as conn:
            query = text("""
                INSERT IGNORE INTO CNAE (
                    cnpj, razao_social, nome_fantasia, abertura, situacao,
                    tipo, porte, telefone, email, logradouro, numero, bairro, municipio, uf, cep,
                    cnae_principal, cnae_principal_desc, cnaes_secundarios, socios
                ) VALUES (
                    :cnpj, :razao_social, :nome_fantasia, :abertura, :situacao,
                    :tipo, :porte, :telefone, :email, :logradouro, :numero, :bairro, :municipio, :uf, :cep,
                    :cnae_principal, :cnae_principal_desc, :cnaes_secundarios, :socios
                )
            """)
            conn.execute(query, data)
        print(f"Dados do CNPJ {data['cnpj']} inseridos.")
    except Exception as e:
        print(f"Erro ao inserir dados do CNPJ {data['cnpj']}: {e}")

# Executa criação da tabela
create_table_for_all_cnpjs(engine)

# Processa os CNPJs da lista
def process_cnpjs(df_cnpjs, engine):
    for cnpj in df_cnpjs["cnpj"]:
        dados = consultar_cnpj(cnpj)
        if dados:
            insert_cnpj_data(engine, dados)
        else:
            print(f"[{cnpj}] Falha ao consultar ou inserir.")
        time.sleep(20)  # Aguarda 20s por CNPJ para respeitar o limite da API

# Inicia o processamento
process_cnpjs(df_cnpjs, engine)
