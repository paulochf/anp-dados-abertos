import requests
from pathlib import Path
import xml.etree.ElementTree as ET
import os
years = range(2004, 2019)
baseurl = "http://www.anp.gov.br/images/dadosabertos/precos/"
links = [baseurl+f"{year}.xml" for year in years]

path_to_save = Path("./raw")
if not path_to_save.is_dir():
    os.mkdir("./raw")

for link in links:
    r = requests.get(link)
    if r.status_code == requests.codes['ok']:
        root = ET.fromstring(r.text.encode("latin-1").decode("UTF-8"))
        print(f"# Finalizado o download do arquivo {link}.")
        #seleciona o ano 
        file_to_save = link[-8:]
        file_to_save = path_to_save / f'{file_to_save}'
        tree = ET.ElementTree(root)
        tree.write(file_to_save, encoding='latin-1')
        print(f"## Arquivo {link} salvo.")
    else:
        print(f"### STATUS: {r.status.code} => Não foi possível realizar o download do arquivo {link}.")
        continue
print("Finalizado o(s) download(s).")
        

        
