#!/bin/bash

# var toma el valor del primer parametro enviado al script
VAR=$1
ENV=""
SSH_ENV=""

PROJECT_FOLDER="GEAOSP_MIR_UC_CEM_WORKFLOWS"

#en caso de que var sea igual a "CASO1", la variable ENV toma un valor y si vale "CASO2", toma otro
case $VAR in
CASO1)
ENV="valor1"
;;
CASO2)
ENV="valor2"
;;
esac

if [ $VAR="CASO1" ]
then
  echo "caso1"
fi


echo "valor de la variable VAR:"
echo $VAR
echo "valor de la variable ENV:"
echo $ENV

#comandos
#comandos
#comandos
