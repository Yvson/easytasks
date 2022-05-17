
# Preparing the VPS
These are the steps needed to be done in order to deploy the easytasks project.

## Steps
1. To install the basic software:
	- Nginx
	- PostgreSQL
	- Certbot
	- Pyenv (Python Version Manager)

2. To configure the VPS environment:
	- To create a user named "easytasks" with no superuser privileges and part of sudo group;
	- To set root user not accessible via bash/tty and ssh;
	- To create a role named "easytasks" in postgres environment;
	- To create a database named "easytasks" owned by "easytasks" role and set its password;
	- To include nginx.conf file of easytasks projects in /etc/nginx/nginx.conf
	-  To edit /etc/hosts file and add "www.easytasks.com.br" and "easytasks.com.br" domains to the local server (127.0.0.1);
	- To use pyenv to install the latest python version;

3. To create the repository of the project in Hostinger panel:
	- To name the repository "easytasks";

4. To use Github Actions to do CI/CD with the Hostinger repository:
	- To create main.yml in the repository directory inside .github/workflows folder;
	- To set up all routine before deploying the latest changes of the project;

5. To create a python environment and install the third-party libraries:
	- The production file is requirements/production.txt;
	- To collect static files with "python manage.py collectstatic" command;

6. To configure repeated actions with crontab:
	- To edit scheduler/cotacoes_update.sh file and check the commands that update currencies and cryptocurrencies values;
	- To edit crontab to execute scheduler/cotacoes_update.sh file every minute;

7. To configure uWSGI settings and run server:
	- To set uWSGI.ini file;
	- To run uWSGI server;