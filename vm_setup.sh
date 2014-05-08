#!/usr/bin/env bash

ln -fs /vagrant /srv/project

cd  /srv/project
sudo pip install -r requirements.txt

mysql -u root -e "create database development;"
mysql -u root -e "create user 'dropbox'@'localhost' identified by 'dropbox';"
mysql -u root -e "grant all on development.* to 'dropbox'@'localhost';"