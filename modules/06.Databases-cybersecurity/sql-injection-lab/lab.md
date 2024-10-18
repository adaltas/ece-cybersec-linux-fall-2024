# SQL injection lab

Installer python 3 en derniere version
Installer la dependance duckdb

```bash
pip install duckdb
```

## Populate DB

lancer le script populate_db.py. Cela va créer la base de données avec un seul utilisateur, admin.

## unsecure_login

unsecure_login est une implémentation naïve d’un système d’authentification

Si le user password est correct, alors unsecure_login renvoit 0 (pas d’erreur) et un message 'login successful'

Vérifier unsecure_login en situation nominale

### Normal failures

Ces commandes doivent échouer
```bash
./unsecure_login.py
./unsecure_login.py toto tutu
./unsecure_login.py admin tutu
```

### Success

La commande suivante doit fonctionner:
```bash
./unsecure_login.py admin password123
```


## Exercice

Il y a plusieurs risques possibles: le vol de données, la destruction de données, l’injection de données frauduleuses.
Nous testerons ici les deux derniers.

1. Seriez vous capable d’obtenir login successful SANS specifier un mot de passe correct ?

2. Via les SQL injections, Ajouter un user toto avec le mot de passe toto123. Verifier que cet utilisateur est valide via 

```bash
./unsecure_login toto toto123
```

3. Via une sql injection, changer le mot de passe admin. Vous pouvez relancer populate_db au besoin.


4. Via une sql injection, détruisez les données. Verifier que le compte admin ne peut plus se logger. Vous pouvez relancer populate_db au besoin.

5. Corriger unsecure_login en conservant le meme mecanisme, mais en utilisant des PreparedStatement
