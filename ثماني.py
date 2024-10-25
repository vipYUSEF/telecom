import os , random , aiohttp , asyncio , datetime , telethon
from telethon import TelegramClient, functions, events
from base64 import b64decode
from user_agent import generate_user_agent
import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')

unique_words = set()
def us():    
    for synset in wn.all_synsets():
        for lemma in synset.lemmas():
            word = lemma.name().replace('_', ' ')
            
            if word not in unique_words:
                unique_words.add(word)
                
                return word
                
a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopassdfghjklzxcvbnm1234567890"

trys = 0

banned = set()

if os.path.exists("banned.txt"):
    with open("banned.txt", "r") as file:
        banned.update(file.read().splitlines())

async def check_user(session, username):
    headers = {
    'User-Agent': generate_user_agent(),
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'cache-control': "max-age=0",
    'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
    'sec-ch-ua-mobile': "?1",
    'sec-ch-ua-platform': "\"Android\"",
    'upgrade-insecure-requests': "1",
    'sec-fetch-site': "none",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'sec-fetch-dest': "document",
    'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    'Cookie': "stel_ssid=f2bea1d7b795e11a7e_4851103426933082246; stel_dt=-180"
}
    try:
        async with session.get(f"https://fragment.com/username/{username}",headers=headers) as response:
            text = await response.text()
            if '<span class="tm-section-header-status tm-status-taken">Taken</span>' in text:
                print(f"Taken username: {username}")
                return False
            elif '<span class="tm-section-header-status tm-status-unavail">Sold</span>' in text or '<span class="tm-section-header-status tm-status-avail">On auction</span>' in text:
                banned.add(username)
                with open("banned.txt", "a") as file:
                    file.write(username + "\n")
                print(f"NFT  username: {username}")
                return False
            elif '<div class="table-cell-status-thin thin-only tm-status-unavail">Unavailable</div>' in text:
                return True
            else:
                return False
    except Exception as e:
        print(e)
        return False

def gen_user(choice):
    if choice == "1":  # ثلاثي
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)
    elif choice == "2": # سداسي
        c = random.choices(a)
        d = random.choices(b)
        
        k1 = [c[0], c[0], c[0], c[0], c[0], d[0]]
        k2 = [d[0], c[0], c[0], c[0], c[0], c[0]]
        k3 = [c[0], d[0], c[0], c[0], c[0], c[0]]
        k4 = [c[0], c[0], d[0], c[0], c[0], c[0]]
        k5 = [c[0], c[0], c[0], d[0], c[0], c[0]]
        k6 = [c[0], c[0], c[0], c[0], d[0], c[0]]
        username = random.choice([k1,k2,k3,k4,k5,k6])
        username = "".join(username)
        
    elif choice == "3": # سداسي حرفين
        k = random.choices(a)
        n = random.choices(b)
        
        k1 = [k[0], k[0], k[0], k[0], n[0], k[0]]
        k2 = [k[0], k[0], n[0], n[0], k[0], k[0]]
        k3 = [k[0], n[0], k[0], k[0], n[0], k[0]]
        k4 = [k[0], k[0], n[0], k[0], k[0], n[0]]
        k5 = [k[0], n[0], k[0], n[0], k[0], k[0]]
        
        username = random.choice([k1,k2,k3,k4,k5])
        username = "".join(username)

    elif choice == "4": # بوتات ثلاثي
        c = random.choices(e)
        d = random.choices(a)
        s = random.choices(e)
        f = [d[0], c[0], s[0]]
        username = "".join(f)
        username = username + "bot"
    elif choice == "5": # خماسي مال فقرة
        k = random.choices(a)
        c = random.choices(e)
        n = random.choices(e)
        z = random.choices(e)
        g = random.choices(a)
        
        k1 = [k[0], c[0], n[0], n[0], n[0]]
        k2 = [k[0], c[0], z[0], z[0], z[0]]
        k3 = [k[0], k[0], k[0], n[0], c[0]]
        k4 = [k[0], z[0], z[0], z[0], g[0]]
        k5 = [k[0], n[0], n[0], n[0], c[0]]
        username = random.choice([k1,k2,k3,k4,k5])
        username = "".join(username)
    elif choice == "6": #سداسي نهاية ارقام
        k = random.choices(a)
        c = random.choices(e)
        n = random.choices(b)               
        username = k + c + n + n + n + n
        username = "".join(username)
        
    elif choice == "7": # سباعي حرفين
        k = random.choices(a)
        n = random.choices(e)
        
        k1 = [k[0], k[0], k[0], k[0], n[0], k[0], k[0]]
        k2 = [k[0], k[0], n[0], n[0], k[0], k[0], k[0]]
        k3 = [k[0], n[0], k[0], k[0], n[0], k[0], k[0]]
        k4 = [k[0], k[0], n[0], k[0], k[0], n[0], k[0]]
        k5 = [k[0], n[0], k[0], n[0], k[0], k[0], k[0]]
        
        username = random.choice([k1,k2,k3,k4,k5])
        username = "".join(username)
    
    elif choice == "8": # ثماني حرف
        c = random.choices(a)
        d = random.choices(e)
        
        k1 = [c[0], c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        k2 = [d[0], c[0], c[0], c[0], c[0], c[0], c[0], c[0]]
        k3 = [c[0], d[0], c[0], c[0], c[0], c[0], c[0], c[0]]
        k4 = [c[0], c[0], d[0], c[0], c[0], c[0], c[0], c[0]]
        k5 = [c[0], c[0], c[0], d[0], c[0], c[0], c[0], c[0]]
        k6 = [c[0], c[0], c[0], c[0], d[0], c[0], c[0], c[0]]
        username = random.choice([k1,k2,k3,k4,k5,k6])
        username = "".join(username)
    elif choice == "9": # id888
        c = random.choices(b)
        d = random.choices(b)
        s = random.choices(b)
        f = [d[0], c[0] , s[0]]
        username = "".join(f)  
        username = "id" + username
    
    elif choice == "10": # aab_b
        pattern = random.choice(['xxxxxxxxa', 'abmmm', 'ab3333', 'aa7aa7', 'aabaab', 'aaabab','aaaaaaab','aaaaaaba','aaaaabaa','aaaabaaa','aaabaaaa','aabaaaaa','abaaaaaa','baaaaaaa','qqqba','ayyyb'])   
        c = random.choice(a)
        d = random.choice(e)            
        username = pattern.replace('a', c).replace('b', d)
    
    elif choice == "11": #تيست
        k = random.choices(a)
        c = random.choices(e)
        n = random.choices(b)               
        username = k + c + n + n + n + n + c + n
    elif choice == "12":
        letters = 'abcdefghijklmnopqrstuvwxyz'
        pair = random.sample([ch for ch in letters if ch != 'x'], 2)
        positions = ['x', 'x', 'x']
        index = random.randint(0, 3)
        positions.insert(index, ''.join(pair))
        username = ''.join(positions)
               
    elif choice == "m":
        username = us()
        
    if username in banned:
        return gen_user(choice)
    
    return username

async def hunterusername(app, event, choice):
    global trys
    async with aiohttp.ClientSession() as session:
        await event.reply("يتم الصيد")
        trys = 0
        try:
            ch = await app(
                functions.channels.CreateChannelRequest(
                    title="ثروڤس | Throofs",
                    about=" Username for @ivvvivv ",
                )
            )
            ch = ch.updates[1].channel_id
        except Exception as e:
            print(e)
            return
        
        while True:
            trys += 1
            username = gen_user(choice)
            if await check_user(session, username):
                try:
                    await app(functions.channels.UpdateUsernameRequest(channel=ch, username=username))
                    
                    await asyncio.sleep(1)
                    
                    try:
                        print(True)
                        me = await app.get_me()
                        phone = me.phone
                        await app.send_file(
                            await app.get_entity(ch),
                            "https://t.me/DGGGDGG/4",
                            caption=f"""
⚊⚊⚊⚊⚊⚊⚊⚊⧎⚊⚊⚊⚊⚊⚊⚊⚊
-  User - @{username}
- Owner - @ivvvivv
⚊⚊⚊⚊⚊⚊⚊⚊⧎⚊⚊⚊⚊⚊⚊⚊⚊                    """,
                        )
                        await app.send_file(
                            "nnwnnnw",
                            "https://t.me/DGGGDGG/4",
                            caption=f"""
⚊⚊⚊⚊⚊⚊⚊⚊⧎⚊⚊⚊⚊⚊⚊⚊⚊
-  User - @{username}
⚊⚊⚊⚊⚊⚊⚊⚊⧎⚊⚊⚊⚊⚊⚊⚊⚊
- Owner - @ivvvivv
⚊⚊⚊⚊⚊⚊⚊⚊⧎⚊⚊⚊⚊⚊⚊⚊⚊
                            """,
                        )
                    except:
                            print(True)
                    break
                except telethon.errors.FloodWaitError as e:
                        hours = e.seconds // 3600
                        minutes = (e.seconds % 3600) // 60
                        seconds = (e.seconds % 3600) % 60
                        await app.send_message(
                            event.chat_id,
                            f"""
Erorr Flood : `{hours}:{minutes}:{seconds}` !
                            """,
                        )
                        await asyncio.sleep(e.seconds + 20)
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    print("banned username: " + username)
                    banned.add(username)
                    with open("banned.txt", "a") as file:
                        file.write(username + "\n")
                except Exception as eee:
                    if "(caused by UpdateUsernameRequest)" in str(eee):
                        pass
                    elif "the username is already" in str(eee):
                        pass
                    elif "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                        pass
                    else:
                        times = datetime.datetime.now().strftime("%I:%M:%S")
                        await app.send_message(
                            ch,f"""                         
Dont Try Again Im The Best ⚓
- - - - - - - - - - - - - - - - - - - - - - - - - 
彡 -  UserName: ❲ @{username} ❳
彡 -  ClickS: ❲ {trys} ❳
彡 - Save: ❲ Chaneel ❳
- - - - - - - - - - - - - - - - - - - - - - - - 
ThE Programmer ❲ @nnwnnnw  ❳
                            """
                        )
                    break              
#1
async def main():
    client = TelegramClient("+9647762452541", b64decode("MjUzMjQ1ODE=").decode(), b64decode("MDhmZWVlNWVlYjZmYzBmMzFkNWYyZDIzYmIyYzMxZDA=").decode())
    await client.start(phone="+9647762452541")
    await client.send_message('me',"""
**Choose the type of fishing - @ivvvivv**
⚊⚊⚊⚊⚊⚊⚊⚊⚊⧎⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊
**1 - ثلاثي**
**2 - سداسي حرف**
**3 - سداسي حرفين**
**4 - ثلاثي بوت**
**5 - خماسي الجديد**
**6 - غير مفضل**
**7 - سباعي حرفين**
**8- ثماني حرف**
**9 - نوع جديد**
**10 - رباعي**
**11 - تست بوت**
⚊⚊⚊⚊⚊⚊⚊⚊⚊⧎⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊
** لـ اختيار النوع اكتب Run واكتب رقم النوع**
    """)
    @client.on(events.NewMessage)
    async def handler(event):
        global trys
        message_text = event.raw_text.strip()
        
        if message_text.startswith("Run"):
            try:
                choice = message_text.split()[1]  
                await hunterusername(client, event, choice)
            except IndexError:
                await event.reply("Error choice.")
        elif "Clicks" in message_text:
            await event.edit(f"The number of attempts is: `{trys}`")
        elif "check" in message_text:
            async with aiohttp.ClientSession() as session:
                sent = await event.edit("Wait") 
                if await check_user(session, "BOB9212345BOBBOB111BOB"):
                    await sent.edit("True")
                else:
                    await sent.edit("Ban Fragment")
            
    await client.run_until_disconnected()
if __name__ == "__main__":
    asyncio.run(main())