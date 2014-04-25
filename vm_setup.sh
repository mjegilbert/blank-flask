#!/usr/bin/env bash

ln -fs /vagrant /srv/project

cd  /srv/project
sudo pip install -r requirements.txt
