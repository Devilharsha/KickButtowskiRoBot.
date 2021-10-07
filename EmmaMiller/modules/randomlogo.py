#    Copyright (C) @Damantha126 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.



from bs4 import *
import shutil
import requests
import os
import base64
import sys
import random
import requests
from pyrogram import filters
from EmmaMiller import pbot
from EmmaMiller.function.pluginhelpers import get_text, admins_only

def download_images(images): 
    count = 0
    print(f"Total {len(images)} Image Found!") 
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"] 
            except: 
                try: 
                    image_link = image["data-src"] 
                except:
                    try:
                        image_link = image["data-fallback-src"] 
                    except:
                        try:
                            image_link = image["src"] 
                        except: 

                            pass
            try: 
                r = requests.get(image_link).content 
                try:

                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open("logo.jpg", "wb+") as f: 
                        f.write(r)
                    count += 1
            except: 
                pass


def mainne(name, typeo):
    url = f"https://www.brandcrowd.com/maker/logos?text={name}&searchtext={typeo}&searchService="
    r = requests.get(url) 
    soup = BeautifulSoup(r.text, 'html.parser') 
    images = soup.findAll('img') 
    random.shuffle(images)
    if images is not None:
       print("level 1 pass")
    download_images(images)



@pbot.on_message(filters.command("rlogo") & ~filters.edited & ~filters.bot)
@admins_only
async def logogen(client, message):
    pablo = await client.send_message(message.chat.id,"`Creating The Logo.....`")
    Godzilla = get_text(message)
    if not Godzilla:
        await pablo.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return
    lmao = Godzilla.split(":", 1)
    try:
        typeo = lmao[1]
    except BaseException:
        typeo = "name"
        await pablo.edit(
             "Give name and type for logo Idiot. like `/rlogo rose`")
    name = lmao[0]
    mainne(name, typeo)
    caption = "<b>Logo Generated By  @szrosebot.<b>"
    pate = "logo.jpg"
    await client.send_photo(message.chat.id, pate)
    try:
        os.remove(pate)
    except:
        pass
    await pablo.delete()
