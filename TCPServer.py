from socket import *
import struct
import os


portaServidor = 8000

socketServidor = socket(AF_INET, SOCK_STREAM)

socketServidor.bind(('', portaServidor))

socketServidor.listen(1)

print("O servidor esta pronto para receber")

while 1:

    socketConexao, endereco = socketServidor.accept()

    request = socketConexao.recv(1024)

    if request != b"":

        mensagem, dir_downloads, dados = request.decode().split(":")

        serializar = struct.Struct("{}s".format(int(dados.split()[0])))

        socketConexao.send("O arquivo pode ser enviado".encode())

        buffer_arquivo = b''
        while True:
            part_arquivo = socketConexao.recv(1024)
            if(part_arquivo):
                buffer_arquivo += part_arquivo
            else:
                break

        with open('downloads/{}'.format(dir_downloads), 'w+b') as novo_arquivo:
            novo_arquivo.write(buffer_arquivo)

        print('Arquivo Salvo')
    socketConexao.close()
