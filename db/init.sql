DROP SCHEMA IF EXISTS `Kaught`;


CREATE SCHEMA IF NOT EXISTS `Kaught` ;
USE `Kaught` ;

CREATE TABLE IF NOT EXISTS `Kaught`.`user`(
    `username`    VARCHAR(30) NOT NULL,
    `haspass`     VARCHAR(100) NOT NULL,
    PRIMARY KEY(`username`)
);

CREATE TABLE IF NOT EXISTS `Kaught`.`task`(
    `taskID`      INT NOT NULL AUTO_INCREMENT,
    `desc`        VARCHAR(300) NOT NULL,
    `complete`    INT NOT NULL DEFAULT 0,
    `where`       DATA NOT NULL,
    `timedue`     TIME,
    PRIMARY KEY(`taskID`)
);

CREATE TABLE IF NOT EXISTS `Kaught`.`runable`(
    `runableID`     INT NOT NULL AUTO_INCREMENT,
    `desc`          VARCHAR(200) NOT NULL,
    `lastRan`       DATETIME,
    PRIMARY KEY(`runableID`)
);

