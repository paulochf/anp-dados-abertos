from schema.datamodel import PrecoParser
from pathlib import Path

path = Path.cwd() / 'raw'
files = list(path.glob("**/*.xml"))

if len(files) == 0:
    raise Exception("Não há arquivo(s) xml a ser(em) processado(s).")


parsers = list()

#inicia o processamento dos arquivos xml
for index, file_ in enumerate(files, 1):
    print(f"Processando o arquivo {file_}.")
    filedata = PrecoParser(file_)

    #processa os dados do arquivo file_
    filedata.parse()

    #exporta para um arquivo csv
    filename = file_.name[:-4] #coleta o ano do dado
    filedata.to_csv(f"{filename}.csv", filedata.data_container)

    #adiciona os dados da instância ao container da classe
    parsers.append(filedata)

#exporta um arquivo único com todos os dados processados
PrecoParser.all_to_csv('serie_precos_completa.csv', parsers)

print(f"Finalizado o processamento de {index} arquivo(s).")
