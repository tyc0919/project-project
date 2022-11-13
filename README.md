# 企劃管理系統
## 工作連結
- [USE CASE](https://online.visual-paradigm.com/share.jsp?id=313330363836372d39)
- [FDD功能分解圖](https://app.diagrams.net/#G1GKiTAp0DL5JkGzfQlaD6uhWOmos8Pfeu)
- [資料表](https://online.visual-paradigm.com/share.jsp?id=313331303432302d36)
## 活動圖
1. [登入](https://online.visual-paradigm.com/share.jsp?id=313235323933372d32)
2. [註冊](https://online.visual-paradigm.com/share.jsp?id=313235323933372d31)
3. [企劃](https://online.visual-paradigm.com/share.jsp?id=313235323933372d35)
4. [新增工作](https://online.visual-paradigm.com/share.jsp?id=313235323933372d36)
5. [新增細項](https://user-images.githubusercontent.com/96291468/201528519-4324d7a0-68a6-45d2-b856-cec87d1c2298.jpg)
6. [修改預算](https://user-images.githubusercontent.com/96291468/201528596-7adec646-e360-4f8b-8324-6147baaaf65b.jpg)
7. [上傳花銷](https://user-images.githubusercontent.com/96291468/201528607-1433c433-e026-497c-a34b-d2750a7b7fa6.jpg)
8. [發表貼文](https://online.visual-paradigm.com/share.jsp?id=313939343439322d33)
9. [瀏覽貼文](https://online.visual-paradigm.com/share.jsp?id=313330363836372d3133)
10. [編輯個人資料](https://online.visual-paradigm.com/share.jsp?id=313937373334352d32)
## 循序圖
1. [登入](https://online.visual-paradigm.com/share.jsp?id=313939343439322d34)
2. [註冊](https://online.visual-paradigm.com/share.jsp?id=323030303137392d31)
3. [查看、編輯個人資料](https://online.visual-paradigm.com/share.jsp?id=323030303137392d32)
4. [瀏覽、評論貼文](https://online.visual-paradigm.com/share.jsp?id=323030303137392d33)
5. [引用合作店家](https://online.visual-paradigm.com/share.jsp?id=323030313636372d32)
6. [新增企劃](https://online.visual-paradigm.com/share.jsp?id=323030313636372d31)
7. [編輯工作](https://online.visual-paradigm.com/share.jsp?id=313331303432302d37)
8. [發表貼文](https://online.visual-paradigm.com/share.jsp?id=313331303432302d39)
## 類別圖
- [分析類別圖](https://online.visual-paradigm.com/share.jsp?id=313937373334352d34)
## 部屬圖
- [佈署圖](https://user-images.githubusercontent.com/96291468/201528775-992c023f-5f89-4029-9e71-6a494e3e198c.jpg)
## 元件圖
- [元件圖](https://user-images.githubusercontent.com/96291468/201528800-d103acaf-e004-4cba-b83d-692d7ec0c963.jpg)
## 套件圖
- [套件圖](https://user-images.githubusercontent.com/96291468/201528820-87b482cd-5a8c-49f8-9c7c-afe7dffd8167.jpg)
## 狀態圖
1. [登入狀態圖](https://user-images.githubusercontent.com/96291468/201528837-c8a0c172-f535-45e5-87ff-f84d577375be.jpg)
2. [註冊狀態圖](https://user-images.githubusercontent.com/96291468/201528846-3def2cc1-d908-4c5b-8668-44b57b18c63d.jpg)
3. [加入活動狀態圖](https://user-images.githubusercontent.com/96291468/201529013-4dd8eb47-9e4c-492b-bf04-e7e524d969ff.jpg)
4. [新增活動狀態圖](https://user-images.githubusercontent.com/96291468/201528850-d05e7476-cf99-44bb-a6fe-9040ffae51b2.jpg)
5. [新增工作狀態圖](https://user-images.githubusercontent.com/96291468/201528968-81e9177d-6076-4209-9ef8-583e9642d285.jpg)
6. [新增細項狀態圖](https://user-images.githubusercontent.com/96291468/201528973-f8d71021-cb0c-4570-86db-a7bf2e61d09b.jpg)
7. [上傳檔案狀態圖](https://user-images.githubusercontent.com/96291468/201528981-b6fab571-d7fa-44ab-908f-8e765f339747.jpg)
8. [更改預算狀態圖](https://user-images.githubusercontent.com/96291468/201529033-c8c8882e-7338-4630-aec3-0a2e06c61841.jpg)

## 系統建置教學
1. 安裝Mysql並建置名稱為"111401_project"的Schema
2. 在Mysql Workbench裡面執行DB資料夾下的腳本(new_create先，再換new_test_data)
3. 去Django資料夾下建置Python虛擬環境並且安裝requirement.txt裡面的套件
4. 在虛擬環境下的Django資料夾裡面打python manage.py makemigrations
5. 再打python manage.py migrate
6. 若沒有問題，可以打python manage.py runserver啟動伺服器，確認無異常就可以開始使用
