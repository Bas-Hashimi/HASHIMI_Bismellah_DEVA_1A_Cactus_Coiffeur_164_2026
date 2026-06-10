# Module 164 2026.02.25

Le "début de la fin"

Le mode d'emploi et vos devoirs se trouvent à l'adresse suivante.

https://info164.github.io/doc164ver1/index.html

# **🛠️ 1. Prérequis (Logiciels à installer)**

Avant de commencer, assurez-vous de disposer des éléments suivants sur votre ordinateur :
Un serveur web local : XAMPP (recommandé), WAMP, ou MAMP.

Il doit inclure Apache, PHP (version 8.0 minimum) et MySQL/MariaDB.

Un navigateur web récent (Chrome, Firefox, Edge, etc.).
Un éditeur de texte/code (Optionnel, ex: VS Code) si vous souhaitez consulter le code source.

# 📥 2. Installation de l'application

Suivez ces étapes pour déployer le projet en local :

### Étape A : Récupérer et placer le projet

Téléchargez le projet sous forme d'archive ZIP depuis GitHub.
Déplacez le dossier extrait dans le répertoire de votre serveur local :

### Étape B : Démarrer le serveur

Ouvrez le panneau de contrôle de votre serveur local.
Démarrez les services Apache et MySQL.

### Étape C : Configuration de la Base de Données

Le projet nécessite une base de données pour fonctionner. Le fichier indispensable est fourni dans le dossier.

### Étape D : Configuration des identifiants (Si applicable)

Si le projet utilise un fichier de configuration pour se connecter à la base de données (ex: config.php, database.php ou un fichier .env), vérifiez que les identifiants correspondent à votre serveur local :
Hôte : localhost ou 127.0.0.1
Nom de la base : hashimi_bismellah_deva_1a_cactus_coiffeur_164_2026
Utilisateur : root

Mot de passe : (laisser vide par défaut sous XAMPP/WAMP)

# 🚀 3. Lancement du projet

Une fois la base de données importée et le serveur allumé, votre application est prête !

Ouvrez votre navigateur web.

Tapez l'URL suivante dans la barre d'adresse (adaptez le nom du dossier si vous l'avez modifié) :
http://localhost/cactus_coiffeur/

Vous devriez maintenant voir la page d'accueil de l'application Cactus Coiffeur.

# 📁 4. Fichiers annexes indispensables inclus

Pour garantir la bonne correction et compréhension du projet, les fichiers suivants sont inclus dans ce dossier :
hashimi_bismellah_deva_1a_cactus_coiffeur_164_2026.sql : Le script complet de création et d'insertion de la base de données.
hashimi_bismellah_deva1a.sql : Le fichier contenant toutes les requêtes CRUD demandées.


