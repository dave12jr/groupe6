# Déploiement sur AWS EC2

Le workflow **Deploy Flask App to EC2** (`.github/workflows/aws.yml`) déploie cette application sur une instance EC2 à chaque push sur `main`.

## Secrets à configurer dans GitHub

Dans **Settings → Secrets and variables → Actions**, ajoute :

| Secret       | Description                          |
|-------------|--------------------------------------|
| `EC2_SSH_KEY` | Clé privée SSH pour te connecter à l’instance |
| `EC2_HOST`    | Adresse IP ou hostname de l’instance EC2      |
| `EC2_USER`    | Utilisateur SSH (souvent `ubuntu`)           |
| `APP_PORT`    | Port de l’app (ex. `5006`)                   |

## Déroulement du déploiement

1. Checkout du dépôt
2. Connexion SSH à l’instance (clé + host)
3. Copie du projet sur l’instance (SCP)
4. Sur l’instance : `python3 -m venv venv`, `pip install -r requirements.txt`, lancement de `run.py`

L’app tourne en arrière-plan ; les logs sont dans `app.log` sur le serveur.
