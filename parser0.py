import telebot
import config
from time import sleep
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands = ['start'])
def start(message):

    html = requests.get("https://www.rbc.ru/short_news")
    soup = BeautifulSoup(html.text, 'lxml')
    title = soup.find('span', class_ = 'item__title-wrap')
    href = soup.find('div', class_ = 'item__wrap l-col-center')

    while html.status_code == 200:

        for t in title.find_all('span', class_ = 'item__title rm-cm-item-text')[:1]:

            answer_title = t.text.strip()
            print(answer_title)

        for h in href.find_all('a', class_ = 'item__link')[:1]:

            answer_href = h.get('href')
            print(answer_href)

            bot.send_message(message.chat.id, f'{answer_title}\n\n{answer_href}')

            sleep(5)

if __name__ == '__main__':
    bot.polling(none_stop = True)