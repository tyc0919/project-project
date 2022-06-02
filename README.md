# 企劃管理系統
## 工作連結
- [USE CASE](https://online.visual-paradigm.com/share.jsp?id=313330363836372d39)
- [FDD功能分解圖](https://app.diagrams.net/#G1GKiTAp0DL5JkGzfQlaD6uhWOmos8Pfeu)
- [資料表](https://online.visual-paradigm.com/share.jsp?id=313331303432302d36)
## 活動圖
1. [登入](https://online.visual-paradigm.com/share.jsp?id=313235323933372d32)
2. [註冊](https://online.visual-paradigm.com/share.jsp?id=313235323933372d31)
3. [企劃](https://online.visual-paradigm.com/share.jsp?id=313235323933372d35)
4. [編輯工作](https://online.visual-paradigm.com/share.jsp?id=313235323933372d36)
5. [邀請協作人員](https://online.visual-paradigm.com/share.jsp?id=313939343439322d31)
6. [引用合作店家](https://online.visual-paradigm.com/share.jsp?id=313939343439322d32)
7. [查看店家資料](https://online.visual-paradigm.com/share.jsp?id=313937373334352d31)
8. [發表貼文](https://online.visual-paradigm.com/share.jsp?id=313939343439322d33)
9. [瀏覽貼文](https://online.visual-paradigm.com/share.jsp?id=313330363836372d3133)
10. [編輯個人資料](https://online.visual-paradigm.com/share.jsp?id=313937373334352d32)
11. [編輯店家資料](https://online.visual-paradigm.com/share.jsp?id=313937373334352d33)
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
## 系統建置教學
1. 安裝Mysql並建置名稱為"111401_project"的Schema
2. 在Mysql Workbench裡面執行DB資料夾下的腳本(new_create先，再換new_test_data)
3. 去Django資料夾下建置Python虛擬環境並且安裝requirement.txt裡面的套件
4. 在虛擬環境下的Django資料夾裡面打python manage.py makemigrations
5. 再打python manage.py migrate
6. 若沒有問題，可以打python manage.py runserver啟動伺服器，確認無異常就可以開始使用
