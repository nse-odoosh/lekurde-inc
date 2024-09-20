#! /bin/python3
import requests
from bs4 import BeautifulSoup
from random import choice
import configparser

config = configparser.ConfigParser()
config.read("conf.ini")
host = "https://" + config["odoo"]["url"] + '/'

with open('products.txt', 'wt') as p:
    for i in range(1,100):
        with requests.request(
            "GET",
            f"{host}/shop/page/{i}",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "priority": "u=0, i",
                "referer": f"{host}",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
        ) as resp:
            soup = BeautifulSoup(resp.text, 'lxml')
            links = []
            for link in soup.select("a[itemprop]"):
                if 'oe_product_image_link' in link['class']:
                    links.append(link['href'])
            link = choice(links)
            with requests.get(f"{host}{link}") as p_det:
                soup_det = BeautifulSoup(p_det.text, 'lxml')
                product_id = int(soup_det.select_one("input[name='product_id']")['value'])
                product_template_id = int(soup_det.select_one("input[name='product_template_id']")['value'])
                p.write(f"{i} {product_id} {product_template_id} {link} \n")