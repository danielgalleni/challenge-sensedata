# challenge-sensedata

# Requisitos
    Python 3.7
    Flask
    Migrate

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

1- Para executar, digite o comando no terminal:

	$ export FLASK_CONFIG=development
	$ export FLASK_APP=run.py
	$ flask run

	*Obs. Altere o parâmetro FLASK_CONFIG para alternar enter "development", "production" e "testing"
