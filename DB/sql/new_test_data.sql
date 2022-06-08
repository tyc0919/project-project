use `111401_project`;
-- user
-- pwd = sha256(test)
INSERT INTO `user` VALUES ('10846017@ntub.edu.tw', 'ce351470542b4a638d0eca628a0eba0e594f0161c8ae4f1ca54b28c74762dc07$e860a501b0dd2e47073f928d5b9bcd8ba3eced9e091a0c5ee09108fe54e8b309', '黃XX', '1.jpg','0976448885',1,now()); 
INSERT INTO `user` VALUES ('10846010@ntub.edu.tw', 'ce351470542b4a638d0eca628a0eba0e594f0161c8ae4f1ca54b28c74762dc07$e860a501b0dd2e47073f928d5b9bcd8ba3eced9e091a0c5ee09108fe54e8b309', '曾XX', '2.jpg','0952802983',1,now());
INSERT INTO `user` VALUES ('test@gmail.com', 'ce351470542b4a638d0eca628a0eba0e594f0161c8ae4f1ca54b28c74762dc07$e860a501b0dd2e47073f928d5b9bcd8ba3eced9e091a0c5ee09108fe54e8b309', '測試者', '2.jpg','0952802983',1,now());

-- shop genre
INSERT INTO `shop_genre` VALUES
(1, 'food'), 
(2, 'conference'),
(3, 'hotel');


-- city
INSERT INTO `city`(`id`,`city_name`) VALUES 
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

-- shop
INSERT INTO`shop`
VALUES
('10846015@ntub.edu.tw',
'8EFC336430B427923869C1722463FB3F41615A0C0DC419E84ED78D2A74C4F9FD', 
'no_name',
'food_shop',
1,
'hello',
'3.jpg',
1,
now(),
2);
INSERT INTO `shop` VALUES
('10846002@ntub.edu.tw',
'8EFC336430B427923869C1722463FB3F41615A0C0DC419E84ED78D2A74C4F9FD',
'魏XX',
'food shop',
1,
'hello!!!!',
'4.jpg',
1,
now(),
2);
INSERT INTO `shop` VALUES
('10846014@ntub.edu.tw',
'8EFC336430B427923869C1722463FB3F41615A0C0DC419E84ED78D2A74C4F9FD',
'胡XX',
'hotel shop',
3,
'hello3',
'5.jpg',
1,
now(),
2);

-- activity
INSERT INTO `activity` VALUES
(1,
'10846017@ntub.edu.tw',
2,
'myActivity',
0,
0,
'helloMyActivity',
now(),
'HSC5487',
'6.jpg');

INSERT INTO `activity` VALUES
(2,
'test@gmail.com',
2,
'myActivity',
0,
0,
'testMyActivity',
now(),
'HSC5487',
'6.jpg');

INSERT INTO `activity` VALUES
(3,
'test@gmail.com',
2,
'testActivity3',
0,
0,
'testMyActivity',
now(),
'HSC5487',
'6.jpg');

-- colab_shop
INSERT INTO `collab_shop`
(`id`,
`shop_email`,
`activity_id`,
`shop_permission`)
VALUES
(1,'10846015@ntub.edu.tw',1,0),
(2,'10846002@ntub.edu.tw',1,0);


INSERT INTO `collaborator`
(`activity_id`,
`user_email`)
VALUES
(1,
'10846010@ntub.edu.tw');


INSERT INTO `collaborator`
(`activity_id`,
`user_email`)
VALUES
(1,
'test@gmail.com');


INSERT INTO `job_status` VALUES
(1,'未完成'),
(2,'進行中'),
(3,'已完成');

INSERT INTO `job`
VALUES
(1,
1,
'10846017@ntub.edu.tw',
'myFirstJob',
1,
1,
now(),
date_add(now(), interval 1 month),
'就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來說，你媽對我的意義，不能不說非常重大。經過上述討論，就我個人來說，你媽對我的意義就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來');

INSERT INTO `job`
VALUES
(2,
2,
'test@gmail.com',
'testJob',
2,
1,
now(),
date_add(now(), interval 1 month),
'就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來說，你媽對我的意義，不能不說非常重大。經過上述討論，就我個人來說，你媽對我的意義就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來');


INSERT INTO `job`
VALUES
(3,
2,
'test@gmail.com',
'testJob3',
2,
1,
now(),
date_add(now(), interval 1 month),
'testjob2就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來說，你媽對我的意義，不能不說非常重大。經過上述討論，就我個人來說，你媽對我的意義就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來');

INSERT INTO `job`
VALUES
(4,
2,
'test@gmail.com',
'testJob3',
2,
1,
now(),
date_add(now(), interval 1 month),
'testjob3就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來說，你媽對我的意義，不能不說非常重大。經過上述討論，就我個人來說，你媽對我的意義就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來');


INSERT INTO `job`
VALUES
(5,
3,
'test@gmail.com',
'testJob4',
2,
1,
now(),
date_add(now(), interval 1 month),
'testjob4就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來說，你媽對我的意義，不能不說非常重大。經過上述討論，就我個人來說，你媽對我的意義就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來');

INSERT INTO `job`
VALUES
(6,
3,
'test@gmail.com',
'testJob5',
2,
1,
now(),
date_add(now(), interval 1 month),
'testjob5就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來說，你媽對我的意義，不能不說非常重大。經過上述討論，就我個人來說，你媽對我的意義就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來');

INSERT INTO`job`
VALUES
(7,
3,
'test@gmail.com',
'testJob6',
2,
1,
now(),
date_add(now(), interval 1 month),
'testjob6就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來說，你媽對我的意義，不能不說非常重大。經過上述討論，就我個人來說，你媽對我的意義就我個人來說就我個人來說就我個人來說就我個人來說就Ssdsdsdsds我個人來說就我個人來');


INSERT INTO `job_detail`
(`id`,
`job_id`,
`content`,
`order`)
VALUES
(1,
1,
'myFirstJobDetail',
1);

INSERT INTO `job_detail`
(`id`,
`job_id`,
`content`,
`order`)
VALUES
(2,
2,
'test2JobDetail',
1);

INSERT INTO `job_detail`
(`id`,
`job_id`,
`content`,
`order`)
VALUES
(3,
2,
'test3JobDetail',
1);

INSERT INTO `review`
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


INSERT INTO `serve_city`
(`id`,
`city`,
`shop_email`)
VALUES
(1,
2,
'10846015@ntub.edu.tw');
