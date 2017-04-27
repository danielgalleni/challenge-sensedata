# challenge-sensedata

    Software desenvolvido mediante desafio, com a proposta de criar um TODO list em Python e Flask, linguagem e framework até então desconhecido.
    Desafio aceito, foram 7 dias de estudo e aprendizagem sobre o universo Python, e posso dizer que me apaixonei pela simplicidade e grandeza de recursos que tem o Python e este pequeno e poderoso framework.

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

digite o comando no terminal:

	$ export FLASK_CONFIG=development
	$ export FLASK_APP=run.py
	$ flask run

	*Obs. Altere o parâmetro FLASK_CONFIG para alternar enter "development", "production" e "testing"