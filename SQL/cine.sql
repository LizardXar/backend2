-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 06-12-2024 a las 20:10:39
-- Versión del servidor: 8.2.0
-- Versión de PHP: 8.2.13

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
  `name` varchar(150) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Vendedor'),
(2, 'Cliente');

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
) ENGINE=MyISAM AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 25),
(2, 1, 26),
(3, 1, 27),
(4, 1, 28),
(5, 1, 29),
(6, 1, 30),
(7, 1, 31),
(8, 1, 32),
(9, 1, 33),
(10, 1, 34),
(11, 1, 35),
(12, 1, 36),
(13, 1, 41),
(14, 1, 42),
(15, 1, 43),
(16, 1, 44),
(17, 1, 45),
(18, 1, 46),
(19, 1, 47),
(20, 1, 48),
(21, 1, 49),
(22, 1, 50),
(23, 1, 51),
(24, 1, 52),
(25, 1, 57),
(26, 1, 58),
(27, 1, 59),
(28, 1, 60),
(29, 1, 61),
(30, 1, 62),
(31, 1, 63),
(32, 1, 64),
(33, 2, 32),
(34, 2, 64),
(35, 2, 36),
(36, 2, 44),
(37, 2, 60),
(38, 2, 48),
(39, 2, 52),
(40, 2, 28),
(41, 2, 61);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

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
(56, 'Can view Detalle de Promoción', 14, 'view_detallepromocion'),
(57, 'Can add Función', 15, 'add_funcion'),
(58, 'Can change Función', 15, 'change_funcion'),
(59, 'Can delete Función', 15, 'delete_funcion'),
(60, 'Can view Función', 15, 'view_funcion'),
(61, 'Can add Entrada', 16, 'add_entrada'),
(62, 'Can change Entrada', 16, 'change_entrada'),
(63, 'Can delete Entrada', 16, 'delete_entrada'),
(64, 'Can view Entrada', 16, 'view_entrada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(3, 'pbkdf2_sha256$870000$AQOyLLYaTwG0eBUAvn8iGN$QXOim/4g0ZWlgB28kPR8t0nW2fgj4oXiFw8RzCFdCmU=', NULL, 0, 'clientito', 'Cliente', 'Cineasta', 'cliente@cliente.cliente', 0, 1, '2024-11-29 18:07:59.710973'),
(2, 'pbkdf2_sha256$870000$nFGGVBvoXeoAoJob1G07zB$nNQMI0hiKDssFxSECnMFkMaOWgl0RhxfrwimIoJEH1A=', '2024-11-29 19:08:15.523519', 1, 'ian', '', '', 'ian@ian.ian', 1, 1, '2024-11-29 16:33:15.000000'),
(4, 'pbkdf2_sha256$870000$VWgLWUGJEtjBNy28KLjgbb$swKgseAADyb3UAzZ4Nm32s8814kin8R079pRWYp+orE=', '2024-11-29 19:09:42.516433', 0, 'Gerald', 'Gerald', 'Martinez', 'gerald@gmail.com', 0, 1, '2024-11-29 19:07:15.752323');

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
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 2, 1),
(2, 3, 2),
(3, 4, 2);

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
  `nombreCategoria` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `imagenCategoria` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `descripcion` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
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
  `nombreCategoriaComida` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcionCategoria` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `imagenCatComida` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
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
  `nombre` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `direccion` varchar(300) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `imagenCine` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
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
  `nombre` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `pais` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `imagenCiudad` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
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
  `nombre` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `precio` int NOT NULL,
  `categoria_id` int NOT NULL,
  `imagenComida` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
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
  `object_id` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci,
  `object_repr` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(27, '2024-11-29 16:47:13.588437', '1', 'Vendedor', 1, '[{\"added\": {}}]', 3, 2),
(28, '2024-11-29 16:48:10.494808', '2', 'Cliente', 1, '[{\"added\": {}}]', 3, 2),
(29, '2024-11-29 16:48:24.851439', '2', 'ian', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

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
(14, 'cine', 'detallepromocion'),
(15, 'cine', 'funcion'),
(16, 'cine', 'entrada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

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
(19, 'sessions', '0001_initial', '2024-11-14 06:04:39.641299'),
(20, 'cine', '0002_funcion_entrada', '2024-11-29 16:43:37.879402');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('v3kaaft0n2ytugkf7xwazopea00y6x7d', '.eJxVjEEOwiAQRe_C2hBgKLQu3fcMZGagUjWQlHZlvLtt0oVu_3vvv0XAbc1ha2kJcxRXocXldyPkZyoHiA8s9yq5lnWZSR6KPGmTY43pdTvdv4OMLe81mB4pKYe6szZNHKPRoJAYnHYA1g_YR8dGuQGIdkcjmy5N1lhCD158vtwiN4M:1tBT3G:r2wCwZEZVM4CNdf_A_iw7dkJVadfxqUL7P-L-dLTYdY', '2024-11-28 06:09:58.832929'),
('twzx0vbf34ogi3fsuplrgdjdyqwtp8z9', '.eJxVjrkOwjAYg98lM4raHErDyM4zVP8VEkCp1GOqeHdSqQOMtj9b3tUI25rHbZF5LKyuyqnLr4dAL6lHwE-oj0nTVNe5oD4QfaaLvk8s79vJ_g1kWHJrd5ZIBAL5aBlME0wgNmGIfSKP3gfnmoMoiU3XWxcTyxAHkzCipTZKUNfC0L64zxdA4z37:1tH6NM:-s3DsdSGquGeRWcsVmYpSzGpw1W5IB-Xhj-FmjQVUZ4', '2024-12-13 19:10:00.293390');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `entrada`
--

DROP TABLE IF EXISTS `entrada`;
CREATE TABLE IF NOT EXISTS `entrada` (
  `idEntrada` int NOT NULL AUTO_INCREMENT,
  `precio` int UNSIGNED NOT NULL,
  `vendida` tinyint(1) NOT NULL,
  `funcion_id` int NOT NULL,
  PRIMARY KEY (`idEntrada`),
  KEY `entrada_funcion_id_875180ca_fk_funcion_idFuncion` (`funcion_id`)
) ;

--
-- Volcado de datos para la tabla `entrada`
--

INSERT INTO `entrada` (`idEntrada`, `precio`, `vendida`, `funcion_id`) VALUES
(1, 0, 1, 1),
(2, 0, 1, 1),
(3, 0, 1, 1),
(4, 0, 1, 1),
(5, 5200, 1, 1),
(6, 5200, 1, 1),
(7, 5200, 1, 1),
(8, 5200, 1, 1),
(9, 5200, 1, 1),
(10, 5200, 1, 1),
(11, 5200, 1, 1),
(12, 5200, 1, 1),
(13, 5200, 1, 1),
(14, 5200, 1, 1),
(15, 5200, 1, 1),
(16, 5200, 1, 1),
(17, 5200, 1, 1),
(18, 5200, 1, 1),
(19, 5200, 1, 1),
(20, 5200, 1, 1),
(21, 5200, 1, 1),
(22, 5200, 1, 1),
(23, 5200, 1, 1),
(24, 5200, 1, 1),
(25, 5200, 1, 1),
(26, 5200, 1, 1),
(27, 5200, 1, 1),
(28, 5200, 1, 1),
(29, 5200, 1, 1),
(30, 5200, 1, 1),
(31, 5200, 1, 1),
(32, 5200, 1, 1),
(33, 5200, 1, 2),
(34, 5200, 1, 2),
(35, 5200, 1, 2),
(36, 5200, 1, 2),
(37, 5200, 1, 2),
(38, 5200, 1, 2),
(39, 5200, 1, 2),
(40, 5200, 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `funcion`
--

DROP TABLE IF EXISTS `funcion`;
CREATE TABLE IF NOT EXISTS `funcion` (
  `idFuncion` int NOT NULL AUTO_INCREMENT,
  `fecha_hora` datetime(6) NOT NULL,
  `entradas_disponibles` int UNSIGNED NOT NULL,
  `pelicula_id` int NOT NULL,
  PRIMARY KEY (`idFuncion`),
  KEY `funcion_pelicula_id_4a9b2377_fk_pelicula_idPelicula` (`pelicula_id`)
) ;

--
-- Volcado de datos para la tabla `funcion`
--

INSERT INTO `funcion` (`idFuncion`, `fecha_hora`, `entradas_disponibles`, `pelicula_id`) VALUES
(1, '2024-11-24 09:15:00.000000', 92, 1),
(2, '2024-11-27 23:30:00.000000', 20, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pelicula`
--

DROP TABLE IF EXISTS `pelicula`;
CREATE TABLE IF NOT EXISTS `pelicula` (
  `idPelicula` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcion` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `fecha_estreno` date NOT NULL,
  `duracion` int UNSIGNED NOT NULL,
  `imagenPelicula` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `categoria_id` int NOT NULL,
  PRIMARY KEY (`idPelicula`),
  KEY `pelicula_categoria_id_b9d63cde` (`categoria_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `pelicula`
--

INSERT INTO `pelicula` (`idPelicula`, `titulo`, `descripcion`, `fecha_estreno`, `duracion`, `imagenPelicula`, `categoria_id`) VALUES
(1, 'Ocho Noches de Locura', 'Adam Sandler esta en un dibujo animado, que épico', '2024-11-20', 240, 'peliculas/pelicula.png', 5);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `entrada`
--
ALTER TABLE `entrada`
  ADD CONSTRAINT `entrada_funcion_id_875180ca_fk_funcion_idFuncion` FOREIGN KEY (`funcion_id`) REFERENCES `funcion` (`idFuncion`);

--
-- Filtros para la tabla `funcion`
--
ALTER TABLE `funcion`
  ADD CONSTRAINT `funcion_pelicula_id_4a9b2377_fk_pelicula_idPelicula` FOREIGN KEY (`pelicula_id`) REFERENCES `pelicula` (`idPelicula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
