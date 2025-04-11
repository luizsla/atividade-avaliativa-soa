# realiza o download da ultima versao de imagem python disponivel no docker hub
FROM python

ARG DEBIAN_FRONTEND=noninteractive

# criando diretorio de trabalho onde serao guardados os arquivos dos servicos
RUN mkdir /servico
WORKDIR /servico

# instalando e configurando poetry
COPY pyproject.toml poetry.lock README.md /servico/
RUN pip3 install --no-cache-dir poetry==2.0.0
RUN poetry config virtualenvs.create false

# instalando as dependencias python
RUN poetry install --only main --no-root

