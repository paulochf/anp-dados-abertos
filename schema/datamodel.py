import xml.etree.ElementTree as ET
from collections import namedtuple

precoRevenda = namedtuple('PrecoRevenda', 'valor_compra valor_venda unidade municipio regiao estado bandeira produto razao_social_revenda data_coleta')

class PrecosParser():
    def __init__(self, filename):
        self.filename = filename
        self.tree = ET.parse(self.filename)
        self.root = tree.getroot()

    def get_data(self):
        self.elems = [child for child in self.root if child.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}R']
        container = []
        for child in self.elems:
            coleta_preco = dict()
            for data in child:
                if data.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}C0':
                    coleta_preco['valor_compra'] = data.text
                elif data.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}C1':
                    coleta_preco['valor_venda'] = data.text
                elif data.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}C2':
                    coleta_preco['unidade'] = data.text
                elif data.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}C3':
                    coleta_preco['municipio'] = data.text
                elif data.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}C4':
                    coleta_preco['regiao'] = data.text
                elif data.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}C5':
                    coleta_preco['estado'] = data.text
                elif data.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}C6':
                    coleta_preco['bandeira'] = data.text
                elif data.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}C7':
                    coleta_preco['produto'] = data.text
                elif data.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}C8':
                    coleta_preco['razao_social_revenda'] = data.text
                elif data.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}C9':
                    coleta_preco['data_coleta'] = data.text
            data_container = precoRevenda(**coleta_preco)
            container.append(data_container)
        return container