# By Alexmarpar
# https://github.com/Alexmarpar/

import requests
from bs4 import BeautifulSoup as bt
import os 

url = 'https://store.steampowered.com/search/?maxprice=free&supportedlang=english&specials=1&ndl=1'
DISCORDWEBHOOK = os.environ.get('DISCORD_WEBHOOK')
request = requests.get(url)


def sendjson(gametittle,linkgame):
    data = {
        "content": f"Nuevo juego reclamable gratis en steam por tiempo limitado, es {gametittle} / link: {linkgame}",
    }
    requests.post(DISCORDWEBHOOK, json=data)


if request.status_code == 200:
    html = request.text
    soup = bt(html, 'lxml')
    searcher = soup.find('div',id='search_result_container')
    games = searcher.find_all('a',class_='search_result_row')

    for game in games:
        # game tittle:
        div_game_tittle = game.find('div', 'search_name ellipsis')
        game_tittle_span = div_game_tittle.find('span')
        game_tittle = game_tittle_span.get_text(strip=True)
        # link to buy
        link_buy = game.get('href')
        sendjson(game_tittle,link_buy)

else:
    print("Error, not status_code 200 detected")