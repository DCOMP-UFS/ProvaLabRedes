
# Importação da biblioteca de socket
from socket import *
import struct

nomeServidor = '192.168.100.3'

portaServidor = 8000

socketCliente = socket(AF_INET, SOCK_STREAM)

socketCliente.connect((nomeServidor, portaServidor))

arquivo = "uploads/"

nome = input(
    'Coloque o Arquivo desejado na pasta uploads, após isso digite seu nome: ')

arquivo += nome

with open(arquivo, 'rb') as arq:

    dados_arquivo = arq.read()
    nome_arquivo = arquivo.encode()

    nome_absoluto = arquivo.split('/')[-1]

    tamanho_em_bytes = len(dados_arquivo)

    estrutura_chave = "{}s".format(tamanho_em_bytes)

    serializar = struct.Struct(estrutura_chave)

    dados_upload = serializar.pack(*[dados_arquivo])

    socketCliente.send("Enviarei um arquivo chamado:{}: {} bytes".format(
        nome_absoluto, len(dados_arquivo)).encode())

    response = socketCliente.recv(1024)

    if response.decode() != "":

        mensagem = response.decode()

        min_enviado = 0
        max_enviado = 1024

        try:
            while(min_enviado < len(dados_upload)):
                part_arquivo = dados_upload[min_enviado: max_enviado]
                socketCliente.send(part_arquivo)
                min_enviado += 1024
                max_enviado += 1024
        except:
            pass


socketCliente.close()
