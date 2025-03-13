import os
from typing import List
import boto3
from dotenv import load_dotenv
import shutil

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da AWS a partir do .env
AWS_ACCESS_KEY_ID: str = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY: str = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION: str = os.getenv('AWS_REGION')
BUCKET_NAME: str = os.getenv('BUCKET_NAME')

# Configura o cliente S3 - instancia do tipo s3
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# le os arquivos de uma pasta
def listar_arquivos(pasta: str) -> List[str]:
    """Lista todos os arquivos em uma pasta local."""
    arquivos: List[str] = []
    for nome_arquivo in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, nome_arquivo)
        if os.path.isfile(caminho_completo):
            arquivos.append(caminho_completo)
    return arquivos

# jogar arquivos para o s3
def upload_arquivos_para_s3(arquivos: List[str]) -> None:
    """Faz upload dos arquivos listados para o S3."""
    for arquivo in arquivos:
        nome_arquivo: str = os.path.basename(arquivo)
        s3_client.upload_file(arquivo, BUCKET_NAME, nome_arquivo)
        print(f'{nome_arquivo} foi enviado para o S3.')

# deletar arquivos locais - opcional
# def deletar_arquivos_locais(arquivos: List[str]) -> None:
#     """Deleta os arquivos locais após o upload."""
#     for arquivo in arquivos:
#         os.remove(arquivo)
#         print(f'{arquivo} foi deletado do local.')

# mover arquivos para processados
def mover_arquivos_para_processados(arquivos: List[str], destino: str) -> None:
    """Move os arquivos copiados para S3 para pasta processados."""
    if not os.path.exists(destino):
        os.makedirs(destino)
    for arquivo in arquivos:
        shutil.move(arquivo, destino)
        print(f'{arquivo} foi movido para {destino}.')

# executa o backup
def executar_backup(pasta: str, destino: str) -> None:
    """Executa o processo completo de backup."""
    arquivos: List[str] = listar_arquivos(pasta)
    if arquivos:
        upload_arquivos_para_s3(arquivos)
        mover_arquivos_para_processados(arquivos, destino)
    else:
        print("Nenhum arquivo encontrado para backup.")

if __name__ == "__main__":
    PASTA_LOCAL: str = 'arquivos'  # Substitua pelo caminho da sua pasta local
    PASTA_DESTINO: str = 'arquivos_processados'  # Substitua pelo caminho da pasta de destino
    executar_backup(PASTA_LOCAL, PASTA_DESTINO)
    mover_arquivos_para_processados(listar_arquivos(PASTA_LOCAL), PASTA_DESTINO)
