import time

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from ads.models import Ad


class Command(BaseCommand):
    help = 'кастомная комманда для парсинга первых 10 объявлений с Farpost'

    def handle(self, *args, **kwargs):
        url = 'https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        ads_table = soup.find('table', class_='viewdirBulletinTable')
        if not ads_table:
            self.stdout.write(self.style.ERROR('No ads table found'))
            return

        ads_body = ads_table.find('tbody', class_='native')
        if not ads_body:
            self.stdout.write(self.style.ERROR('No ads tbody found'))
            return

        ads = ads_body.find_all('tr', class_='bull-list-item-js')[:10]

        for position, ad in enumerate(ads, start=1):
            ad_div = ad.find('div', class_='bull-item')
            if not ad_div:
                continue

            title_element = ad_div.find('a', class_='bulletinLink')
            title = title_element.get_text(strip=True) if title_element else 'No title'

            ad_id = ad_div['data-bulletin-id']

            author_element = ad_div.find('div', class_='address')
            author = author_element.get_text(strip=True) if author_element else 'No author'

            views_element = ad_div.find('span', class_='views')
            views = int(views_element.get_text(strip=True)) if views_element else 0

            Ad.objects.update_or_create(
                ad_id=ad_id,
                defaults={
                    'title': title,
                    'author': author,
                    'views': views,
                    'position': position,
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully parsed and saved ads'))
