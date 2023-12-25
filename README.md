# Desafio Sindria

### Sobre o Projeto
Este projeto foi desenvolvido com o objetivo de participar do processo seletivo para o cargo de Engenheiro de Software Sênior. Ele representa um esforço concentrado para demonstrar habilidades e conhecimentos em FastAPI e MongoDB, refletindo uma abordagem prática e eficiente em engenharia de software.

### Contexto de Desenvolvimento
Importante destacar que o desenvolvimento deste projeto foi realizado principalmente em um curto período de tempo - especificamente durante o sábado anterior ao prazo final de entrega. Isso apresentou desafios únicos, especialmente em termos de gerenciamento de tempo e priorização de recursos.

### Perspectivas de Melhorias
Embora o projeto atenda às especificações e requisitos do desafio, reconheço que, com mais tempo, haveria espaço significativo para refinamentos e melhorias. Isso incluiria aprimoramentos na estrutura do código, na implementação de testes, na otimização de consultas ao banco de dados, e na adição de novas funcionalidades.

O projeto, portanto, representa tanto uma demonstração das habilidades atuais quanto uma base sobre a qual melhorias contínuas podem ser construídas.

## Instalação

Instruções para instalar as dependências do projeto. Por exemplo:

usando Pipenv:

```bash
pipenv install --dev
```

## Configuração

Para configurar o ambiente de execução do projeto, é necessário criar um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:

 - APP_VERSION: Versão atual do aplicativo. Exemplo: 1.0.0
 - ENVIRONMENT: Ambiente em que o aplicativo está sendo executado (dev, prod, etc.). Exemplo: dev
 - TESTING: Define se o aplicativo está em modo de teste (True ou False). Exemplo: False
 - APP_PORT: Porta na qual o aplicativo FastAPI será executado. Exemplo: 8000
 - APP_NAME: Nome do aplicativo. Exemplo: Desafio Sindria
 - APP_DESCRIPTION: Descrição do aplicativo. Exemplo: Desafio Sindria para o cargo de Engenheiro de Software Senior
 - MONGO_URI: URI de conexão com o MongoDB. Exemplo: mongodb://localhost:27017/local
 - MONGO_DB: Nome do banco de dados MongoDB a ser utilizado. Exemplo: local


## Ambiente de Desenvolvimento com Docker
Este projeto utiliza Docker Compose para configurar e executar o MongoDB localmente. É necessário ter o Docker e o Docker Compose instalados para seguir os passos abaixo.

Instalando o Docker e o Docker Compose
Se ainda não tiver o Docker e o Docker Compose instalados, você pode baixá-los e instalá-los seguindo as instruções no site oficial:

 - Instalar Docker
 - Instalar Docker Compose
 - Iniciando o Banco de Dados MongoDB com Docker Compose

Com o Docker e o Docker Compose instalados, execute o seguinte comando na raiz do projeto para iniciar uma instância do MongoDB:

```bash
docker-compose up -d
```

Isso levantará um container Docker rodando o MongoDB, conforme configurado no arquivo docker-compose.yml do projeto.

Encerrando o Banco de Dados MongoDB
Para parar e remover o container Docker do MongoDB, você pode usar:

```bash
docker-compose down
```

### Instruções para Importação de Dados Fictícios
Este projeto inclui um conjunto de dados fictícios localizados na pasta data. Estes dados são úteis para testar e demonstrar as funcionalidades do sistema sem a necessidade de dados reais. Siga as instruções abaixo para importar esses dados para o seu banco de dados MongoDB.

#### Pré-requisitos
Antes de prosseguir, certifique-se de que:

O MongoDB está instalado e em execução na sua máquina ou em um container Docker.
Você tem os privilégios necessários para acessar e modificar o banco de dados.
#### Passos para Importação
Localize os Arquivos de Dados: Navegue até a pasta data no diretório raiz do projeto. Você encontrará os arquivos de dados neste local, geralmente no formato JSON ou CSV.

#### Prepare o Banco de Dados: 
Certifique-se de que o banco de dados está configurado e pronto para receber os dados. Se necessário, crie uma nova coleção onde os dados serão importados.

#### Importe os Dados para o MongoDB: 
Utilize a ferramenta mongoimport para importar os dados para o MongoDB. 
Abaixo está um exemplo de comando para importar um arquivo JSON:

```bash
mongoimport --db local --collection questions --file ./data/local.questions.json
```
#### Verifique a Importação: 
Após a importação, você pode verificar se os dados foram corretamente importados para o banco de dados usando um cliente MongoDB de sua escolha.

#### Dicas Adicionais
Automatização: Para projetos maiores ou importações frequentes, considere automatizar este processo com um script.
Backup: Sempre faça backup dos seus dados antes de realizar operações de importação em um banco de dados existente.


## Executando o Projeto

Instruções para iniciar o servidor FastAPI:

```bash
make run-app
```

## Estrutura do Projeto

Estrutura do projeto:

- `src/api/v1`: Endpoints da API.
- `src/core`: Configurações centrais e lógica de banco de dados.
- `src/modules`: Módulos do projeto, incluindo lógica de negócios e modelos.
- `main.py`: Ponto de entrada do aplicativo FastAPI.

## Testes

Instruções para executar os testes:

```bash
pytest
```

## Ferramentas de Desenvolvimento

- FastAPI
- pytest
- motor Framework
- python-decouple
- loguru
- Black
- isort
- flake8

## Autor

- Nome: Weslei Souza
- E-mail: weslei.andrade.souza@gmail.com
