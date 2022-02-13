#!/bin/bash

cd ..

if [[ "$VIRTUAL_ENV" != "" ]]
then
  INVENV=1
  echo VENV FOUND
else
  INVENV=0
  echo NO VENV FOUND
fi

if [ $INVENV -eq 1 ]
then
    pip cache purge 
    pip uninstall -r requirements.txt -y
    pip install -r requirements.txt
fi