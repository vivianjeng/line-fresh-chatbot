# Line Bot 安裝

使用 Python LINE Bot SDK 在 Heroku 上架設一個chatbot。

## 在開始之前

確保具有以下內容：

- 在 Line 的控制台為機器人創建了一個頻道 [#教學](https://developers.line.me/en/docs/messaging-api/getting-started/)
- 一個 [Heroku](https://www.heroku.com) 的帳戶（可以免費創建一個）

## 架設聊天機器人

按照以下步驟架設機器人。


1. 登入 Heroku 後，
  在 [Heroku](https://dashboard.heroku.com/apps) 頁面中，點選 New -> Create New App
  ![](https://i.imgur.com/MVrkUsn.png)
2. 輸入 App name ，然後點擊 Create app
  ![](https://i.imgur.com/k5Cn8SZ.png)
3. 下載此repository
``` shell=
$ git clone https://github.com/vivianjeng/line-fresh-chatbot
```
4. 進入 [Line 控制台](https://developers.line.me/console/)，[創建一個chatbot](https://developers.line.me/en/docs/messaging-api/getting-started/)
5. 取得 **channel secret** 和 **channel access token**，看[教學](https://developers.line.me/en/docs/messaging-api/building-sample-bot-with-heroku/)
6. 開啟資料夾內的 app.py，修改 **channel secret** 、 **channel access token** 和 **heroku app name**
  ![](https://i.imgur.com/Qj9r1nU.png)
7. 並使用 Heroku CLI 將程式部署到 Heroku 上面 （請參考 [使用 Heroku CLI](#使用-heroku-cli)）
8. 使用以下 URL 格式在控制台中輸入 webhook URL 
  `{HEROKU_APP_NAME}.herokuapp.com/callback`
  注意：{HEROKU_APP_NAME} 是步驟2中的應用程序名稱
9. 通過在控制台的 “Channel settings” 頁面上掃描 QR Code，將您的機器人添加到 LINE 的朋友中
10. 即可在 Line 上向您的機器人發送文字訊息

## 使用 Heroku CLI

1. 下載並安裝 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)、[Git](https://git-scm.com/)
2. 開啟範例程式碼資料夾，在路徑上輸入 cmd
3. 使用終端或命令行應用程序登錄到 Heroku
```shell＝
heroku login
```
4. 用 git 將資料夾與 heroku 連接
```shell＝
heroku git:remote -a {HEROKU_APP_NAME}
```
    注意：{HEROKU_APP_NAME} 是上述步驟2中的應用名稱
5. 將資料夾底下所有檔案加入 git 清單，如跳出錯誤訊息請重新執行
```shell
git add .
```
6. 儲存記錄點，如跳出錯誤訊息請詳讀
```shell
git commit -m "Init"
```
    注意："Init" 可使用任意文字替換，其為此紀錄點的敘述
7. 將在 git 清單中的檔案上傳到 heroku，請確認訊息是否顯示成功
```shell
git push heroku master
```
**每當需要更新 Bot 時，請重新執行 5、6、7 步驟**


## 檢查log
```
當成是遇到問題時，可查看log以找出錯誤
```
要查看您的機器人在 Heroku 的log，請按照以下步驟。

1. 如果沒登入，請先透過 Heroku CLI 登入
```shell
heroku login
```

2. 顯示 app log
```shell
heroku logs --tail --app {HEROKU_APP_NAME}
```
注意：{HEROKU_APP_NAME} 是上述步驟2中的應用名稱。
​    
    --tail    # 持續打印日誌
    --app {HEROKU_APP_NAME}    # 指定 App

## 程式解說
```
資料夾裡需含有兩份文件來讓你的程式能在 heroku 上運行
```
- Procfile：heroku 執行命令，web: {語言} {檔案}，這邊語言為 python，要自動執行的檔案為 app.py，因此我們改成 **web: python3 app.py**。
- requirements.txt：列出所有用到的套件，heroku 會依據這份文件來安裝需要套件

### app.py

如想更多了解此程式，可以去研究 
Python3、
[Flask 套件](http://docs.jinkan.org/docs/flask/)、
[Line bot sdk](https://github.com/line/line-bot-sdk-python)
[官方文件](https://github.com/line/line-bot-sdk-python#api)

