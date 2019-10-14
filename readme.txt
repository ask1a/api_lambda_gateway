1/ Monter l'image docker d'une lambda aws python3.6 (pour la suite il est important d'executer cette commande depuis le dossier du layer que l'on souhaite creer):

docker run --rm -it -v ${PWD}:/var/task lambci/lambda:build-python3.6 bash



2/ Commande à lancer dans le container pour installer les packages listés dans requirement.txt à l'endroit indiqué en parametre(cette structure de dossier est necessaire pour fonctionner dans un layer lambda):

pip install -r requirements.txt --no-deps -t python/lib/python3.6/site-packages/



3/ zipper le dossier python du layer:

python zip_layers.py



4/ creer modele basique, l'enregistrer, le zipper:

python build_model.py



5/ on créé dans lambda le layer scipy/numpy (présent par défaut) ensuite, on pousse les zip sur S3 et on en créé des layers

6/ on test les layers avec les codes de test pandas et scikit

7/ on écrit la fonction finale contenu dans "code_lambda_function_appel_modele_scikit.py"

8/ on créé une nouvelle api REST dans api_gateway

9/ dans "ressource" on ajoute une action "POST" qui se réfère à la lambda créé plus tot

10/ on ajoute ensuite une action "deployer api" on nomme l'etape et on laisse param par defaut

11/ URL de l'api accessible dans etape

12/ on test l'api:

python tests/test_api.py




