# RUFFLES
# programa que vai abrir um pdf com senha e tentar quebrá-la com bruteforce
import PyPDF2

# abrindo o arquivo com as senhas e salvando-as numa lista:
senhas_possiveis = []
new = []
lista = open('dictionary.txt', 'r')
ler_lista = lista.readlines()
for cada_palavra in ler_lista:
    senhas_possiveis.append(cada_palavra)
for palavras in senhas_possiveis:
    nova = palavras.replace('\n', '')
    new.append(nova)
# descriptografando o pdf através de um loop (bruteforce)
pdf = open('pdfcomsenha3.pdf', 'rb')
pdf_senha = PyPDF2.PdfFileReader(pdf)
# verificando se está mesmo criptografado:
if pdf_senha.isEncrypted:
    print('O arquivo possui senha')
    print('Começando ataque de senhas')
    print('***')
    for senhas in new:
        if pdf_senha.decrypt(str(senhas)) == 1:
            print(f'Senha encontrada: {senhas}')
            exit(1)
else:
    print('O pdf não tem senha, noob!')
