# Récapitulatif des Changements

## Remplacement de data.json par une interaction avec Amazon RDS
   Le fichier data.json a été remplacé par une connexion à une base de données PostgreSQL hébergée sur Amazon RDS.
L'ancienne logique de lecture et d'écriture dans le fichier JSON a été modifiée pour utiliser psycopg2 afin d'interagir avec la base de données.

### Avantage 
 Une base de données relationnelle comme RDS est conçue pour gérer des volumes de données importants et permet de gérer des milliers voire des millions de lignes de manière performante. Elle permet également des requêtes efficaces et optimisées sur de grands ensembles de données grâce aux index et à la gestion des transactions.

## Création et Configuration du Dockerfile et les manifests K8s

## Ajout de Gunicorn pour la production
Gunicorn gère la montée en charge verticale en augmentant le nombre de workers dans un pod.

## Création du GitHub Action Workflow
pour mettre une pipeline ci/cd afin d'automatisé le workflow

## Déploiement sous EKS
pour plus d'optimisation, sécurité et scalabilité.

# To Do
## Configuration des vars d'env et les secrets sur github
## Création des ressources coté AWS 
vpc, security grp, bdd rds, cluster eks, loadbalancer, iam roles...
de préférence avec une approche Iac avec Terraform.
## Amélioration de la CI
Déclenchement basé sur pull request : test unitaire, lint, format(pas d'actions de CD)
Déclenchement basé sur un nouveau tag : build d'image , deploiement de la solution dans un environnement de prod

## Adopté une architecture Blue Green
séparer les deux environnement pour ne pas causer d'indisponibilité.
il faut définir deux deployments et Gérer les services via le fichier service.yaml pour orienter le trafic vers le Blue ou le Green selon l'environnement.