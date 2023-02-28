# Hackernews



## Getting started
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx

sudo -u postgres psql
postgres=# create database chatgpt;
postgres=# create user vmm with password 'vmm';
postgres=# ALTER ROLE vmm SET client_encoding TO 'utf8';
postgres=# ALTER ROLE vmm SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE vmm SET timezone TO 'UTC';
postgres=# GRANT ALL PRIVILEGES ON DATABASE chatgpt TO vmm;
```

## Clone
- ``


## Deployment
python3 -m pipenv shell

## Kill process
- lsof -i:8000
- kill -9 <PID>