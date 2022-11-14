import requests
from bs4 import BeautifulSoup
import discord
import asyncio

@client.event()
async def on_message(message):
    if message.content.startswith("!날씨"):
        try : 
            Name = message.content[4:len(message.content)]
            url = ("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="+Name + "+날씨")
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')

        #날씨 주워먹는 거
            #온도
            temperature =  soup.find('div', class_ = 'temperature_text')
            temresult = temperature.get_text()
            #날씨 상태
            weather = soup.find("span", {"class" : "weather before_slash"}).text
            #체감온도 구하기
            BodyTemperature = soup.find('dd', class_ = 'desc')
            Bodyresult = BodyTemperature.get_text()
            print("현재 온도 : " + temresult + "\n현재 날씨 : " + weather + "\n체감온도 : " + Bodyresult)
            embed = discord.Embed(title="", description="", color=0xB7F0B1)
            embed.set_author(name = Name +"의 날씨", url=url, icon_url="https://ssl.pstatic.net/sstatic/keypage/outside/scui/weather_new_new/img/logo_kma.png")
            embed.add_field(name="지역 이름 : " + Name, value= temresult , inline=False)
            embed.add_field(name="현재 날씨 상태 : " + weather ,value = '체감온도 ' + Bodyresult, inline= False)
            embed.set_footer(text='날씨 출처 : 기상청')
            embed.set_thumbnail(url="https://ssl.pstatic.net/sstatic/keypage/outside/scui/weather_new_new/img/logo_kma.png")
            await message.reply(embed=embed)
        
        except :
            await message.reply("해당 지역의 날씨를 찾을 수 없어요")