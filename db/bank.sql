-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 30, 2018 at 08:50 AM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bank`
--
CREATE DATABASE IF NOT EXISTS `bank` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `bank`;

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE IF NOT EXISTS `account` (
  `acc_no` varchar(15) NOT NULL,
  `name` varchar(35) NOT NULL,
  `type` varchar(5) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `balance` varchar(25) NOT NULL,
  `loan_availed` varchar(20) NOT NULL DEFAULT '0',
  `lrepay_term` varchar(100) NOT NULL DEFAULT '0',
  `fd_amount` varchar(10) NOT NULL DEFAULT '0',
  `deposit_term` varchar(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`acc_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`acc_no`, `name`, `type`, `mobile`, `balance`, `loan_availed`, `lrepay_term`, `fd_amount`, `deposit_term`) VALUES
('101', 'Raja', 'sb', '9597822446', '46800', '0', '0', '20000', '20'),
('102', 'Hari', 'sb', '9597822557', '27200', '10000', '10', '0', '0'),
('103', 'Venkatesh', 'sb', '9487620975', '1000', '0', '0', '0', '0'),
('105', 'kalathi', 'fd', '9487620975', '1000', '0', '0', '150000', '15'),
('106', 'philip', 'sb', '978654321', '1000', '0', '0', '0', '0'),
('107', 'manik', 'sb', '9894340702', '1000', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `closed`
--

CREATE TABLE IF NOT EXISTS `closed` (
  `acc_no` varchar(15) NOT NULL,
  `name` varchar(30) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  PRIMARY KEY (`acc_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `closed`
--

INSERT INTO `closed` (`acc_no`, `name`, `mobile`) VALUES
('100', 'visanth', '9500964003'),
('108', 'Appa', '1234567890');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `id` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `password`) VALUES
('101', 'hari'),
('103', 'venkat'),
('105', 'venkat'),
('106', 'philip'),
('107', 'raja'),
('admin', 'admin@123');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
