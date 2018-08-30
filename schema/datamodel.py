import xml.etree.ElementTree as ET
from collections import namedtuple
from pathlib import Path
import os

precoRevenda = namedtuple('PrecoRevenda', 'valor_compra valor_venda unidade municipio regiao estado bandeira produto razao_social_revenda data_coleta')

class PrecosParser():
    """
    Classe utilizada para processar os arquivos xml da série histórica de preços de combustíveis

    Atributos
    ---------
    filename: str
        string que representa o caminho onde está localizado o arquivo a ser processado.
    tree: xml.etree.ElementTree
        classe ElementTree representando todo o documento xml
    root: xml.etree.ElementTree.Element
        raiz da árvore do objeto tree
    elems: list
        contém todos os nós do objeto root que possuem a tag {urn:schemas-microsoft-com:xml-analysis:rowset}R
    data_container: list
        contém todos os registros de preços de revenda armazenados como objetos precoRevenda obtidos a partir do objeto root.
    container : list
        objeto de classe utilizado para armazenar objetos data_container de diferents instâncias.
    
    Métodos
    -------
    get_data()
        Parser do arquivo filename a partir do objeto root.
    data_to_csv(nomearquivo)
        Gera um arquivo .csv a partir dos dados armazenados em data_container
    add_data(data)
        Método de classe utilizado para adicionar o objeto de instância data_container ao objeto de classe container.
    exporta_dados_csv(data)
        Método de classe utilizado para gerar um arquivo .csv a partir dos dados armazenados no objeto de classe container.
    """
    container = []

    def __init__(self, filename: str):
        """
        Parâmetros
        ----------
        filename: str
            string que representa o caminho onde está localizado o arquivo a ser processado.
        tree: xml.etree.ElementTree
            objeto que representa todo o documento xml
        root: xml.etree.ElementTree.Element
            raiz da árvore do objeto tree
        """
        self.filename = filename
        self.tree = ET.parse(self.filename)
        self.root = self.tree.getroot()

    def get_data(self):
        """
        Parser do arquivo filename a partir do objeto root.
        
        O método não tem retorno, irá gerar a lista data_container que será 
        populada com os objetos precoRevenda.

        Parâmetros:
        ----------
        elems: list
            lista contendo todos os nós do objeto root que possuem a tag {urn:schemas-microsoft-com:xml-analysis:rowset}R
        data_container: list
            lista contendo todos os registros de preços de revenda armazenados como objetos precoRevenda obtidos a partir do objeto root.
        """
        self.elems = [child for child in self.root if child.tag == '{urn:schemas-microsoft-com:xml-analysis:rowset}R']
        self.data_container = []
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
            self.data_price = precoRevenda(**coleta_preco)
            self.data_container.append(self.data_price)
        del self.data_price
        del coleta_preco
    
    def data_to_csv(self, nomearquivo):
        """
        Gera um arquivo .csv a partir dos dados armazenados em data_container
        
        Parâmetros
        ----------
        nomearquivo: str
            nome do arquivo a ser salvo na pasta ./data
        """
        if len(self.data_container) == 0:
            print(f"Não há dado para exportar. Utilizar método get_data para processar o arquivo {self.filename}.")
        else:
            fullpath = Path("./data")
            if not fullpath.is_dir():
                os.mkdir(fullpath)
            fullpath = fullpath / f"{nomearquivo}.csv"
            with open(fullpath, 'w', encoding='latin-1') as file_:
                file_.write("valor_compra;valor_venda;unidade;municipio;regiao;estado;bandeira;produto;razao_social_revenda;data_coleta\n")
                for data in self.data_container:
                    file_.write(f"{data.valor_compra};{data.valor_venda};{data.unidade};{data.municipio};{data.regiao};{data.estado};{data.bandeira};{data.produto};{data.razao_social_revenda};{data.data_coleta}\n")
            print(f"Arquivo ./data/{nomearquivo}.csv criado com sucesso.")
    
    @classmethod
    def add_data(cls, data):
        """
        Adiciona a lista gerada por get_data ao container da classe.
        data : lista -> self.data_container
        """
        cls.container.append(data)
    @classmethod
    def exporta_dados_csv(cls, nomearquivo):
        """
        Método que gera um csv a partir dos dados do objeto de classe container.
        Deve ser utilizado para produzir um único arquivo csv oriundo de múltiplos arquivos xml.
        
        Parâmetros
        ----------
        nomearquivo: str
            nome do arquivo a ser salvo na pasta ./data
        """
        if len(cls.container) == 0:
            print(f"Não há dado para exportar. Utilizar método o add_data para salvar os dados necessários.")
        else:
            fullpath = Path("./data")
            if not fullpath.is_dir():
                os.mkdir(fullpath)
            fullpath = fullpath / f"{nomearquivo}.csv"
            with open(fullpath, 'w', encoding='latin-1') as file_:
                file_.write("valor_compra;valor_venda;unidade;municipio;regiao;estado;bandeira;produto;razao_social_revenda;data_coleta\n")
                for lista_precos in cls.container:
                    for data in lista_precos:
                        file_.write(f"{data.valor_compra};{data.valor_venda};{data.unidade};{data.municipio};{data.regiao};{data.estado};{data.bandeira};{data.produto};{data.razao_social_revenda};{data.data_coleta}\n")
            print(f"Arquivo ./data/{nomearquivo}.csv criado com sucesso.")




                        

