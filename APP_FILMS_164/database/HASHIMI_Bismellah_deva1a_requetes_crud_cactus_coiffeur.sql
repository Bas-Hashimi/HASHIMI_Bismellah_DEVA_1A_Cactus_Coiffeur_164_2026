-- ==============================================================================
-- NOM : HASHIMI
-- PRÉNOM : Bismellah
-- CLASSE : DEVA 1A
-- PROJET : Cactus Coiffeur
-- OBJET : Requêtes CRUD (Create, Read, Update, Delete) de l'application
-- ==============================================================================

-- Sélection de la base de données du projet
USE `hashimi_bismellah_deva_1a_cactus_coiffeur_164_2026`;

-- ==============================================================================
-- 1. CRUD : TABLE `t_client` (Gestion de la Clientèle)
-- ==============================================================================

-- [CREATE] : Ajouter un nouveau client lors de son inscription au salon
INSERT INTO `t_client` (`nom`, `prenom`, `telephone`) 
VALUES ('Dupont', 'Jean', '06 99 88 77 66');

-- [READ] : Lister tous les clients enregistrés dans le salon
SELECT `id_client`, `nom`, `prenom`, `telephone` 
FROM `t_client`;

-- [READ SPECIFIC] : Rechercher un client particulier par son identifiant
SELECT `nom`, `prenom`, `telephone` 
FROM `t_client` 
WHERE `id_client` = 1;

-- [UPDATE] : Modifier le numéro de téléphone d'un client suite à un changement
UPDATE `t_client` 
SET `telephone` = '06 00 11 22 33' 
WHERE `id_client` = 1;

-- [DELETE] : Supprimer la fiche d'un client du système
DELETE FROM `t_client` 
WHERE `id_client` = 21;


-- ==============================================================================
-- 2. CRUD : TABLE `t_employe` (Gestion du Personnel)
-- ==============================================================================

-- [CREATE] : Recruter et enregistrer un nouvel employé (ex: un nouveau Barbier)
INSERT INTO `t_employe` (`nom`, `prenom`, `post`) 
VALUES ('Rousseau', 'Kevin', 'Barbier');

-- [READ] : Afficher la liste de tous les employés et leurs postes respectifs
SELECT `id_employe`, `nom`, `prenom`, `post` 
FROM `t_employe`;

-- [UPDATE] : Promouvoir un employé (changement de poste, ex: Coiffeur devient Coiffeur Senior)
UPDATE `t_employe` 
SET `post` = 'Coiffeur Senior' 
WHERE `id_employe` = 2;

-- [DELETE] : Retirer un employé de la base de données suite à son départ
DELETE FROM `t_employe` 
WHERE `id_employe` = 11;


-- ==============================================================================
-- 3. CRUD : TABLE `t_prestation` (Gestion du Catalogue des Services)
-- ==============================================================================

-- [CREATE] : Ajouter une nouvelle prestation au catalogue du salon
INSERT INTO `t_prestation` (`prix`, `duree`, `libelle`) 
VALUES (45.00, 50, 'Soin Capillaire Premium');

-- [READ] : Consulter l'ensemble des prestations, tarifs et durées associées
SELECT `id_prestation`, `libelle`, `prix`, `duree` 
FROM `t_prestation`
ORDER BY `prix` ASC;

-- [UPDATE] : Modifier le prix d'une prestation (ex: inflation ou stratégie commerciale)
UPDATE `t_prestation` 
SET `prix` = 38.00 
WHERE `id_prestation` = 2; -- Passage de la Coupe Femme à 38.00

-- [DELETE] : Retirer définitivement une prestation obsolète du catalogue
DELETE FROM `t_prestation` 
WHERE `id_prestation` = 17;


-- ==============================================================================
-- 4. CRUD : TABLE `t_produit` (Gestion des Stocks et Produits)
-- ==============================================================================

-- [CREATE] : Ajouter une nouvelle référence de produit reçue d'un fournisseur
INSERT INTO `t_produit` (`nom_produit`, `quantite_stock`, `prix_unitaire`) 
VALUES ('Cire coiffante forte Bio', 15, 16.50);

-- [READ] : Vérifier l'état général des stocks du salon pour le réapprovisionnement
SELECT `id_produit`, `nom_produit`, `quantite_stock`, `prix_unitaire` 
FROM `t_produit`
WHERE `quantite_stock` < 10; -- Alerte sur les stocks bas

-- [UPDATE] : Mettre à jour le stock après réception d'une commande fournisseur (+50 unités)
UPDATE `t_produit` 
SET `quantite_stock` = `quantite_stock` + 50 
WHERE `id_produit` = 1;

-- [DELETE] : Supprimer un produit qui n'est plus commercialisé par le salon
DELETE FROM `t_produit` 
WHERE `id_produit` = 21;


-- ==============================================================================
-- 5. CRUD : TABLE `t_rendez_vous` & TABLES DE LIAISON (Flux Opérationnel)
-- ==============================================================================

-- [CREATE] : Prise de rendez-vous (Étape 1 : Création du RDV principal)
INSERT INTO `t_rendez_vous` (`id_client`, `date_rdv`, `date_annulation`) 
VALUES (1, '2026-05-30 10:00:00', NULL);

-- [CREATE] : Affectation (Étape 2 : Lier le RDV à l'employé n°1 et la prestation n°3)
INSERT INTO `t_rdv_employe` (`id_employe`, `id_rdv`) VALUES (1, 30);
INSERT INTO `t_rdv_prestation` (`id_rdv`, `id_prestation`, `quantite`, `prix_prestation`) VALUES (30, 3, 1, 45.00);

-- [READ] : Visualiser le planning des rendez-vous avec le nom du client et de l'employé
SELECT 
    r.`id_rdv`, 
    r.`date_rdv`, 
    c.`nom` AS client_nom, 
    c.`prenom` AS client_prenom,
    e.`nom` AS employe_nom,
    p.`libelle` AS soin_demande
FROM `t_rendez_vous` r
JOIN `t_client` c ON r.`id_client` = c.`id_client`
JOIN `t_rdv_employe` re ON r.`id_rdv` = re.`id_rdv`
JOIN `t_employe` e ON re.`id_employe` = e.`id_employe`
JOIN `t_rdv_prestation` rp ON r.`id_rdv` = rp.`id_rdv`
JOIN `t_prestation` p ON rp.`id_prestation` = p.`id_prestation`
WHERE r.`date_annulation` IS NULL;

-- [UPDATE] : Annulation d'un rendez-vous par un client (Renseigner la date d'annulation)
UPDATE `t_rendez_vous` 
SET `date_annulation` = '2026-05-29 14:00:00' 
WHERE `id_rdv` = 1;


-- ==============================================================================
-- 6. CRUD : TABLE `t_vendre` (Gestion des Ventes au Comptoir)
-- ==============================================================================

-- [CREATE] : Enregistrer la vente d'un produit en caisse après une prestation
INSERT INTO `t_vendre` (`id_employe`, `id_produit`, `id_client`, `quantite`) 
VALUES (1, 4, 1, 1); -- L'employé 1 vend 1 Huile d'Argan (Produit 4) au client 1

-- [READ] : Historique des ventes pour calculer le chiffre d'affaires des produits
SELECT 
    v.`id_vente`, 
    v.`quantite`, 
    p.`nom_produit`, 
    p.`prix_unitaire`,
    (v.`quantite` * p.`prix_unitaire`) AS total_facture,
    e.`prenom` AS vendeur
FROM `t_vendre` v
JOIN `t_produit` p ON v.`id_produit` = p.`id_produit`
JOIN `t_employe` e ON v.`id_employe` = e.`id_employe`;