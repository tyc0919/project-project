DROP DATABASE `111401_project`;
CREATE DATABASE `111401_project`;

USE `111401_project`;

-- 建立資料表 '使用者'
CREATE TABLE `user`(
	`user_email` char(30) PRIMARY KEY,
    `password` char(130),
    `user_name` char(15),
    `picture_path` varchar(50) DEFAULT NULL, -- 圖片路徑存法: 只要檔名
    `telephone` char(10) DEFAULT NULL,
    `enable` tinyint DEFAULT 0,
    `enable_time` datetime
);



-- 建立資料表 '企劃'
CREATE TABLE `activity`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `owner` char(30) NOT NULL,
    `activity_name` varchar(30) NOT NULL,
    `is_public` tinyint DEFAULT 0,
    `is_finished` tinyint DEFAULT 0,
    `content` text DEFAULT NULL,
    `create_time` datetime,
    `post_time` datetime,
    `invitation_code` char(20),
    `activity_picture` varchar(50),
	`activity_budget` int,
    `activity_description` text,
    FOREIGN KEY(`owner`) REFERENCES `user`(`user_email`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 建立資料表 '協作人員'
CREATE TABLE `collaborator` (
   `id` int PRIMARY KEY AUTO_INCREMENT,
   `activity_id` int NOT NULL,
    `user_email` char(30) NOT NULL,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`user_email`) REFERENCES `user`(`user_email`) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (`activity_id`, `user_email`)
);


-- 建立資料表 '工作'
CREATE TABLE `job`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `activity_id` int ,
    `person_in_charge_email` char(30), -- 負責人
    `title` varchar(15),
	`order` int, -- 序號
    `status` tinyint DEFAULT 0,
    `create_time` datetime, -- 建立時間
    `dead_line` datetime,	-- 到期時間
    `content` text,
    `job_budget` int,
    `job_expenditure` int,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`person_in_charge_email`) REFERENCES `user`(`user_email`) ON DELETE CASCADE ON UPDATE CASCADE
);	

-- 建立資料表 '工作細項'
CREATE TABLE `job_detail`(
	`job_detail_id` int PRIMARY KEY AUTO_INCREMENT,
    `title` varchar(15),
    `content` text,
    `job_id` int,
    `activity_id` int,
    `status` tinyint Default 0,
	FOREIGN KEY(`job_id`) REFERENCES `job`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `review`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `activity_id` int,
    `reviewer` char(30),
    `content` varchar(500),
    `review_time` datetime,
    `review_star` tinyint,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`reviewer`) REFERENCES `user`(`user_email`) ON DELETE CASCADE ON UPDATE CASCADE
);



CREATE TABLE `file`(
	`id` int PRIMARY KEY auto_increment,
    `activity_id` int ,
	`job_id` int,
    `uploader` char(30),
    `file_path` varchar(50) DEFAULT NULL,
    `file_uploaded_time` datetime,
    FOREIGN KEY(`uploader`) REFERENCES `user`(`user_email`) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(`job_id`) REFERENCES `job`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `expenditure`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
	`job_id` int,
    `activity_id` int ,
    `expense` int Default 0,
    `expenditure_receipt_path` varchar(50) DEFAULT NULL,
    `expenditure_uploaded_time` datetime,
    `is_deleted` tinyint Default 0,
	FOREIGN KEY(`job_id`) REFERENCES `job`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `log`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `activity_id` int,
    `user_email` char(30),
    `action` varchar(50),
    `time` datetime,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`user_email`) REFERENCES `user`(`user_email`) ON DELETE CASCADE ON UPDATE CASCADE
);
    
CREATE TABLE `invitation_list` (
    `id` int PRIMARY KEY AUTO_INCREMENT,
    `activity_id` int NOT NULL,
    `user_email` char(30) NOT NULL,
    `invitation_code` char(20),
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`user_email`) REFERENCES `user`(`user_email`) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (`activity_id`, `user_email`)
);