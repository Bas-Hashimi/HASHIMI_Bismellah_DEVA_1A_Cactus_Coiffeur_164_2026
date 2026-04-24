-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 22 avr. 2026 à 09:40
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `hashimi_bismellah_deva_1a_cactus_coiffeur_164_2026`
--

DROP DATABASE IF EXISTS `hashimi_bismellah_deva_1a_cactus_coiffeur_164_2026`;
CREATE DATABASE IF NOT EXISTS `hashimi_bismellah_deva_1a_cactus_coiffeur_164_2026` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `hashimi_bismellah_deva_1a_cactus_coiffeur_164_2026`;

-- --------------------------------------------------------

--
-- Structure de la table `t_client`
--

CREATE TABLE IF NOT EXISTS `t_client` (
  `id_client` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_client`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_client`
--

INSERT INTO `t_client` (`id_client`, `nom`, `prenom`, `telephone`) VALUES
(1, 'Martin', 'Sophie', '06 12 34 56 78'),
(2, 'Bernard', 'Lucas', '06 23 45 67 89'),
(3, 'Petit', 'Emma', '06 34 56 78 90'),
(4, 'Robert', 'Hugo', '06 45 67 89 01'),
(5, 'Richard', 'Léa', '06 56 78 90 12'),
(6, 'Durand', 'Thomas', '06 67 89 01 23'),
(7, 'Dubois', 'Camille', '06 78 90 12 34'),
(8, 'Moreau', 'Nathan', '06 89 01 23 45'),
(9, 'Laurent', 'Manon', '06 90 12 34 56'),
(10, 'Simon', 'Antoine', '06 01 23 45 67'),
(11, 'Michel', 'Julie', '07 12 34 56 78'),
(12, 'Lefebvre', 'Mathis', '07 23 45 67 89'),
(13, 'Leroy', 'Sarah', '07 34 56 78 90'),
(14, 'Roux', 'Ethan', '07 45 67 89 01'),
(15, 'David', 'Chloé', '07 56 78 90 12'),
(16, 'Bertrand', 'Noah', '07 67 89 01 23'),
(17, 'Morel', 'Lina', '07 78 90 12 34'),
(18, 'Fournier', 'Tom', '07 89 01 23 45'),
(19, 'Girard', 'Jade', '07 90 12 34 56'),
(20, 'Bonnet', 'Louis', '07 01 23 45 67');

-- --------------------------------------------------------

--
-- Structure de la table `t_employe`
--

CREATE TABLE IF NOT EXISTS `t_employe` (
  `id_employe` int(11) NOT NULL AUTO_INCREMENT,
  `nom_employe` varchar(50) DEFAULT NULL,
  `prenom_employe` varchar(50) DEFAULT NULL,
  `post_employe` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_employe`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_employe`
--

INSERT INTO `t_employe` (`id_employe`, `nom_employe`, `prenom_employe`, `post_employe`) VALUES
(1, 'Dupont', 'Marie', 'Coiffeur Senior'),
(2, 'Garcia', 'Jean', 'Coiffeur'),
(3, 'André', 'Claire', 'Coloriste'),
(4, 'Lefranc', 'Pierre', 'Barbier'),
(5, 'Mercier', 'Anna', 'Coiffeur Styliste'),
(6, 'Blanc', 'Marc', 'Coiffeur Senior'),
(7, 'Chevalier', 'Laura', 'Coloriste Senior'),
(8, 'Meyer', 'Paul', 'Coiffeur'),
(9, 'Perrin', 'Julie', 'Coiffeur'),
(10, 'Gauthier', 'Nicolas', 'Barbier');

-- --------------------------------------------------------

--
-- Structure de la table `t_prestation`
--

CREATE TABLE IF NOT EXISTS `t_prestation` (
  `id_prestation` int(11) NOT NULL AUTO_INCREMENT,
  `prix` decimal(10,2) DEFAULT NULL,
  `duree` int(11) DEFAULT NULL,
  `libelle` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_prestation`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_prestation`
--

INSERT INTO `t_prestation` (`id_prestation`, `prix`, `duree`, `libelle`) VALUES
(1, 25.00, 30, 'Coupe Homme'),
(2, 35.00, 45, 'Coupe Femme'),
(3, 45.00, 60, 'Coupe + Brushing Femme'),
(4, 55.00, 90, 'Coupe + Coloration'),
(5, 65.00, 120, 'Coupe + Mèches'),
(6, 15.00, 15, 'Barbe'),
(7, 20.00, 20, 'Taille de barbe + Contours'),
(8, 40.00, 45, 'Shampoing + Soin'),
(9, 30.00, 30, 'Coiffure événementielle'),
(10, 80.00, 150, 'Lissage brésilien'),
(11, 50.00, 60, 'Permanente'),
(12, 35.00, 45, 'Balayage'),
(13, 25.00, 30, 'Défrisage'),
(14, 15.00, 15, 'Chignon simple'),
(15, 45.00, 60, 'Chignon de mariée'),
(16, 10.00, 10, 'Coupe enfant (-12 ans)');

-- --------------------------------------------------------

--
-- Structure de la table `t_produit`
--

CREATE TABLE IF NOT EXISTS `t_produit` (
  `id_produit` int(11) NOT NULL AUTO_INCREMENT,
  `nom_produit` varchar(100) DEFAULT NULL,
  `quantite_stock` int(11) DEFAULT NULL,
  `prix_unitaire` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_produit`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_produit`
--

INSERT INTO `t_produit` (`id_produit`, `nom_produit`, `quantite_stock`, `prix_unitaire`) VALUES
(1, 'Shampoing Réparateur L\'Oréal', 25, 18.50),
(2, 'Après-shampoing Nutrition', 20, 15.90),
(3, 'Masque Capillaire Intense', 15, 22.00),
(4, 'Huile d\'Argan Bio', 30, 24.90),
(5, 'Sérum Anti-Frisottis', 18, 19.50),
(6, 'Laque Fixation Forte', 40, 12.00),
(7, 'Cire Coiffante Mat', 22, 14.50),
(8, 'Gel Coiffant Fort', 35, 9.90),
(9, 'Coloration Permanente Châtain', 50, 8.50),
(10, 'Coloration Permanente Blond', 45, 8.50),
(11, 'Coloration Permanente Noir', 30, 8.50),
(12, 'Oxydant 20 volumes', 60, 4.50),
(13, 'Oxydant 30 volumes', 55, 4.50),
(14, 'Shampoing Sec Volume', 28, 16.90),
(15, 'Baume à Barbe', 20, 18.00),
(16, 'Huile à Barbe Premium', 15, 25.00),
(17, 'Brosse à Cheveux Bois', 12, 12.50),
(18, 'Peigne Démêlant Professionnel', 25, 8.90),
(19, 'Lisseur Vaporisateur', 8, 89.00),
(20, 'Sèche-cheveux Ionique Pro', 6, 120.00);

-- --------------------------------------------------------

--
-- Structure de la table `t_rdv_employe`
--

CREATE TABLE IF NOT EXISTS `t_rdv_employe` (
  `id_employe` int(11) NOT NULL,
  `id_rdv` int(11) NOT NULL,
  PRIMARY KEY (`id_employe`,`id_rdv`),
  KEY `fk_rdve_rdv` (`id_rdv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_rdv_employe`
--

INSERT INTO `t_rdv_employe` (`id_employe`, `id_rdv`) VALUES
(1, 1),
(1, 5),
(1, 13),
(1, 23),
(2, 2),
(2, 9),
(2, 21),
(3, 3),
(3, 11),
(3, 22),
(4, 4),
(4, 14),
(4, 26),
(5, 6),
(5, 16),
(5, 24),
(6, 7),
(6, 17),
(6, 25),
(7, 8),
(7, 18),
(7, 27),
(8, 10),
(8, 19),
(8, 28),
(9, 12),
(9, 20),
(9, 29);

-- --------------------------------------------------------

--
-- Structure de la table `t_rdv_prestation`
--

CREATE TABLE IF NOT EXISTS `t_rdv_prestation` (
  `id_rdv` int(11) NOT NULL,
  `id_prestation` int(11) NOT NULL,
  `quantite` int(11) DEFAULT NULL,
  `prix_prestation` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_rdv`,`id_prestation`),
  KEY `fk_rdvp_pres` (`id_prestation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_rdv_prestation`
--

INSERT INTO `t_rdv_prestation` (`id_rdv`, `id_prestation`, `quantite`, `prix_prestation`) VALUES
(1, 2, 1, 35.00),
(2, 1, 1, 25.00),
(3, 4, 1, 55.00),
(4, 6, 1, 15.00),
(5, 3, 1, 45.00),
(6, 5, 1, 65.00),
(7, 8, 1, 40.00),
(8, 12, 1, 35.00),
(9, 2, 1, 35.00),
(10, 1, 1, 25.00),
(11, 4, 1, 55.00),
(12, 7, 1, 20.00),
(13, 3, 1, 45.00),
(14, 6, 1, 15.00),
(15, 10, 1, 80.00),
(16, 2, 1, 35.00),
(17, 5, 1, 65.00),
(18, 9, 1, 30.00),
(19, 11, 1, 50.00),
(20, 1, 1, 25.00),
(21, 3, 1, 45.00),
(22, 13, 1, 25.00),
(23, 2, 1, 35.00),
(24, 14, 1, 15.00),
(25, 4, 1, 55.00),
(26, 6, 1, 15.00),
(27, 8, 1, 40.00),
(28, 12, 1, 35.00),
(29, 1, 1, 25.00);

-- --------------------------------------------------------

--
-- Structure de la table `t_rendez_vous`
--

CREATE TABLE IF NOT EXISTS `t_rendez_vous` (
  `id_rdv` int(11) NOT NULL AUTO_INCREMENT,
  `id_client` int(11) DEFAULT NULL,
  `date_rdv` datetime DEFAULT NULL,
  `date_annulation` datetime DEFAULT NULL,
  PRIMARY KEY (`id_rdv`),
  KEY `fk_rdv_client` (`id_client`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_rendez_vous`
--

INSERT INTO `t_rendez_vous` (`id_rdv`, `id_client`, `date_rdv`, `date_annulation`) VALUES
(1, 1, '2026-04-21 09:00:00', NULL),
(2, 2, '2026-04-21 10:30:00', NULL),
(3, 3, '2026-04-21 14:00:00', NULL),
(4, 4, '2026-04-21 15:30:00', NULL),
(5, 5, '2026-04-22 09:00:00', NULL),
(6, 6, '2026-04-22 11:00:00', NULL),
(7, 7, '2026-04-22 14:30:00', NULL),
(8, 8, '2026-04-22 16:00:00', NULL),
(9, 9, '2026-04-23 09:30:00', NULL),
(10, 10, '2026-04-23 11:30:00', NULL),
(11, 11, '2026-04-23 14:00:00', NULL),
(12, 12, '2026-04-23 15:30:00', NULL),
(13, 13, '2026-04-24 09:00:00', NULL),
(14, 14, '2026-04-24 10:30:00', NULL),
(15, 15, '2026-04-24 13:30:00', '2026-04-23 18:00:00'),
(16, 16, '2026-04-24 15:00:00', NULL),
(17, 17, '2026-04-25 09:00:00', NULL),
(18, 18, '2026-04-25 10:30:00', NULL),
(19, 19, '2026-04-25 14:00:00', NULL),
(20, 20, '2026-04-25 15:30:00', NULL),
(21, 1, '2026-04-28 10:00:00', NULL),
(22, 3, '2026-04-28 14:00:00', NULL),
(23, 5, '2026-04-29 09:30:00', NULL),
(24, 7, '2026-04-29 11:00:00', NULL),
(25, 9, '2026-04-29 15:00:00', NULL),
(26, 2, '2026-04-30 09:00:00', NULL),
(27, 4, '2026-04-30 10:30:00', NULL),
(28, 6, '2026-04-30 14:00:00', NULL),
(29, 8, '2026-04-30 15:30:00', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `t_vendre`
--

CREATE TABLE IF NOT EXISTS `t_vendre` (
  `id_vente` int(11) NOT NULL AUTO_INCREMENT,
  `id_employe` int(11) DEFAULT NULL,
  `id_produit` int(11) DEFAULT NULL,
  `id_client` int(11) DEFAULT NULL,
  `quantite` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_vente`),
  KEY `fk_v_emp` (`id_employe`),
  KEY `fk_v_prod` (`id_produit`),
  KEY `fk_v_cli` (`id_client`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `t_vendre`
--

INSERT INTO `t_vendre` (`id_vente`, `id_employe`, `id_produit`, `id_client`, `quantite`) VALUES
(1, 1, 1, 1, 1),
(2, 2, 4, 2, 1),
(3, 3, 9, 3, 2),
(4, 4, 15, 4, 1),
(5, 5, 2, 5, 1),
(6, 6, 6, 6, 1),
(7, 7, 10, 7, 1),
(8, 8, 14, 8, 1),
(9, 9, 3, 9, 1),
(10, 1, 7, 10, 1),
(11, 2, 11, 11, 1),
(12, 3, 16, 12, 1),
(13, 4, 5, 13, 1),
(14, 5, 8, 14, 1),
(15, 6, 12, 15, 2),
(16, 7, 17, 16, 1),
(17, 8, 18, 17, 1),
(18, 9, 1, 18, 1),
(19, 1, 4, 19, 1),
(20, 2, 13, 20, 1),
(21, 3, 15, 1, 1),
(22, 4, 2, 3, 1),
(23, 5, 6, 5, 1),
(24, 6, 9, 7, 2),
(25, 7, 11, 9, 1);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `t_rdv_employe`
--
ALTER TABLE `t_rdv_employe`
  ADD CONSTRAINT `fk_rdve_emp` FOREIGN KEY (`id_employe`) REFERENCES `t_employe` (`id_employe`),
  ADD CONSTRAINT `fk_rdve_rdv` FOREIGN KEY (`id_rdv`) REFERENCES `t_rendez_vous` (`id_rdv`);

--
-- Contraintes pour la table `t_rdv_prestation`
--
ALTER TABLE `t_rdv_prestation`
  ADD CONSTRAINT `fk_rdvp_pres` FOREIGN KEY (`id_prestation`) REFERENCES `t_prestation` (`id_prestation`),
  ADD CONSTRAINT `fk_rdvp_rdv` FOREIGN KEY (`id_rdv`) REFERENCES `t_rendez_vous` (`id_rdv`);

--
-- Contraintes pour la table `t_rendez_vous`
--
ALTER TABLE `t_rendez_vous`
  ADD CONSTRAINT `fk_rdv_client` FOREIGN KEY (`id_client`) REFERENCES `t_client` (`id_client`);

--
-- Contraintes pour la table `t_vendre`
--
ALTER TABLE `t_vendre`
  ADD CONSTRAINT `fk_v_cli` FOREIGN KEY (`id_client`) REFERENCES `t_client` (`id_client`),
  ADD CONSTRAINT `fk_v_emp` FOREIGN KEY (`id_employe`) REFERENCES `t_employe` (`id_employe`),
  ADD CONSTRAINT `fk_v_prod` FOREIGN KEY (`id_produit`) REFERENCES `t_produit` (`id_produit`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
