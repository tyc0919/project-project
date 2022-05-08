-- user
INSERT INTO `user` VALUES ('10846017@ntub.edu.tw', 0, 'habi', '1.jpg');
INSERT INTO `user` VALUES ('10846010@ntub.edu.tw', 0, 'doge', '2.jpg');
-- shop genre
INSERT INTO `shop_genre` VALUES
(1, 'food'), 
(2, 'conference'),
(3, 'hotel');

-- shop
INSERT INTO `111401_project`.`shop`
(`account`,
`password`,
`contact_person`,
`shop_name`,
`genre`,
`profile`,
`picture_path`)
VALUES
('shop@gmail.com',
'5D41402ABC4B2A76B9719D911017C592',
'CEO',
'good_shop',
1,
'hello',
'1.jpg');
INSERT INTO `111401_project`.`shop` VALUES
('shop2@gmail.com',
'5D41402ABC4B2A76B9719D911017C592',
'CEO2',
'good_shop2',
1,
'hello2',
'2.jpg');
INSERT INTO `111401_project`.`shop` VALUES
('shop3@gmail.com',
'5D41402ABC4B2A76B9719D911017C592',
'CEO3',
'good_shop3',
3,
'hello3',
'3.jpg');



-- city
INSERT INTO `111401_project`.`city`(`id`,`city_name`) VALUES 
(1,'基隆市'),
(2,'台北市'),
(3,'新北市'),
(4,'桃園縣'),
(5,'新竹市'),
(6,'新竹縣'),
(7,'苗栗縣'),
(8,'台中市'),
(9,'彰化縣'),
(10,'南投縣'),
(11,'雲林縣'),
(12,'嘉義市'),
(13,'嘉義縣'),
(14,'台南市'),
(15,'高雄市'),
(16,'屏東縣'),
(17,'台東縣'),
(18,'花蓮縣'),
(19,'宜蘭縣'),
(20,'澎湖縣'),
(21,'金門縣'),
(22,'連江縣');

-- activity
INSERT INTO `111401_project`.`activity`
(`id`,
`owner`,
`city`,
`activity_name`,
`is_public`,
`content`,
`post_time`,
`invitation_code`)
VALUES
(1,
'10846017@ntub.edu.tw',
2,
'myActivity',
0,
'helloMyActivity',
now(),
'HSC5487');

-- colab_shop
INSERT INTO `111401_project`.`colab_shop`
(`id`,
`shop_account`,
`activity_id`)
VALUES
(1,'shop@gmail.com',1),
(2,'shop2@gmail.com',1),
(3,'shop3@gmail.com',2),
(4,'shop4@gmail.com',3);


INSERT INTO `111401_project`.`collaborator`
(`id`,
`activity_id`,
`user_account`)
VALUES
(1,
1,
'10846017@ntub.edu.tw');


INSERT INTO `111401_project`.`job`
(`id`,
`activity_id`,
`person_in_charge_account`,
`title`,
`order`,
`status`,
`create_time`,
`dead_line`)
VALUES
(1,
1,
'10846010@ntub.edu.tw',
'myFirstJob',
1,
0,
now(),
now());


INSERT INTO `111401_project`.`job_detail`
(`id`,
`job_id`,
`content`,
`order`)
VALUES
(1,
1,
'myFirstJobDetail',
1);

INSERT INTO `111401_project`.`review`
(`id`,
`activity_id`,
`reviewer`,
`content`,
`review_time`,
`review_star`)
VALUES
(1,
1,
'10846010@ntub.edu.tw',
'review1084610',
now(),
5);

INSERT INTO `111401_project`.`serve_city`
(`id`,
`city`,
`shop_account`)
VALUES
(1,
2,
'shop@gmail.com');


