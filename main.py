import tgcrypto
from pyromod import listen
from pyrogram import Client, filters
import os
import sys
import asyncio
from pyrogram import *
import pyrogram
import random
import requests
from threading import Thread
from user_agent import generate_user_agent
import contextlib
from server import web_server
from aiohttp import web
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)
api_id = 18922496
api_hash = '371d1dc33eccaa19bb0814a27bb98f3c'
token = '5490492288:AAGLCMOVsmYJolrofALL79xB8is0GDdFKz0'  # vmwbot
token2 = '5695022956:AAHdCQRIE9aIQIjz1gm2FqT14V1v5ow0FnA'  # lj4bot
bot = Client("Bot", bot_token=token, api_hash=api_hash, api_id=api_id)
dev = 5307018300
stats = []
users = []


def delete_text(file_name, text_to_delete):
    with open(file_name, 'r') as f:
        old_text = f.read()
        old_text = old_text.split(":")
    with open(file_name, 'w') as f:
        new_text = ""
        old_text.remove(text_to_delete)
        new_text = ":".join(old_text)
        f.write(new_text)


def gen_user(choice):
    c = choice
    abc = "qwertyuiopasdfghjklzxcvbnm1234567890"
    abcc = "qwertyuiopasdfghjklzxcvbnm"
    if c == 1:
        l1 = random.choice(abcc)
        l2 = random.choice(abc)
        l3 = random.choice(abc)
        username = f"{l1}_{l2}_{l3}"
        #username = l1+l2+l2+l2+l3
        username = "".join(username)
        #username = "abdjuxiskdjd"
        return username
    elif c == 2:
        l1 = random.choice(abcc)
        l2 = random.choice(abc)
        l3 = random.choice(abc)
        username = [l1, l1, l1, l1, l2, l1]
        random.shuffle(username)
        username = "".join(username)
        return username
    elif c == 3:
        l1 = random.choice(abcc)
        l2 = random.choice(abc)
        l3 = random.choice(abc)
        username = [l1, l1, l1, l1, l2, l1]
        random.shuffle(username)
        username = "".join(username)
        return username
    elif c == 4:
        l1 = random.choice(abcc)
        l2 = random.choice(abc)
        l3 = random.choice(abc)
        username = [l1, l1, l1, l1, l2]
        random.shuffle(username)
        username = "".join(username)
        return username
    else:
        l1 = random.choice(abcc)
        l2 = random.choice(abc)
        l3 = random.choice(abc)
        username = f"{l1}_{l2}_{l3}"
        username = "".join(username)
        return username


async def check_user(sedthon, username):
    #print("With :", username)
    with open("banned.txt", "r") as f:
        text = f.read().split(":")
    if username in text:
        return False
    else:
        pass
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        await asyncio.sleep(2)
    else:
        return False
    try:
        res = await sedthon.invoke(pyrogram.raw.functions.account.CheckUsername(
            username=username))
        if res == True:
            print("Av : ", username)
            return True
        elif res == False:
            print("Un : ", username)
            return False
    except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
        with open("banned.txt", "a") as f:
            f.write(f"{username}:")
        return False
    except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
        with open("banned.txt", "a") as f:
            f.write(f"{username}:")
        return False

    except Exception as e:
        print(f"Error with @{username} , \n The error : {e}")
        await sedthon.send_message("me", f"Error with @{username} , \n The error : {e}")
        return e


async def main2(session, bot, msg, choice):
    try:
        client = Client("", session_string=session)
    except Exception as e:
        print(e)
        return
    await client.start()
    me = await client.get_me()
    stats.append(me.id)
    with open("prime.txt", "r") as f:
        prime = f.read().split(":")
    ch = await client.create_channel(title="Sedthon Source")
    ch = ch.id
    await client.send_message(ch, "@Sedthon | @Dar4k")
    for i in range(10000):

        username = gen_user(choice)
        if me.id in prime:
            await asyncio.sleep(0.2)
            res = await check_user(client, username)
            if res == True:
                try:
                    await client.set_chat_username(ch, username)
                    await client.send_message(
                        "me", f"تم صيد @{username} ! \n @Dar4k | @Sedthon")
                    await bot.send_message(msg.chat.id, f'Getted ! @{username}')
                    with open("hits.txt", "a") as f:
                        f.write(f"\n@{username}")
                except Exception as e:
                    print(f"Error with @{username} , \n The error : {e}")
                    await client.send_message(
                        "me", f"خطأ مع @{username} ، الخطأ : \n {e}")
                    break
            elif res == False:
                pass
            else:
                break
        else:
            await asyncio.sleep(1.2)
            try:
                await client.set_chat_username(ch, username)
                await client.send_message(
                    "me", f"تم صيد @{username} ! \n @Dar4k | @Sedthon")
                await bot.send_message(msg.chat.id, f'Getted ! @{username}')
                with open("hits.txt", "a") as f:
                    f.write(f"\n@{username}")
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                with open("banned.txt", "a") as f:
                    f.write(f"{username}:")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                with open("banned.txt", "a") as f:
                    f.write(f"{username}:")
            except Exception as e:
                if "The username is already in use by someone else" in e :
                    pass
                else :
                    print(f"Error with @{username} , \n The error : {e}")
                    await client.send_message(
                        "me", f"خطأ مع @{username} ، الخطأ : \n {e}")
                    break
    await client.send_message("me", "تم الانتهاء من الصيد .")
    stats.remove(me.id)
    await asyncio.sleep(1)
    try:
        await client.stop()
    except:
        sys.exit()


@bot.on_message(filters.command("start"))
async def start(bot, msg):
    await bot.send_message(msg.chat.id, "اهلا بك في البوت ! \n اختر امر من الاوامر ادناه .",
                           reply_markup=InlineKeyboardMarkup(
                               [
                                   [
                                       InlineKeyboardButton(
                                           "بدء الصيد",
                                           callback_data="checker"
                                       )
                                   ],
                                   [
                                       InlineKeyboardButton(
                                           "حذف الحسابات",
                                           callback_data="delete"
                                       ),
                                       InlineKeyboardButton(
                                           "اضافة حساب",
                                           callback_data="add"
                                       )
                                   ],
                                   [
                                       InlineKeyboardButton(
                                           text="المطور",
                                           url="t.me/Dar4k"
                                       )
                                   ]
                               ]
                           )
                           )


async def checker(bot, call):
    cid = call.message.chat.id
    user_id = call.from_user.id
    try:
        with open(f"{user_id}.txt", "r") as f:
            sessions = f.read().split(":")
    except:
        await bot.send_message(cid, "ليس لديك اي حساب ! .")
        return
    await bot.send_message(cid, "اختر من الانواع ادناه .",
                           reply_markup=InlineKeyboardMarkup(
                               [
                                   [
                                       InlineKeyboardButton(
                                           text="ثلاثي",
                                           callback_data="1"
                                       ),
                                       InlineKeyboardButton(
                                           text="سداسي",
                                           callback_data="2"
                                       )
                                   ],
                                   [
                                       InlineKeyboardButton(
                                           text="خماسي حرفين",
                                           callback_data="3"
                                       ),
                                       InlineKeyboardButton(
                                           text="خماسي",
                                           callback_data="4"
                                       )
                                   ],
                                   [
                                       InlineKeyboardButton(
                                           text="المطور",
                                           url="t.me/Dar4k"
                                       )
                                   ]
                               ]
                           )
                           )


@bot.on_callback_query()
async def answer(bot, call):
    data = call.data
    msg = call.message
    await call.message.delete()
    if data == 'checker':
        await checker(bot, call)
        return
    elif data == 'add':
        await add_acccounts(bot, call)
        return
    elif data == 'delete':
        await delete_accounts(bot, call)
        return
    if data == "1":
        choice = 1
    elif data == "2":
        choice = 2
    elif data == "3":
        choice = 3
    elif data == "4":
        choice = 4
    with open(f"{call.from_user.id}.txt", "r") as f:
        sessions = f.read().split(":")
    for i in sessions:
        if i == '':
            return
        try:
            sedthon = Client("", session_string=i)
            await sedthon.start()
            me = await sedthon.get_me()
            await bot.send_message(msg.chat.id, f"تم بدء الصيد في : {me.first_name}")
            await client.stop()
        except Exception as e:
            pass
        loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        th = Thread(target=asyncio.run, args=(main2(i, bot, msg, choice),))
        th.start()


async def restart(bot, msg):
    if msg.from_user.id == dev:
        await bot.send_message(msg.chat.id, "Ok")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        return


async def add_acccounts(bot, call):
    msg = call.message
    cid = msg.chat.id
    user_id = call.from_user.id
    if user_id in users:
        await bot.send_message(cid, "انت ضايف حساب قبل , لازم تحذفه")
        return
    else:
        pass
    with open("users.txt", 'r') as f:
        text = f.read().split(":")
        if str(user_id) in text or user_id == dev:
            pass
        else:
            await bot.send_message(cid, "للاسف انت مو مشترك بل بوت :(")
            return
    try:
        count = int((await bot.ask(cid, "ادخل عدد الحسابات لديك : ")).text)
        with open("prime.txt", "r") as f:
            text = f.read().split(":")
        if count >= 2 and str(user_id) not in text:
            await bot.send_message(
                cid, "للاسف الاشتراك الخاص بك لايسمح لك ب اضافة اكثر من حساب .")
            return
        else:
            pass
    except Exception as e:
        await bot.send_message(cid, "يرجى ادخال رقم ! ")
        return
    for i in range(int(count)):
        i += 1
        s = await bot.ask(cid, f"ادخل كود بايرو للحساب رقم ({i}) : ")
        with open(f"{user_id}.txt", "a") as f:
            f.write(f"{s.text}:")
    users.append(user_id)
    await bot.send_message(cid, "تم اضافة كل الحسابات .")


async def delete_accounts(bot, call):
    msg = call.message
    cid = msg.chat.id
    user_id = call.from_user.id
    try:
        import os
        os.remove(f"{user_id}.txt")
        users.remove(user_id)
        await bot.send_message(cid, "تم حذف جميع الحسابات لديك !")

    except:
        await bot.send_message(cid, "ليس لديك اي حساب ! .")


@bot.on_message(filters.command("status"))
async def status(bot, msg):
    if msg.from_user.id in stats:
        await bot.send_message(msg.chat.id, "الصيد يعمل في حسابك .")
    else:
        await bot.send_message(msg.chat.id, "الصيد لايعمل في حسابك")


@bot.on_message(filters.command("prime"))
async def add_prime(bot, msg):
    if msg.from_user.id == dev:
        try:
            id = msg.text.split()[1]
        except:
            await bot.send_message(msg.chat.id, "يرجى ادخال ايدي صالح !")
            return
        with open("prime.txt", "a") as f:
            f.write(f"{id}:")
        await bot.send_message(msg.chat.id, "تم اضافته الى قائمة ال(prime)")
    else:
        return


@bot.on_message(filters.command("user"))
async def add_user(bot, msg):
    if msg.from_user.id == dev:
        try:
            id = msg.text.split()[1]
        except:
            await bot.send_message(msg.chat.id, "يرجى ادخال ايدي صالح !")
            return
        with open("users.txt", "a") as f:
            f.write(f"{id}:")
        await bot.send_message(msg.chat.id, "تم اضافته الى قائمة ال(user)")
    else:
        return


@bot.on_message(filters.command("unprime"))
async def remove_prime(bot, msg):
    if msg.from_user.id == dev:
        try:
            id = msg.text.split()[1]
        except:
            await bot.send_message(msg.chat.id, "يرجى ادخال ايدي صالح !")
            return
        try:
            delete_text('prime.txt', f"{id}")
            await bot.send_message(msg.chat.id, "تم حذفه من قائمة ال(prime)")
        except:
            await bot.send_message(msg.chat.id, "العضو مو موجود بل قائمة")
    else:
        return


@bot.on_message(filters.command("unuser"))
async def remove_user(bot, msg):
    if msg.from_user.id == dev:
        try:
            id = msg.text.split()[1]
        except:
            await bot.send_message(msg.chat.id, "يرجى ادخال ايدي صالح !")
            return
        try:
            delete_text('users.txt', f"{id}")
            await bot.send_message(msg.chat.id, "تم حذفه من قائمة ال(user)")
        except:
            await bot.send_message(msg.chat.id, "العضو مو موجود بل قائمة")
    else:
        return


@bot.on_message(filters.command("del"))
async def remove_user(bot, msg):
    if msg.from_user.id == dev:
        try:
            id = msg.text.split()[1]
        except:
            await bot.send_message(msg.chat.id, "يرجى ادخال ايدي صالح !")
            return
        try:
            os.remove(f"{id}.txt")
        except:
            await bot.send_message(msg.chat.id, "العضو ماعنده حسابات")
    else:
        return


@bot.on_message(filters.command("files"))
async def remove_user(bot, msg):
    if msg.from_user.id == dev:
        file1 = open("users.txt", 'rb')
        file2 = open("prime.txt", 'rb')
        await bot.send_document(msg.chat.id, file1)
        await bot.send_document(msg.chat.id, file2)
    else:
        return


# RUN
PORT = os.environ.get("PORT", "8080")


async def server():
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()


bot.loop.run_until_complete(server())

if len(sys.argv) in {1, 3, 4}:
    with contextlib.suppress(ConnectionError):
        bot.run()
else:
    bot.disconnect()

# bot.run()
