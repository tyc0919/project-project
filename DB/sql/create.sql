-- 建立資料庫
CREATE DATABASE `111401_project`;

USE `111401_project`;
-- 建立資料表 '使用者'
CREATE TABLE `user`(
	`account` char(30) PRIMARY KEY,
    -- remove role 
    `password` char(70),
    `name` char(15),
    `picture_path` varchar(50) DEFAULT NULL -- 圖片路徑存法: 只要檔名
);

-- 建立資料表 '店家分類'
CREATE TABLE `shop_genre`(
	`id` int PRIMARY KEY,
    `genre` char(15)
);

-- 建立資料表 '店家'
CREATE TABLE `shop`(
	`account` char(30) PRIMARY KEY,
    `password` char(70),
    `contact_person` char(15) DEFAULT NULL, -- 聯絡人
    `shop_name` varchar(30),
    `genre`  int, -- 分類需要使用編號
    `profile` text DEFAULT NULL,
    `picture_path` varchar(50) DEFAULT NULL,
    FOREIGN KEY(`genre`) REFERENCES `shop_genre`(`id`) ON DELETE CASCADE
);



-- 建立資料表 '縣市'
CREATE TABLE `city`(
	`id` int PRIMARY KEY  AUTO_INCREMENT,
    `city_name` char(3)
);
-- 建立資料表 '服務地點'
CREATE TABLE `serve_city`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `city` int,
    `shop_account` char(30),
    FOREIGN KEY(`city`) REFERENCES `city`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`shop_account`) REFERENCES `shop`(`account`) ON DELETE CASCADE ON UPDATE CASCADE
); 

-- 建立資料表 '企劃'
CREATE TABLE `activity`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `owner` char(30) NOT NULL,
    `city` int DEFAULT NULL,
    `activity_name` varchar(30) NOT NULL,
    `is_public` int DEFAULT 0,
    `content` text DEFAULT NULL,
    `post_time` datetime,
    `invitation_code` char(20),
    FOREIGN KEY(`city`) REFERENCES `city`(`id`)  ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY(`owner`) REFERENCES `user`(`account`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 建立資料表 '協作人員'
CREATE TABLE `collaborator`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `activity_id` int NOT NULL,
    `user_account` char(30) NOT NULL,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`user_account`) REFERENCES `user`(`account`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 建立資料表 '工作'
CREATE TABLE `job`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `activity_id` int ,
    `person_in_charge_account` char(30), -- 負責人
    `title` varchar(15),
	`order` int UNIQUE NOT NULL, -- 序號
    `status` int DEFAULT 0,
    `create_time` datetime, -- 建立時間
    `dead_line` datetime,	-- 到期時間
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`person_in_charge_account`) REFERENCES `user`(`account`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 建立資料表 '工作細項'
CREATE TABLE `job_detail`(
	`id` int PRIMARY KEY,
    `job_id` int,
    `content` text,
    `order` int UNIQUE NOT NULL,
    FOREIGN KEY(`job_id`) REFERENCES `job`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `review`(
	`id` int PRIMARY KEY,
    `activity_id` int,
    `reviewer` char(30),
    `content` varchar(500),
    `review_time` datetime,
    `review_star` int,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`reviewer`) REFERENCES `user`(`account`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `colab_shop`(
	`id` int PRIMARY KEY,
	`shop_account` char(30),
    `activity_id` int,
    FOREIGN KEY(`shop_account`) REFERENCES `shop`(`account`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
);
