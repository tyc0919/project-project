USE `111401_project`;
-- CREATE DATABASE `111401_project`;
-- DROP DATABASE `111401_project`;

-- 建立資料表 '使用者'
CREATE TABLE `user`(
	`user_email` char(30) PRIMARY KEY,
    `password` char(130),
    `user_name` char(15),
    `picture_path` varchar(50) DEFAULT NULL, -- 圖片路徑存法: 只要檔名
    `telephone` char(10) DEFAULT NULL,
    `enable` int DEFAULT 0,
    `enable_time` datetime
);

-- 建立資料表 '店家分類'
CREATE TABLE `shop_genre`(
	`id` int PRIMARY KEY,
    `genre` char(15)
);

-- 建立資料表 '店家'
CREATE TABLE `shop`(
	`shop_email` char(30) PRIMARY KEY,
    `password` char(130),
    `contact_person` char(15) DEFAULT NULL, -- 聯絡人
    `shop_name` varchar(30),
    `genre`  int, -- 分類需要使用編號
    `profile` text DEFAULT NULL,
    `picture_path` varchar(50) DEFAULT NULL,
    `enable` int DEFAULT 0,
    `enable_time` datetime,
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
    `shop_email` char(30),
    FOREIGN KEY(`city`) REFERENCES `city`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`shop_email`) REFERENCES `shop`(`shop_email`) ON DELETE CASCADE ON UPDATE CASCADE
); 

-- 建立資料表 '企劃'
CREATE TABLE `activity`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `owner` char(30) NOT NULL,
    `city` int DEFAULT NULL,
    `activity_name` varchar(30) NOT NULL,
    `is_public` int DEFAULT 0,
    `is_finished` int DEFAULT 0,
    `content` text DEFAULT NULL,
    `post_time` datetime,
    `invitation_code` char(20),
    `activity_picture` varchar(50),
    FOREIGN KEY(`city`) REFERENCES `city`(`id`)  ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY(`owner`) REFERENCES `user`(`user_email`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 建立資料表 '協作人員'
CREATE TABLE `collaborator`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `activity_id` int NOT NULL,
    `user_email` char(30) NOT NULL,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`user_email`) REFERENCES `user`(`user_email`) ON DELETE CASCADE ON UPDATE CASCADE
);


-- 建立資料表'工作狀態'
CREATE TABLE `job_status`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `status_name` char(10)
);
-- 建立資料表 '工作'
CREATE TABLE `job`(
	`id` int PRIMARY KEY AUTO_INCREMENT,
    `activity_id` int ,
    `person_in_charge_email` char(30), -- 負責人
    `title` varchar(15),
	`order` int UNIQUE NOT NULL, -- 序號
    `status` int DEFAULT 0,
    `create_time` datetime, -- 建立時間
    `dead_line` datetime,	-- 到期時間
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`person_in_charge_email`) REFERENCES `user`(`user_email`) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(`status`) REFERENCES `job_status`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
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
    FOREIGN KEY(`reviewer`) REFERENCES `user`(`user_email`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `collab_shop`(
	`id` int PRIMARY KEY,
	`shop_email` char(30),
    `activity_id` int,
    `shop_permittion` int default 0,
    FOREIGN KEY(`shop_email`) REFERENCES `shop`(`shop_email`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(`activity_id`) REFERENCES `activity`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
);


