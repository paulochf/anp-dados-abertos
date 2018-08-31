import xml.etree.ElementTree as ET

from collections import OrderedDict
from itertools import tee, chain
from pathlib import Path


TAG_PREFIX = '{urn:schemas-microsoft-com:xml-analysis:rowset}'

TAG_KEY_MAPPING = OrderedDict({
    "0": "valor_compra",
    "1": "valor_venda",
    "2": "unidade",
    "3": "municipio",
    "4": "regiao",
    "5": "estado",
    "6": "bandeira",
    "7": "produto",
    "8": "razao_social_revenda",
    "9": "data_coleta",
})

def print_preco(obj=None, sep=";"):
    if not obj:
        obj = TAG_KEY_MAPPING

    txt = sep.join(obj.values())

    return f"{txt}\n"

PrecoRevenda = OrderedDict({x: float('nan') for x in TAG_KEY_MAPPING.values()})
PrecoRevenda.__str__ = print_preco


class PrecoParser:
    """
    Classe utilizada para processar os arquivos xml da série histórica de preços de combustíveis.

    Atributos
    ---------
    elems: list
        contém todos os nós do objeto root que possuem a tag {urn:schemas-microsoft-com:xml-analysis:rowset}R
    data_container: list
        contém todos os registros de preços de revenda armazenados como objetos precoRevenda obtidos a partir do objeto root.

    """
    container = list()

    def __init__(self, filename):
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
        self.elems = filter(
            lambda x: x.tag == f'{TAG_PREFIX}R',
            ET.parse(filename).getroot()
        )
        self.data_container = None

    @staticmethod
    def _get_data(elemento):
        """Parseia de um registro de dado do arquivo de entrada a partir do objeto root."""
        coleta_preco = PrecoRevenda.copy()
        for data in elemento:
            key = data.tag[-1]
            new_key = TAG_KEY_MAPPING.get(key)

            if not new_key:
                print(f"Tag {data.tag} not expected.")
                continue

            coleta_preco[new_key] = data.text

        return coleta_preco

    def parse(self):
        """Executa o parser para todos os elementos do arquivo de entrada."""
        self.data_container = map(self._get_data, self.elems)

    @staticmethod
    def to_csv(nome_arquivo, all_data):
        """
        Gera um arquivo .csv com os dados.

        Parâmetros
        ----------
        nome_arquivo: str
            nome do arquivo a ser salvo na pasta ./data

        all_data: iter
            iterador da lista dos dados parseados
        """
        data_list, data_list_check = tee(all_data)

        if len(list(data_list_check)) == 0:
            raise Exception(
                f"Não há dado para exportar. "
                f"Utilizar método get_data para processar o arquivo de origem."
            )

        fullpath = Path("./data")
        fullpath.mkdir(parents=True, exist_ok=True)
        fullpath = fullpath / nome_arquivo

        with open(fullpath, 'w') as f:
            f.write(print_preco())

            for preco in data_list:
                f.write(print_preco(preco))

        print(f"Arquivo {fullpath} criado com sucesso.")

    @staticmethod
    def all_to_csv(nome_arquivo, parsers_list):
        """
        Gera um arquivo .csv com os dados de cada Parser da lista dada.

        Parâmetros
        ----------
        nomearquivo: str
            nome do arquivo a ser salvo na pasta ./data

        all_data: list
            lista de Parser's
        """
        all_data = map(lambda x: x.data_container, parsers_list)

        PrecoParser.to_csv(nome_arquivo, chain(*all_data))
