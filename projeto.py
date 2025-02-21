import PyPDF2
import os

#cria uma variavel para juntar os arquivos pdf com auxilio da biblioteca
merger = PyPDF2.PdfMerger()

#lista os arquivos da pasta e ordena eles
lista_arquivos = os.listdir("PDFs")
lista_arquivos.sort()

for arquivo in lista_arquivos: #verifica se os arquivos dentro da pasta PDF são .pdf
    if ".pdf" in arquivo:
        merger.append(f"PDFs/{arquivo}") #pega o mesclador e adiciona com o append
                                         #(f"PDFs/{arquivo}") percorre na pasta PDFs e le o nome do arquivo que é dinamico

merger.write("PDF final.pdf") #gera o arquivo final