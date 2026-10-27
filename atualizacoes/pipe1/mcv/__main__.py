from dak import DAL
from model import Ativo,Mercadoria
from view import reader,writer

def main():
    dal=DAL("ativo")
    ativos=dal.retrieve()
    reader(ativos)
    writer(ativos)  