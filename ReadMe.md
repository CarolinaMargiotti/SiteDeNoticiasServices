# SiteDeNoticias

Essa é a versão do usuario em que qualquer um pode ler as noticias.

# Como rodar

## Passos fora do projeto

1. Instalar MariaDB

2. Abrir mysql client do MariaDb

3. Criar database "db1"

`create database db1;`

## Passos no projeto

1. Instalar virtualenv

`pip install virtualenv`

2. Criar ambiente do virtualenv

`virtualenv myenv`

3. Ativar virtualenv

`.\myenv\Scripts\activate`

4. Instalar dependencias

`pip install -r requirements.txt`

5. Rodar app

`python server.py`

# Requisitos Técnicos

1. Utilizar linguagem de programação Python (versão 3.6 ou superior) no back end;
2. Utilizar SQLAlchemy (1.2.19 ou superior) para persistência de dados;
3. Utilizar Jinja 2 ou similar para geração de páginas dinâmicas (tipo template);
4. Utilizar o microframework Flask para implantação do sistema web;
5. Utilizar o Gunicorn ou o Waitress como servidor de implantação, em conjunto com o Flask;
6. Utilizar o Virtualenv para isolamento de ambiente de desenvolvimento e obtenção de pacotes;
7. Estruturar o sistema seguindo a arquitetura MVC e orientação a serviços.
8. Sistema Gerenciador de Banco de Dados MariaDB.
9. Utilizar o GitHub para gerenciar o código-fonte do projeto.
10. Utilizar o GitHub Actions para exemplificar a integração contínua (CI) do sistema.

# Requisitos Funcionais

1. Qualquer usuário pode visualizar as notícias associadas a uma categoria ao acessar a interface correspondente (ex. um menu de navegação).
2. Somente um usuário administrador (único) deve ser capaz de cadastrar, excluir ou alterar as notícias.
3. O usuário administrador (único) deve acessar a interface administrativa somente após ter sido autenticado, não havendo uma rota diretamente acessível sem o procedimento de autenticação.
4. Cada notícia deve possuir (no mínimo):

-   Um assunto (ex. esporte, política, etc.)
-   Um título
-   Um conteúdo.

4. Sua aplicação web deve conter um menu para navegação e, no mínimo, três interfaces distintas com o usuário, acessíveis a partir do menu.

# Requisitos Não Funcionais

1. A aplicação que faz a leitura das notícias e mostra para o usuário deve fazê-lo a partir de requisições à API do serviço de acesso às notícias.
2. A aplicação deve ser responsiva a ponto de não tornar a interface confusa quando acessada a partir de um dispositivo móvel.
