from fastapi import FastAPI, Body, BackgroundTasks
from fastapi_utils.tasks import repeat_every
from typing import Optional
from fastapi import FastAPI
import sms
from datetime import datetime


app = FastAPI()

@app.get("/")
async def read_item():
    return {"Bio": "This is under develpment by AbbaTanim"}

@app.post("/bot/", status_code=200)
async def bot_post(data=Body(...)):
    if "text" in data['message']:
        name=data['message']['from']['first_name']
        message=data['message']['text']
        if "/help" in message:
            tid=data['message']['from']['id']
            msg="Hi! "+name.upper() +", I am being prepared by AbbaTanim, Thank you for your cooporation and patients command list will update shortly, exp: /who, /makecomplain etc 🙏 ☆☆☆"
            sms.send_telegram(msg,tid)
        
        print(name)
        print(message)
    else:
        print("Currently Im not working with image or file")
    return {"ok": 200}


@app.get("/bot/")
async def bot_get():
    return {"Bio": "Bot is under develpment by AbbaTanim"}


#https://api.telegram.org/bot1755770302:AAGeys1rIM-Z0BuQswdAhh5_kubCXjcCBWc/setWebhook?url=https://6b9cbffde5b4.ngrok.io/bot/
#https://api.telegram.org/bot1755770302:AAGeys1rIM-Z0BuQswdAhh5_kubCXjcCBWc/getFile?file_id=AgACAgQAAxkBAANhYJROJhPN-YoTSzlSR3lSIK6ONhQAAi24MRs3xqlQr0lHyDSiqWQNn9cnXQADAQADAgADeQADn_sGAAEfBA
#http://api.telegram.org/file/bot1755770302:AAGeys1rIM-Z0BuQswdAhh5_kubCXjcCBWc/photos/file_0.jpg
@app.on_event("startup")
@repeat_every(seconds=50)  # 1 hour
async def reminder()-> None:
    print("Interval...")
    now = datetime.utcnow()
    current_time = now.strftime("%H:%M:%S")
    current_hours=int(current_time.split(":")[0])
    if current_hours==19:
        sms.task()
    else:
        print("nothing to do")