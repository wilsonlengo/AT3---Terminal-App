#!/bin/bash
python3 -m ensurepip --upgrade

pip3 install virtualenv 

virtualenv appvenv

source appvenv/bin/activate

pip3 install -r requirements.txt

#installs pip and creates requirements.txt
