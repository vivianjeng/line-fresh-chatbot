import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom, BaseSize, ImagemapArea,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction, URIImagemapAction,
    PostbackTemplateAction, DatetimePickerTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageSendMessage, ImageMessage, VideoMessage, AudioMessage, FileMessage, ImagemapSendMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('TJpkyAGnxyWf7eFcAL7+egcX1VroELC04ikPM3hOU7txBqQhbx/gZGSRRh8zBwCcPnt6xW29ayvek4y4c/tf/aolwFB6qaw0hLGrU/keBNZOCHkuPahVEmxsEKy/GENEg1Jfgag5qqNcdV0ChpeMhgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('3095660aba36a6922da86ea27d46e27e')
# Heroku App Name
appName = 'linepythonbot'

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text =  event.message.text
    # message = TextSendMessage(text=event.message.text)
    if text.find("自我介紹") != -1:
        selfIntroduction(event.reply_token)
    elif text.find("個性") != -1:
        personality(event.reply_token)
    elif text.find("工作經歷") != -1:
        workExperience(event.reply_token)
    elif text.find("助教") != -1:
        TA(event.reply_token)
    elif text.find("壹傳實習") != -1:
        etrovision(event.reply_token)
    elif text.find("臺大演講網") != -1:
        speech(event.reply_token)
    elif text.find("學業") != -1:
        education(event.reply_token)
    elif text.find("程式作品") != -1:
        collections(event.reply_token)
    elif text.find("美術作品") != -1:
        art(event.reply_token)
    elif text.find("Yes!") != -1:
        transcript(event.reply_token)
    elif text.find("No!") != -1:
        pass
    else:
        default(event.reply_token)



# customize function
def selfIntroduction(reply_token):
    message1 = TextMessage(text="你好，我叫鄭雅文，目前就讀台大資訊工程研究所，請多多指教。")
    image_url1 = createUri('/static/pics/ya-wen.png')
    image1 = ImageSendMessage(original_content_url=image_url1,preview_image_url=image_url1)
    sticker1 = StickerSendMessage(
        package_id='3',
        sticker_id='217')
    
    line_bot_api.reply_message(
        reply_token,
        [message1,
        image1,
        sticker1])

def personality(reply_token):
    image_url1 = createUri('/static/pics/activity1.jpg')
    image_url2 = createUri('/static/pics/activity.JPG')
    image_url3 = createUri('/static/pics/activity3.jpg')
    message1 = TextSendMessage(text="我的個性樂觀、與人為善，總是可以帶給周遭的人歡樂，也會積極參與社交活動，像是系學會等")
    message2 = TextSendMessage(text="做事認真負責，以往工作過的地方老闆都給予正面的評價")
    message3 = TextSendMessage(text="喜歡運動，從大學到現在都有參加系女籃，維持一個禮拜兩次的運動頻率")
    image1 = ImageSendMessage(original_content_url=image_url1,preview_image_url=image_url1)
    image2 = ImageSendMessage(original_content_url=image_url2,preview_image_url=image_url2)
    image3 = ImageSendMessage(original_content_url=image_url3,preview_image_url=image_url3)
    
    line_bot_api.reply_message(
        reply_token,
        [message1,message2,image2,message3,image3])

def workExperience(reply_token):
    image_url1 = createUri('/static/pics/work.png')
    buttons_template = ButtonsTemplate(
        title='工作經歷', text='「資料科學與社會研究」助教\n壹傳科技股份有限公司實習生\n臺大演講網工讀生\n如果對哪一項工作有興趣的話歡迎選擇下方按鍵：',
        thumbnail_image_url = image_url1, 
        actions=[
            MessageTemplateAction(label='「助教」', text='助教'),
            MessageTemplateAction(label='「壹傳實習」', text='壹傳實習'),
            MessageTemplateAction(label='「臺大演講網」', text='臺大演講網')
        ])
    template_message = TemplateSendMessage(
        alt_text='工作經歷', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, template_message)

def TA(reply_token):
    image_url1 = createUri('/static/pics/TA.jpg')
    buttons_template = ButtonsTemplate(
        title='「資料科學與社會研究」助教', text='課程包含實作R語言及web crawling\n助教在這門課中負責回答同學們程式、作業的問題，以及批改作業。',
        thumbnail_image_url = image_url1, 
        actions=[
            URITemplateAction(
                label='觀看課程網站', uri='https://paper.dropbox.com/doc/DSSI1061-lLG99DNybar4Niv37RExw#:h2=DSSI1061'),
            MessageTemplateAction(label='繼續觀看「壹傳實習」', text='壹傳實習'),
            MessageTemplateAction(label='繼續觀看「臺大演講網」', text='臺大演講網')
        ])
    template_message = TemplateSendMessage(
        alt_text='助教', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, template_message)

def etrovision(reply_token):
    image_url1 = createUri('/static/pics/blog.jpg')
    buttons_template = ButtonsTemplate(
        title='「壹傳科技」實習生', text='停車場做智慧尋車的工程，從HTML、CSS、JavaScript到後來可以用Visual Studio開發一個全端的網站',
        thumbnail_image_url = image_url1, 
        actions=[
            URITemplateAction(
                label='參考我的部落格', uri='https://vivianjengsite.wordpress.com/'),
            MessageTemplateAction(label='繼續觀看「助教」', text='助教'),
            MessageTemplateAction(label='繼續觀看「臺大演講網」', text='臺大演講網')
        ])
    template_message = TemplateSendMessage(
        alt_text='壹傳實習', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, template_message)

def speech(reply_token):
    image_url1 = createUri('/static/pics/speech1.jpg')
    image_url2 = createUri('/static/pics/speech2.jpg')
    image_url3 = createUri('/static/pics/speech3.jpg')
    message1 = TextSendMessage(text="學會使用相機、腳架等攝影器材之外，也學會使用Adobe Premiere。\n以下是推薦的演講：")
    
    image_carousel_template = ImageCarouselTemplate(columns=[
            ImageCarouselColumn(image_url=image_url1,
                                action=URITemplateAction(label="拒絕小確幸，開創大格局",uri="https://speech.ntu.edu.tw/ntuspeech/Video/id-1724")),
            ImageCarouselColumn(image_url=image_url2,
                                action=URITemplateAction(label="葉丙成-台大畢業典禮演講",uri="https://speech.ntu.edu.tw/ntuspeech/Video/id-2044")),
            ImageCarouselColumn(image_url=image_url3,
                                action=URITemplateAction(label="從科學觀點了解人類行為",uri="https://speech.ntu.edu.tw/ntuspeech/Video/id-1837"))
        ])
    template_message1 = TemplateSendMessage(
        alt_text='臺大演講網', template=image_carousel_template)
    
    buttons_template = ButtonsTemplate(
        title='繼續觀看其他項目', text='請選擇以下按鈕',
        actions=[
            MessageTemplateAction(label='繼續觀看「助教」', text='助教'),
            MessageTemplateAction(label='繼續觀看「壹傳實習」', text='壹傳實習')
        ])
    template_message2 = TemplateSendMessage(
        alt_text='繼續觀看', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, [message1,template_message1,template_message2])


def collections(reply_token):
    image_url1 = createUri('/static/pics/github2.png')
    image_url2 = createUri('/static/pics/game1.png')
    image_url3 = createUri('/static/pics/game2.png')
    image_url4 = createUri('/static/pics/youtube.png')
    carousel_template = CarouselTemplate(columns=[
        CarouselColumn(text='My Github repository', title='Github',thumbnail_image_url=image_url1, 
            actions=[
                URITemplateAction(
                    label='Go to my github', uri='https://github.com/vivianjeng')
        ]),
        CarouselColumn(text='2D maple story game', title='UNITY GAME',thumbnail_image_url=image_url2, 
            actions=[
                URITemplateAction(
                    label='Go to demo video', uri='https://youtu.be/YbrYrtQ4abM')
        ]),
        CarouselColumn(text='3D kart racing game', title='UNITY GAME',thumbnail_image_url=image_url3,
            actions=[
                URITemplateAction(
                    label='Go to demo video', uri='https://youtu.be/Bhj-r0bRPZg')
        ]),
        CarouselColumn(text='My Youtube Channel', title='Youtube',thumbnail_image_url=image_url4, 
            actions=[
                URITemplateAction(
                    label='Go to youtube', uri='https://www.youtube.com/channel/UC0BvlI2ZTnxguTXdd7IvkiQ')
        ])
    ])
    template_message = TemplateSendMessage(
        alt_text='程式作品', template=carousel_template)
    
    line_bot_api.reply_message(reply_token, template_message)

def art(reply_token):
    image_url1 = createUri('/static/pics/AI1.jpg')
    image_url2 = createUri('/static/pics/PI1.jpg')
    image_url3 = createUri('/static/pics/PI2.png')
    image_url4 = createUri('/static/pics/PS2.jpg')
    image_url5 = createUri('/static/pics/PS2-1.png')
    image_url6 = createUri('/static/pics/PS3.jpg')
    image_url7 = createUri('/static/pics/PS3-1.jpg')
    image_url8 = createUri('/static/pics/PS5.jpg')
    image_url9 = createUri('/static/pics/PS5-1.png')
    
    imagemap_message1 = ImagemapSendMessage(
        base_url=createUri('/static/pics/imagemap'),
        alt_text='繪畫作品',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            URIImagemapAction(
                link_uri=image_url1,
                area=ImagemapArea(
                    x=0, y=0, width=520, height=520
                )
            ),
            URIImagemapAction(
                link_uri=image_url2,
                area=ImagemapArea(
                    x=520, y=0, width=520, height=520
                )
            ),
            URIImagemapAction(
                link_uri=image_url3,
                area=ImagemapArea(
                    x=0, y=520, width=1040, height=520
                )
            )
        ]
    )

    imagemap_message2 = ImagemapSendMessage(
        base_url=createUri('/static/pics/imagemap2'),
        alt_text='修圖作品',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            URIImagemapAction(
                link_uri=image_url4,
                area=ImagemapArea(
                    x=0, y=0, width=475, height=325
                )
            ),
            URIImagemapAction(
                link_uri=image_url5,
                area=ImagemapArea(
                    x=565, y=0, width=475, height=325
                )
            ),
            URIImagemapAction(
                link_uri=image_url6,
                area=ImagemapArea(
                    x=0, y=325, width=475, height=325
                )
            ),
            URIImagemapAction(
                link_uri=image_url7,
                area=ImagemapArea(
                    x=565, y=325, width=475, height=325
                )
            ),
            URIImagemapAction(
                link_uri=image_url8,
                area=ImagemapArea(
                    x=0, y=650, width=475, height=390
                )
            ),
            URIImagemapAction(
                link_uri=image_url9,
                area=ImagemapArea(
                    x=565, y=650, width=475, height=390
                )
            )
        ]
    )
    
    line_bot_api.reply_message(reply_token, [imagemap_message1, imagemap_message2])


def education(reply_token):
    message1 = TextSendMessage(text="在大學時期，我修習了許多資訊工程的核心課程，如「資料結構與演算法、演算法設計與分析、作業系統、計算機結構、線性代數」等，在這些課程中我學習了基礎的程式設計的觀念與作業實作。\n"+
                                    "之後也在學校的「CS+X」課程中學習應用方面的網頁相關語言HTML、CSS、JavaScript及遊戲設計使用Unity和資料庫使用MongoDB。")
    message2 = TextSendMessage(text="在當研究生的這段期間，除了跟指導老師吳家麟做區塊鏈方面的研究外，我還修習了電機系李宏毅的「機器學習」及資工系林軒田的「機器學習基石」課程\n"+
                                    "在李宏毅的機器學習課程中我學到用keras實作DNN、CNN、RNN等Deep learning的技術，也用python實作word embedding、t-SNE、auto-encoder、K-means等處理資料的方式。\n"+
                                    "在林軒田的機器學習基石的課程中則是透過數學證明，為機器學習背後的數學理論打下基礎。")
    message3 = TextSendMessage(text="在課餘時會跟著教授參與金融科技、區塊鏈等的研討會，也定期追蹤R-ladies Taipei的社團動態\n"+
                                    "聽前輩分享研究成果或是現在的趨勢，除了可以對未來研究方向有幫助之外，也讓自己隨時與世界接軌，充實自己。")

    confirm_template = ConfirmTemplate(text='是否需要附上成績單？', actions=[
        MessageTemplateAction(label='Yes', text='Yes!'),
        MessageTemplateAction(label='No', text='No!'),
    ])
    template_message = TemplateSendMessage(
        alt_text='學業', template=confirm_template)
    
    line_bot_api.reply_message(reply_token, [message1, message2, message3, template_message])


def transcript(reply_token):
    image_url1 = createUri('/static/pics/transcript1.jpg')
    image_url2 = createUri('/static/pics/transcript2.jpg')
    image1 = ImageSendMessage(original_content_url=image_url1,preview_image_url=image_url1)
    image2 = ImageSendMessage(original_content_url=image_url2,preview_image_url=image_url2)

    line_bot_api.reply_message(
        reply_token,
        [image1,image2])

def default(reply_token):
    message1 = TextMessage(text="抱歉現在還無法回答這個問題\n"+
                                "您可以下的指令有：\n"+
                                "「自我介紹」：認識雅文的第一步\n"+
                                "「個性」：好奇雅文內心是怎麼樣的人嗎\n"+
                                "「工作經歷」：雅文認真的時候\n"+
                                "「學業」：我也是會念書的\n"+
                                "「程式作品」、「美術作品」：雅文的心血結晶\n"+
                                "還有更多指令藏在上面的指令裡喔！")
    sticker1 = StickerSendMessage(
        package_id='3',
        sticker_id='217')
    
    line_bot_api.reply_message(
        reply_token,
        [message1,
        sticker1])

def createUri(pathName):
    return 'https://'+appName+'.herokuapp.com'+pathName
    

@handler.add(FollowEvent)
def handle_follow(event):
    if isinstance(event.source, SourceUser):
        profile = line_bot_api.get_profile(event.source.user_id)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='嗨' + profile.display_name+ '，歡迎多認識鄭雅文 Ya-wen,Jeng！\n'+
                                                                                 "您可以下的指令有：\n"+
                                                                                 "「自我介紹」：認識雅文的第一步\n"+
                                                                                 "「個性」：好奇雅文內心是怎麼樣的人嗎\n"+
                                                                                 "「工作經歷」：雅文認真的時候\n"+
                                                                                 "「學業」：我也是會念書的\n"+
                                                                                 "「程式作品」、「美術作品」：雅文的心血結晶\n"+
                                                                                 "還有更多指令藏在上面的指令裡喔！"))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
