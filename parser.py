from schema.datamodel import PrecosParser
from pathlib import Path

path = Path.cwd()/ 'raw'
files = list(path.glob("**/*.xml"))

if len(files) !=0:
    #inicia o processamento dos arquivos xml
    for index, file_ in enumerate(files,1):
        print(f"Processando o arquivo {file_}.")
        filedata = PrecosParser(file_)
        #processa os dados do arquivo file_
        filedata.get_data()
        #exporta para um arquivo csv
        filename = file_.name[:-4] #coleta o ano do dado
        filedata.data_to_csv(filename)
        #adiciona os dados da instância ao container da classe
        PrecosParser.add_data(filedata.data_container)
    #exporta um arquivo único com todos os dados processados
    PrecosParser.exporta_dados_csv('serie_precos_completa')
    print(f"Finalizado o processamento de {index} arquivos.")
else:
    print("Não há arquivo xml a ser processado.")

