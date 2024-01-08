
create database face_recognition;
use face_recognition;
CREATE TABLE `register` (
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `secq` varchar(45) DEFAULT NULL,
  `seca` varchar(45) DEFAULT NULL,
  `pass` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`email`)
); 



create database hotel_management_system;
use hotel_management_system;

CREATE TABLE `addroom` (
  `floor` varchar(45) DEFAULT NULL,
  `roomno` varchar(45) NOT NULL,
  `roomtype` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`roomno`)
);

CREATE TABLE `customer` (
  `ref` int NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `mother` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `postcode` varchar(45) DEFAULT NULL,
  `mobile` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `nation` varchar(45) DEFAULT NULL,
  `idproof` varchar(45) DEFAULT NULL,
  `idnumber` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ref`)
);

CREATE TABLE `feedback` (
  `user` varchar(45) NOT NULL,
  `feedback` varchar(45) NOT NULL,
  PRIMARY KEY (`user`)
);

CREATE TABLE `room` (
  `ref` varchar(45) DEFAULT NULL,
  `checkin` varchar(45) DEFAULT NULL,
  `checkout` varchar(45) DEFAULT NULL,
  `roomtype` varchar(45) DEFAULT NULL,
  `avlroom` varchar(45) NOT NULL,
  `meal` varchar(45) DEFAULT NULL,
  `noofdays` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`avlroom`)
);


CREATE TABLE `user` (
  `name` varchar(255) DEFAULT NULL,
  `password` varchar(80) DEFAULT NULL
);
