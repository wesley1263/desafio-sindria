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
pipenv install
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

## Executando o Projeto

Instruções para iniciar o servidor FastAPI:

```bash
make run-app
```

## Estrutura do Projeto

Explique brevemente a estrutura do seu projeto:

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
