-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 17, 2026 at 04:29 PM
-- Server version: 8.4.3
-- PHP Version: 8.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ico801`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('4994c1c7b78a');

-- --------------------------------------------------------

--
-- Table structure for table `alumnos`
--

CREATE TABLE `alumnos` (
  `id` int NOT NULL,
  `nombre` varchar(250) NOT NULL,
  `apaterno` varchar(50) NOT NULL,
  `amaterno` varchar(150) NOT NULL,
  `edad` int NOT NULL,
  `correo` varchar(100) NOT NULL,
  `created_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `alumnos`
--

INSERT INTO `alumnos` (`id`, `nombre`, `apaterno`, `amaterno`, `edad`, `correo`, `created_date`) VALUES
(3, 'Kyrie', 'Irving', 'Cleveland', 26, 'kirving@cleveland.com', '2026-03-26 08:49:12'),
(4, 'Isaiah', 'Thomas', 'Boston', 25, 'ithomas@boston.com', '2026-03-26 08:50:15'),
(7, 'Nicole', 'Vázquez', 'Hernández', 28, 'nlnvazquezh@gmail.com', '2026-04-09 08:51:21'),
(8, 'Ariadana', 'Amezquita', 'C', 21, 'aamezquita@universidad.com', '2026-04-16 09:32:59'),
(9, 'Antonio', 'Landín', 'A', 28, 'alandin@psicologia.com', '2026-04-16 18:25:01'),
(10, 'Jennifer', 'Cabrera', 'Hernández', 29, 'jcabrerah@informes.com', '2026-04-16 18:37:46'),
(11, 'Carlos', 'Gutiérrez', 'Herrera', 28, 'carlosgherrera@manzanares.com', '2026-04-16 18:38:46'),
(12, 'Brian', 'Zamarron', 'Barron', 28, 'bzamarron@mecatronica.com', '2026-04-16 18:39:31'),
(13, 'Francisco', 'Davalos', 'M', 20, 'franciscod@tecnologico.com', '2026-04-16 18:40:36');

-- --------------------------------------------------------

--
-- Table structure for table `cursos`
--

CREATE TABLE `cursos` (
  `id` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text,
  `maestro_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cursos`
--

INSERT INTO `cursos` (`id`, `nombre`, `descripcion`, `maestro_id`) VALUES
(1, 'Cybersecurity Essentials', 'Curso de (30 horas) enfocado en controles de red y seguridad, y Networking Essentials (70 horas) que prepara para la certificación CCNA.', 4),
(2, 'freeCodeCamp', 'Ofrece 10 certificaciones en áreas como diseño web adaptativo, bibliotecas front-end y desarrollo back-end, con más de 300 horas de contenido por curso y un enfoque 100% práctico.', 1),
(3, 'Herramientas y Protocolos', 'Intro to Packet Tracer (10 horas) para simulaciones de red y NDG Linux Unhatched (8 horas) para comandos esenciales de Linux.', 6),
(5, 'Control de Procesos', 'Control de Procesos', 6),
(6, 'Bases de datos en la nube', 'Identifica, diseña y elige las soluciones de bases de datos más adecuadas dentro del ecosistema AWS, abarcando servicios SQL como Amazon RDS y Aurora, y NoSQL como DynamoDB, Neptune y DocumentDB.', 9),
(14, 'español', 'español', 4);

-- --------------------------------------------------------

--
-- Table structure for table `inscripciones`
--

CREATE TABLE `inscripciones` (
  `id` int NOT NULL,
  `alumno_id` int NOT NULL,
  `curso_id` int NOT NULL,
  `fecha_inscripcion` datetime DEFAULT (now())
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `inscripciones`
--

INSERT INTO `inscripciones` (`id`, `alumno_id`, `curso_id`, `fecha_inscripcion`) VALUES
(2, 3, 1, '2026-04-16 08:29:00'),
(4, 7, 2, '2026-04-16 08:29:18'),
(5, 13, 2, '2026-04-16 20:04:15'),
(7, 4, 5, '2026-04-16 20:10:10'),
(17, 4, 1, '2026-04-17 09:09:49');

-- --------------------------------------------------------

--
-- Table structure for table `maestros`
--

CREATE TABLE `maestros` (
  `matricula` int NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellidos` varchar(50) DEFAULT NULL,
  `especialidad` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `maestros`
--

INSERT INTO `maestros` (`matricula`, `nombre`, `apellidos`, `especialidad`, `email`) VALUES
(1, 'Gerardo', 'Carpio Flores', 'Software Development', 'gcarpiof@gmail.com'),
(4, 'Roberto', 'Gallegos Muñoz', 'Network Engineer', 'rgallegosm@gmail.com'),
(6, 'Christian', 'Aguilera', 'Information Technology', 'caguilera@itecnologico.com'),
(9, 'Blanca', 'Martínez', 'Data Base Manager', 'bmartinez@database.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `maestro_id` (`maestro_id`);

--
-- Indexes for table `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_alumno_curso` (`alumno_id`,`curso_id`),
  ADD KEY `curso_id` (`curso_id`);

--
-- Indexes for table `maestros`
--
ALTER TABLE `maestros`
  ADD PRIMARY KEY (`matricula`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `inscripciones`
--
ALTER TABLE `inscripciones`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `maestros`
--
ALTER TABLE `maestros`
  MODIFY `matricula` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cursos`
--
ALTER TABLE `cursos`
  ADD CONSTRAINT `cursos_ibfk_1` FOREIGN KEY (`maestro_id`) REFERENCES `maestros` (`matricula`);

--
-- Constraints for table `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD CONSTRAINT `inscripciones_ibfk_1` FOREIGN KEY (`alumno_id`) REFERENCES `alumnos` (`id`),
  ADD CONSTRAINT `inscripciones_ibfk_2` FOREIGN KEY (`curso_id`) REFERENCES `cursos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
