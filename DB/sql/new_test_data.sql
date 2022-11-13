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
'公司職工團康活動籌備',
0,
0,
'這次活動圓滿成功，要感謝公司同仁的配合、各地贊助商的支持。',
now(),
now(),
'INVITINGCODE',
'6.jpg',
50000,'每年更邀請其他新竹地區的公司參與，達到拓展交友圈與聯誼互動之效。另外也於員工宿舍、廠內設置休閒中心，鼓勵同仁養成運動的習慣，並舉辦健康紓壓');

INSERT INTO `activity` VALUES
(2,
'test@gmail.com',
2,
'myActivity',
0,
0,
'這次活動圓滿成功，要感謝公司同仁的配合、各地贊助商的支持。',
now(),
now(),
'INVITINGCODE',
'6.jpg',
50000,'每年更邀請其他新竹地區的公司參與，達到拓展交友圈與聯誼互動之效。另外也於員工宿舍、廠內設置休閒中心，鼓勵同仁養成運動的習慣，並舉辦健康紓壓');

INSERT INTO `activity` VALUES
(3,
'test@gmail.com',
2,
'testActivity3',
0,
0,
'這次活動圓滿成功，要感謝公司同仁的配合、各地贊助商的支持。',
now(),
now(),
'INVITINGCODE',
'6.jpg',
50000,'每年更邀請其他新竹地區的公司參與，達到拓展交友圈與聯誼互動之效。另外也於員工宿舍、廠內設置休閒中心，鼓勵同仁養成運動的習慣，並舉辦健康紓壓');

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
'10846017@ntub.edu.tw');

INSERT INTO `collaborator`
(`activity_id`,
`user_email`)
VALUES
(2,
'test@gmail.com');

INSERT INTO `collaborator`
(`activity_id`,
`user_email`)
VALUES
(3,
'test@gmail.com');



INSERT INTO `job`
VALUES
(1,
1,
'10846017@ntub.edu.tw',
'前期準備',
2,
1,
now(),
date_add(now(), interval 1 month),
'包括活動企劃、策劃、宣傳、內容準備、找講者、找場地、準備茶水、準備設備、準備伴手禮等。',
500,0);



INSERT INTO `job`
VALUES
(2,
2,
'test@gmail.com',
'前期準備',
2,
1,
now(),
date_add(now(), interval 1 month),
'包括活動企劃、策劃、宣傳、內容準備、找講者、找場地、準備茶水、準備設備、準備伴手禮等。',
500,0);

INSERT INTO `job`
VALUES
(3,
2,
'test@gmail.com',
'活動執行',
2,
1,
now(),
date_add(now(), interval 1 month),
'桌椅準備、測試設備、活動指引、分發DM、演說內容、互動、變通等。'
,500,0);


INSERT INTO `job`
VALUES
(4,
3,
'test@gmail.com',
'後期研討',
2,
1,
now(),
date_add(now(), interval 1 month),
'收集資料、獲得反饋、再行銷等。',
500,0);

INSERT INTO `job`
VALUES
(5,
3,
'test@gmail.com',
'活動指引',
2,
1,
now(),
date_add(now(), interval 1 month),
'尋找並列出在每一個活動中需要哪些指引標示、說明書，以提醒各個活動的內容狀態',
500,0);

INSERT INTO`job`
VALUES
(6,
3,
'test@gmail.com',
'找場地',
2,
1,
now(),
date_add(now(), interval 1 month),
'可以容納所有員工的場地，需要一個高舞台來主持和表演',
500,0);


INSERT INTO `job_detail`
(`job_detail_id`,
`title`,
`content`,
`job_id`,
`activity_id`,
`status`)
VALUES
(1,
'找尋適合的物件',
'條件包括: 1. 容納500人 2. 需要提供高舞台',
6,
3,
0);

INSERT INTO `job_detail`
(`job_detail_id`,
`title`,
`content`,
`job_id`,
`activity_id`,
`status`)
VALUES
(2,
'保留聯絡人',
'保留各候選場地聯絡人的聯絡方式，以方便之後場地的比較與參考。',
6,
3,
0);

INSERT INTO `job_detail`
(`job_detail_id`,
`title`,
`content`,
`job_id`,
`activity_id`,
`status`)
VALUES
(3,
'場地活動指引牌',
'列出有使用場地的活動指引牌，並且測量大小，以及需要的材料',
2,
2,
0);

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
'請問這個活動的計畫有在公司官網上嗎?想要一些拍攝的照片作為參考。',
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

INSERT INTO `111401_project`.`file`
(`id`,
`job_id`,
`activity_id`,
`file_path`,
`file_uploaded_time`)
VALUES
(1,
1,
2,
'file.jpg',
now());




