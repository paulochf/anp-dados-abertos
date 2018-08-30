# PARSER DA SÉRIE HISTÓRICA DE PREÇOS DE COMBUSTÍVEIS
### ORIGEM DOS DADOS
#### http://www.anp.gov.br/dados-abertos-anp
#### http://dados.gov.br/dataset?q=anp

### ESTRUTURA DE DIRETÓRIOS
data - Armazena os arquivos .csv gerados a partir dos arquivos xml processados<br>
docs - Armazena o PDF com os metadados dos arquivos xml da série histórica<br>
raw - Armazena os arquivos xml a serem parseados<br>
schema - Armazena a Classe PrecosParser utilizada para processar os arquivos xml<br>

### INSTRUÇÕES:

```
# clonar o repositório
git clone https://github.com/netoferraz/anp-dados-abertos.git
```

#### Criar um ambiente virtual

```
python -m venv .\venv
```

#### Instalar as dependências

```
pip install -r requirements.txt
```

#### Ative o ambiente virtual

```
.\venv\Scripts\activate
```

#### Sobre:

1. O arquivo `getdata.py` deve ser utilizado para realizar o download dos arquivos xml disponibilizados.
2. O arquivo `parser.py` deve ser utilizado para processar os arquivos xml e salvar os respectivos arquivos .csv.

### **DOWNLOAD MANUAL:**

Caso você não deseje realizar o procedimento de geração dos arquivo .csv programaticamente, segue os links para os respectivos arquivos.

- [2004](https://www.amazon.com/clouddrive/share/Jr377WcRRVy5EflToiUAT6fvvexvBXclDvwIxk4P2Sj)
- [2005](https://www.amazon.com/clouddrive/share/6BuXxRe53uFToinkFwuDe9svGHVX3NWiyiBvTbRKdqs)
- [2006](https://www.amazon.com/clouddrive/share/H8rRnTFMg0ikTAOq3NH7xkUU4It6aV8eqmGPUS6aRUM)
- [2007](https://www.amazon.com/clouddrive/share/7DqhxaEuQnIH7juuEJCGmow4Hhqz8Vrjw6DhgMyg75h)
- [2008](https://www.amazon.com/clouddrive/share/Ggtc8JK7orbr6fSfgK04AijAaDuFI2xRqvB0qZW33Og)
- [2009](https://www.amazon.com/clouddrive/share/jmkuavUMusRmKrudq2rbV2ZRwmU3YxdNMZ316mSpFru)
- [2010](https://www.amazon.com/clouddrive/share/1OmzEyoZEj4DfLxaTDR6qgYBvVkQAuvi4ZtWC3U2RsJ)
- [2011](https://www.amazon.com/clouddrive/share/oHT4sNJMf113oXguSnEwlblz4jckFZL7cp4bWo9d0Zy)
- [2012](https://www.amazon.com/clouddrive/share/uZSSaPKjawVnlRQPesYyTO8v7w3KOnAGa8QHaNffQfl)
- [2013](https://www.amazon.com/clouddrive/share/b9AQzL5Ts9pfbvzIKVnM2AfuWd2kk1zYl6OR8NGkcu0)
- [2014](https://www.amazon.com/clouddrive/share/hp6L71QdW68iDGmRQlip6CKeKX3s1V84Gpv0MIUknxQ)
- [2015](https://www.amazon.com/clouddrive/share/MBxZpayAdvuy70bRsvTn0pO5yCgC8brbDGxIA4SJYlZ)
- [2016](https://www.amazon.com/clouddrive/share/CLo9whnG84Qs9Lm7zfZIycoWM5pYMhuZBxnkjEiw4dY)
- [2017](https://www.amazon.com/clouddrive/share/dNz0V3ErSDDc00fxwHJIGa0F7EMC0lz14OKe2eyg6jj)
- [2018](https://www.amazon.com/clouddrive/share/bmrJzpiBXySXN4rLyUnk7C29q2zAhPeVDbwP1mSVwkM)
- [2004-2018](https://www.amazon.com/clouddrive/share/Sgjd3cK1IJTN0PfKTc83FGDd8KSsu8HX41DDolMT7kL) (Até 21/08/2018)

### **NOTA:**

> O presente repositório não é institucional, portanto, qualquer comunicação sobre os dados devem ser dirigidas diretamente a instituição pública. O único propósito dessa página é fornecer um formato de arquivo mais acessível ao grande público


