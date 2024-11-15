-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 15-11-2024 a las 11:52:22
-- Versión del servidor: 8.3.0
-- Versión de PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cine`
--
CREATE DATABASE IF NOT EXISTS `cine` DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci;
USE `cine`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Categoría', 7, 'add_categoria'),
(26, 'Can change Categoría', 7, 'change_categoria'),
(27, 'Can delete Categoría', 7, 'delete_categoria'),
(28, 'Can view Categoría', 7, 'view_categoria'),
(29, 'Can add Categoria comida', 8, 'add_categoriacomida'),
(30, 'Can change Categoria comida', 8, 'change_categoriacomida'),
(31, 'Can delete Categoria comida', 8, 'delete_categoriacomida'),
(32, 'Can view Categoria comida', 8, 'view_categoriacomida'),
(33, 'Can add Ciudad', 9, 'add_ciudad'),
(34, 'Can change Ciudad', 9, 'change_ciudad'),
(35, 'Can delete Ciudad', 9, 'delete_ciudad'),
(36, 'Can view Ciudad', 9, 'view_ciudad'),
(37, 'Can add Promoción', 10, 'add_promocion'),
(38, 'Can change Promoción', 10, 'change_promocion'),
(39, 'Can delete Promoción', 10, 'delete_promocion'),
(40, 'Can view Promoción', 10, 'view_promocion'),
(41, 'Can add Cine', 11, 'add_cine'),
(42, 'Can change Cine', 11, 'change_cine'),
(43, 'Can delete Cine', 11, 'delete_cine'),
(44, 'Can view Cine', 11, 'view_cine'),
(45, 'Can add Comida', 12, 'add_comida'),
(46, 'Can change Comida', 12, 'change_comida'),
(47, 'Can delete Comida', 12, 'delete_comida'),
(48, 'Can view Comida', 12, 'view_comida'),
(49, 'Can add Película', 13, 'add_pelicula'),
(50, 'Can change Película', 13, 'change_pelicula'),
(51, 'Can delete Película', 13, 'delete_pelicula'),
(52, 'Can view Película', 13, 'view_pelicula'),
(53, 'Can add Detalle de Promoción', 14, 'add_detallepromocion'),
(54, 'Can change Detalle de Promoción', 14, 'change_detallepromocion'),
(55, 'Can delete Detalle de Promoción', 14, 'delete_detallepromocion'),
(56, 'Can view Detalle de Promoción', 14, 'view_detallepromocion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb3_spanish_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb3_spanish_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb3_spanish_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb3_spanish_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb3_spanish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$870000$YYlHUL0l8jtiWV2LOBrjxn$mGRsiGFef4dNuObuoz4ImqQ78dXAJHg3GNqdh5aGCrM=', '2024-11-14 06:09:58.819910', 1, 'xar', '', '', 'ian@gmail.com', 1, 1, '2024-11-14 06:05:48.856223');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

DROP TABLE IF EXISTS `categoria`;
CREATE TABLE IF NOT EXISTS `categoria` (
  `idCategoria` int NOT NULL AUTO_INCREMENT,
  `nombreCategoria` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `imagenCategoria` varchar(255) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `descripcion` varchar(255) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`idCategoria`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`idCategoria`, `nombreCategoria`, `imagenCategoria`, `descripcion`) VALUES
(1, 'Acción', 'categoria/categoria.png', 'Películas llenas de adrenalina y escenas emocionantes.'),
(2, 'Aventura', 'categoria/categoria.png', 'Historias de viajes, exploraciones y descubrimientos.'),
(4, 'Ciencia Ficción', 'categoria/categoria.png', 'Relatos futuristas que exploran tecnología y el espacio.'),
(5, 'Comedia', 'categoria/categoria.png', 'Películas humorísticas que buscan hacer reír al espectador.'),
(6, 'Drama', 'categoria/categoria.png', 'Dramas intensos que exploran temas emocionales y sociales.'),
(7, 'Fantasia', 'categoria/categoria.png', 'Historias llenas de magia, criaturas míticas y mundos imaginarios.'),
(8, 'Romance', 'categoria/categoria.png', 'Películas románticas que exploran el amor y las relaciones.'),
(9, 'Suspenso', 'categoria/categoria.png', 'Películas llenas de tensión y giros inesperados.'),
(10, 'Terror', 'categoria/categoria.png', 'Películas de terror que buscan asustar y sorprender al espectador.'),
(11, 'Musicales', 'categoria/categoria.png', 'Películas con actuaciones musicales y grandes números de canto y baile.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria_comida`
--

DROP TABLE IF EXISTS `categoria_comida`;
CREATE TABLE IF NOT EXISTS `categoria_comida` (
  `idCategoriaComida` int NOT NULL AUTO_INCREMENT,
  `nombreCategoriaComida` varchar(200) COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcionCategoria` varchar(200) COLLATE utf8mb3_spanish_ci NOT NULL,
  `imagenCatComida` varchar(255) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`idCategoriaComida`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `categoria_comida`
--

INSERT INTO `categoria_comida` (`idCategoriaComida`, `nombreCategoriaComida`, `descripcionCategoria`, `imagenCatComida`) VALUES
(1, 'Palomitas de Maíz', 'Clásicas con sal, con mantequilla, dulces, con sabores, etc', 'catcomida/catcomida.png'),
(2, 'Bebidas', 'Refrescos, Agua, Jugos, Té helados, Café, Bebidas energeticas, etc', 'catcomida/15112024_070500.png'),
(3, 'Dulces y Snacks', 'Chocolates, Gomitas, Caramelos, Galletas, Pretzels, Frutos secos, etc', 'catcomida/15112024_070508.png'),
(4, 'Comida Rápida', 'Hot dogs, Completos, Empanadas, Papas fritas, etc', 'catcomida/15112024_070527.png'),
(5, 'Comida Saludable', 'Frutas, Barras de cereal, Yoghurt, etc', 'catcomida/15112024_070547.png'),
(6, 'Helados y Postres', 'Helado, Sundaes, Pasteles, Brownies, etc', 'catcomida/15112024_070555.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cine`
--

DROP TABLE IF EXISTS `cine`;
CREATE TABLE IF NOT EXISTS `cine` (
  `idCine` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) COLLATE utf8mb3_spanish_ci NOT NULL,
  `direccion` varchar(300) COLLATE utf8mb3_spanish_ci NOT NULL,
  `imagenCine` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  `ciudad_id` int NOT NULL,
  PRIMARY KEY (`idCine`),
  KEY `cine_ciudad_id_368388c5` (`ciudad_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `cine`
--

INSERT INTO `cine` (`idCine`, `nombre`, `direccion`, `imagenCine`, `ciudad_id`) VALUES
(3, 'Cine Hoyts', 'La vuelta de la esquina', 'cine/15112024_030446.png', 2),
(2, 'Cinepolis', 'George Washington 39200', 'cine/15112024_005205.png', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciudad`
--

DROP TABLE IF EXISTS `ciudad`;
CREATE TABLE IF NOT EXISTS `ciudad` (
  `idCiudad` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `pais` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `imagenCiudad` varchar(255) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`idCiudad`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `ciudad`
--

INSERT INTO `ciudad` (`idCiudad`, `nombre`, `pais`, `imagenCiudad`) VALUES
(1, 'Nueva York', 'Estados Unidos', 'ciudad/15112024_070929.png'),
(2, 'La Serena', 'Chile', 'ciudad/15112024_070937.png'),
(3, 'Coquimbo', 'Chile', 'ciudad/15112024_070953.png'),
(5, 'Calama', 'Chile', 'ciudad/15112024_071000.png'),
(6, 'Antofagasta', 'Chile', 'ciudad/15112024_071010.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comida`
--

DROP TABLE IF EXISTS `comida`;
CREATE TABLE IF NOT EXISTS `comida` (
  `idComida` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `precio` int NOT NULL,
  `categoria_id` int NOT NULL,
  `imagenComida` varchar(255) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`idComida`),
  KEY `comida_categoria_id_9885dd11` (`categoria_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `comida`
--

INSERT INTO `comida` (`idComida`, `nombre`, `precio`, `categoria_id`, `imagenComida`) VALUES
(1, 'Caja de palomitas dulces XXL', 20000, 1, 'comidas/comida.png'),
(3, 'Coca-cola 350ml', 900, 2, 'comidas/15112024_063043.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb3_spanish_ci,
  `object_repr` varchar(200) COLLATE utf8mb3_spanish_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb3_spanish_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-11-14 06:10:22.920345', '1', 'Acción', 1, '[{\"added\": {}}]', 7, 1),
(2, '2024-11-14 06:10:27.614328', '2', 'Aventura', 1, '[{\"added\": {}}]', 7, 1),
(3, '2024-11-14 06:10:33.203927', '3', 'Catástrofe', 1, '[{\"added\": {}}]', 7, 1),
(4, '2024-11-14 06:10:39.429368', '4', 'Ciencia Ficción', 1, '[{\"added\": {}}]', 7, 1),
(5, '2024-11-14 06:10:42.842337', '5', 'Comedia', 1, '[{\"added\": {}}]', 7, 1),
(6, '2024-11-14 06:10:46.566635', '6', 'Drama', 1, '[{\"added\": {}}]', 7, 1),
(7, '2024-11-14 06:10:51.242470', '7', 'Fantasia', 1, '[{\"added\": {}}]', 7, 1),
(8, '2024-11-14 06:10:54.564734', '8', 'Romance', 1, '[{\"added\": {}}]', 7, 1),
(9, '2024-11-14 06:11:07.214956', '9', 'Suspenso', 1, '[{\"added\": {}}]', 7, 1),
(10, '2024-11-14 06:11:10.371660', '10', 'Terror', 1, '[{\"added\": {}}]', 7, 1),
(11, '2024-11-14 06:11:17.254187', '11', 'Musicales', 1, '[{\"added\": {}}]', 7, 1),
(12, '2024-11-14 06:12:06.506842', '1', 'Nueva York', 1, '[{\"added\": {}}]', 9, 1),
(13, '2024-11-14 06:12:13.636466', '2', 'La Serena', 1, '[{\"added\": {}}]', 9, 1),
(14, '2024-11-14 06:12:18.532463', '3', 'Coquimbo', 1, '[{\"added\": {}}]', 9, 1),
(15, '2024-11-14 06:12:39.867484', '4', 'Tacna', 1, '[{\"added\": {}}]', 9, 1),
(16, '2024-11-14 06:15:00.493879', '1', 'Palomitas de Maíz', 1, '[{\"added\": {}}]', 8, 1),
(17, '2024-11-14 06:15:56.345863', '2', 'Bebidas', 1, '[{\"added\": {}}]', 8, 1),
(18, '2024-11-14 06:16:22.398853', '3', 'Dulces y Snacks', 1, '[{\"added\": {}}]', 8, 1),
(19, '2024-11-14 06:16:37.673005', '4', 'Comida Rápida', 1, '[{\"added\": {}}]', 8, 1),
(20, '2024-11-14 06:17:09.304116', '5', 'Comida Saludable', 1, '[{\"added\": {}}]', 8, 1),
(21, '2024-11-14 06:17:35.922301', '6', 'Helados y Postres', 1, '[{\"added\": {}}]', 8, 1),
(22, '2024-11-14 06:18:13.017980', '2', 'Bebidas', 2, '[{\"changed\": {\"fields\": [\"DescripcionCategoria\"]}}]', 8, 1),
(23, '2024-11-14 06:18:30.740187', '3', 'Dulces y Snacks', 2, '[{\"changed\": {\"fields\": [\"DescripcionCategoria\"]}}]', 8, 1),
(24, '2024-11-14 06:18:58.375610', '4', 'Comida Rápida', 2, '[{\"changed\": {\"fields\": [\"DescripcionCategoria\"]}}]', 8, 1),
(25, '2024-11-15 00:31:05.884877', '1', 'Promocion 1 4x2  Palomitas XXL', 1, '[{\"added\": {}}]', 10, 1),
(26, '2024-11-15 00:31:14.859232', '1', '4 x Caja de palomitas dulces XXL en Promocion 1 4x2  Palomitas XXL', 1, '[{\"added\": {}}]', 14, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'cine', 'categoria'),
(8, 'cine', 'categoriacomida'),
(9, 'cine', 'ciudad'),
(10, 'cine', 'promocion'),
(11, 'cine', 'cine'),
(12, 'cine', 'comida'),
(13, 'cine', 'pelicula'),
(14, 'cine', 'detallepromocion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-11-14 06:04:29.478248'),
(2, 'auth', '0001_initial', '2024-11-14 06:04:33.034035'),
(3, 'admin', '0001_initial', '2024-11-14 06:04:33.875854'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-11-14 06:04:33.877757'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-14 06:04:33.886925'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-11-14 06:04:34.148662'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-11-14 06:04:34.289415'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-11-14 06:04:34.581979'),
(9, 'auth', '0004_alter_user_username_opts', '2024-11-14 06:04:34.597602'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-11-14 06:04:34.724144'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-11-14 06:04:34.724144'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-11-14 06:04:34.724144'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-11-14 06:04:34.890813'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-11-14 06:04:35.041844'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-11-14 06:04:35.240151'),
(16, 'auth', '0011_update_proxy_permissions', '2024-11-14 06:04:35.240151'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-11-14 06:04:35.568525'),
(18, 'cine', '0001_initial', '2024-11-14 06:04:39.392085'),
(19, 'sessions', '0001_initial', '2024-11-14 06:04:39.641299');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb3_spanish_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb3_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('v3kaaft0n2ytugkf7xwazopea00y6x7d', '.eJxVjEEOwiAQRe_C2hBgKLQu3fcMZGagUjWQlHZlvLtt0oVu_3vvv0XAbc1ha2kJcxRXocXldyPkZyoHiA8s9yq5lnWZSR6KPGmTY43pdTvdv4OMLe81mB4pKYe6szZNHKPRoJAYnHYA1g_YR8dGuQGIdkcjmy5N1lhCD158vtwiN4M:1tBT3G:r2wCwZEZVM4CNdf_A_iw7dkJVadfxqUL7P-L-dLTYdY', '2024-11-28 06:09:58.832929');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pelicula`
--

DROP TABLE IF EXISTS `pelicula`;
CREATE TABLE IF NOT EXISTS `pelicula` (
  `idPelicula` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(200) COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb3_spanish_ci NOT NULL,
  `fecha_estreno` date NOT NULL,
  `duracion` int UNSIGNED NOT NULL,
  `imagenPelicula` varchar(100) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `categoria_id` int NOT NULL,
  PRIMARY KEY (`idPelicula`),
  KEY `pelicula_categoria_id_b9d63cde` (`categoria_id`)
) ;

--
-- Volcado de datos para la tabla `pelicula`
--

INSERT INTO `pelicula` (`idPelicula`, `titulo`, `descripcion`, `fecha_estreno`, `duracion`, `imagenPelicula`, `categoria_id`) VALUES
(1, 'Ocho Noches de Locura', 'Adam Sandler esta en un dibujo animado, que épico', '2024-11-20', 240, 'peliculas/pelicula.png', 5);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
