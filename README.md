# challenge-sensedata

    Software desenvolvido mediante desafio, com a proposta de criar um TODO list em Python e Flask, linguagem e
    framework até então desconhecido. Desafio aceito, foram 7 dias de estudo e aprendizagem sobre o universo
    Python, e posso dizer que me apaixonei pela simplicidade e grandeza de recursos que tem o Python e este pe-
    queno e poderoso framework.

# Dependências do projeto
    alembic==0.9.1
    appdirs==1.4.3
    click==6.7
    dominate==2.3.1
    Flask==0.12.1
    Flask-Bootstrap==3.3.7.1
    Flask-Login==0.4.0
    Flask-Migrate==2.0.3
    Flask-Script==2.0.5
    Flask-SQLAlchemy==2.2
    Flask-Testing==0.6.2
    Flask-WTF==0.14.2
    itsdangerous==0.24
    Jinja2==2.9.6
    Mako==1.0.6
    MarkupSafe==1.0
    migrate==0.3.8
    MySQL-python==1.2.5
    packaging==16.8
    pyparsing==2.2.0
    python-editor==1.0.3
    six==1.10.0
    SQLAlchemy==1.1.9
    visitor==0.1.3
    Werkzeug==0.12.1
    WTForms==2.1

# Ambiente
Faça o dowload [aqui](https://github.com/danielgalleni/challenge-sensedata/archive/master.zip) do projeto e 
descompacte em seu computador em uma pasta de sua preferência.


Após descompactar o arquivo, abra o terminal, localize o diretório onde está a pasta e digite:

	$ virtualenv challenge-sensedata
	$ cd challenge-sensedata
	$ . bin/activate

Seu terminal ficará com a aparência semelhante a esta:

	(challenge-sensedata) daniel@5750:~/Documents/challenge-sensedata$ 

Este passo é necessário para isolar o ambiente de desenvolvimento do ambiente de produção do seu computador, pois caso haja alguma imcompatibilidade ou erro de algum pacote, apenas o ambiente virtual do env será afeta-
do, evitando assim possíveis manutenções em seu computador.

No próximo passo, precisamos apenas instalar as dependências ou os pacotes requeridos do projeto. Digite o comando:

    $ pip install -r requeriments.txt

# Banco de dados
Executar código para criar o usuário de produção e teste:

	CREATE USER 'admin'@'localhost' IDENTIFIED WITH mysql_native_password AS 'admin';
	GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

	CREATE USER 'teste'@'localhost' IDENTIFIED WITH mysql_native_password AS 'teste';
	GRANT ALL PRIVILEGES ON *.* TO 'teste'@'localhost' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

Executar código para criar banco de dados de produção e teste:

	CREATE DATABASE sensedata;

	CREATE DATABASE sensedata_teste;

Executar código para conceder privilégio ao usuário de produção e teste:

	GRANT ALL PRIVILEGES ON sensedata . * TO 'admin'@'localhost';
	
	GRANT ALL PRIVILEGES ON sensedata_teste . * TO 'teste'@'localhost';

# Para executar

Digite o comando no terminal:

	$ export FLASK_CONFIG=development
	$ export FLASK_APP=run.py
	$ flask run

	*Obs. Altere o parâmetro FLASK_CONFIG para alternar enter "development", "production" e "testing"

Pronto, agora está tudo certo para usar e testar o aplicativo.
Fique a vontade da forkar o projeto e contribuir com ele solicitando um pull request.