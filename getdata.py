import requests
import xml.etree.ElementTree as ET

from pathlib import Path

BASE_URL = "http://www.anp.gov.br/images/dadosabertos/precos"
years = range(2004, 2019)

path_to_save = Path("./raw")
path_to_save.mkdir(parents=True, exist_ok=True)

for year in years:
    url = f"{BASE_URL}/{year}.xml"
    r = requests.get(url)

    if r.status_code != requests.codes.ok:
        print(f"### STATUS: {r.status_code} => Não foi possível realizar o download do arquivo {url}.")
        continue

    root = ET.fromstring(r.text.encode("latin-1").decode("UTF-8"))
    print(f"# Finalizado o download do arquivo {url}.")

    #seleciona o ano
    file_to_save = path_to_save / str(year)

    tree = ET.ElementTree(root)
    tree.write(file_to_save, encoding='latin-1')
    print(f"## Arquivo {url} salvo.")

print("Finalizado o(s) download(s).")



