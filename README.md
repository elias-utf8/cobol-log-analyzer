# cobol-log-analyzer
> Projet sous développement, seule la lecture de fichier et analyse de base sont implémentés!
## Description

`cobol-log-analyzer` est une application CLI écrite en COBOL avec objectif de lire et d'analyser des fichiers volumineux de logs. Initialement conçu sous IBM Z/OS, ceci est une version compatible avec des compilateurs gratuits tel que GnuCOBOL.

## Compilation 
```sh
cobc -x ./main.cbl -o main log_reader
```
Puis `./log_reader`
