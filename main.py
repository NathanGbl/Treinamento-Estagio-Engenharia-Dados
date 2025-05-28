import pandas as pd

def normaliza_seguradora(filepath: str):
    df = None
    try:
        df = pd.read_excel(filepath)
        print(df.head())
    except Exception as e:
        raise(f"Erro ao ler o arquivo: {e}")
    clientes = df[["CLIENTE CNPJ", "CLIENTE RAZÃO SOCIAL", "CLIENTE UF"]]
    vendedores = df[["VENDEDOR", "CÓDIGO VENDEDEOR", "SEGURADORA"]]
    venda = df[["CLIENTE CNPJ", "CÓDIGO VENDEDEOR", "Cod_Nota", "Data", "Modalidade"]]