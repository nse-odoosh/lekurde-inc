#!/bin/python3
import names
import urllib.parse
import configparser

from bs4 import BeautifulSoup
from time import sleep
from random import randint

from locust import task, run_single_user
from locust import FastHttpUser


config = configparser.ConfigParser()
config.read("conf.ini")

min_sleep = int(float(config['frontend']['min_sleep'] or 1) * 1000)
max_sleep = int(float(config['frontend']['max_sleep'] or 1) * 1000)

class WebShop(FastHttpUser):
    weight = int(config["weight"].get('webshop', 10))
    host = "https://" + config["odoo"]["url"] + '/'
    default_headers = {
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
    }

    @task
    def t(self):
        self.client.client.clientpool.close()
        self.client.cookies.clear()
        order_id = False
        csrf_token = False
        access_token = False

        with self.client.request(
            "GET",
            "/shop",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "priority": "u=0, i",
                "referer": f"{self.host}",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.client.request(
            "GET",
            "/shop/pt-996-product-template-name-996-998",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "priority": "u=0, i",
                "referer": f"{self.host}shop",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/pt-996-product-template-name-996-998",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 0,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 998,
                    "product_id": 33912,
                    "combination": [12859, 12876, 12864, 12871],
                    "add_qty": 1,
                    "parent_combination": [],
                },
            },
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/pt-996-product-template-name-996-998",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 2,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 998,
                    "product_id": 33912,
                    "combination": [12859, 12876, 12864, 12873],
                    "add_qty": 1,
                    "parent_combination": [],
                },
            },
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/pt-996-product-template-name-996-998",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 3,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 998,
                    "product_id": 33912,
                    "combination": [12859, 12876, 12864, 12873],
                    "add_qty": 1,
                    "parent_combination": [],
                },
            },
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/pt-996-product-template-name-996-998",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 4,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 998,
                    "product_id": 33916,
                    "combination": [12859, 12876, 12864, 12874],
                    "add_qty": 1,
                    "parent_combination": [],
                },
            },
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/pt-996-product-template-name-996-998",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 6,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 998,
                    "product_id": 33918,
                    "combination": [12862, 12876, 12864, 12874],
                    "add_qty": 1,
                    "parent_combination": [],
                },
            },
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/pt-996-product-template-name-996-998",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 8,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 998,
                    "product_id": 33948,
                    "combination": [12862, 12876, 12864, 12874],
                    "add_qty": 1,
                    "parent_combination": [],
                },
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/sale_product_configurator/show_advanced_configurator",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/pt-996-product-template-name-996-998",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 9,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_id": 33948,
                    "variant_values": [12862, 12876, 12864, 12874],
                    "product_custom_attribute_values": [],
                    "pricelist_id": False,
                    "add_qty": 1,
                    "force_dialog": False,
                    "no_attribute": [
                        {
                            "custom_product_template_attribute_value_id": 12864,
                            "attribute_value_name": "PAV_9542",
                            "value": "12864",
                            "attribute_name": "PA_73",
                        }
                    ],
                    "custom_attribute": [],
                    "context": {"quantity": 1, "website_id": 1, "lang": "en_US"},
                },
            },
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.rest(
            "POST",
            "/shop/cart/update_json",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/pt-996-product-template-name-996-998",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 10,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_id": 33948,
                    "product_custom_attribute_values": "[]",
                    "variant_values": [12862, 12876, 12864, 12874],
                    "no_variant_attribute_values": '[{"custom_product_template_attribute_value_id":12864,"attribute_value_name":"PAV_9542","value":"12864","attribute_name":"PA_73"}]',
                    "add_qty": 1,
                    "display": False,
                    "force_create": True,
                },
            },
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.client.request(
            "GET",
            "/shop/cart",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "priority": "u=0, i",
                "referer": f"{self.host}shop/pt-996-product-template-name-996-998",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            soup = BeautifulSoup(resp.text, 'lxml')
            order_id = soup.select_one("sup[data-order-id]")["data-order-id"]
            
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.client.request(
            "GET",
            "/shop/checkout?express=1",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "priority": "u=0, i",
                "referer": f"{self.host}shop/cart",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.client.request(
            "GET",
            "/shop/address",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "priority": "u=0, i",
                "referer": f"{self.host}shop/cart",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            soup = BeautifulSoup(resp.text, 'lxml')
            csrf_token = soup.select_one("input[name='csrf_token']")["value"]

        with self.rest(
            "POST",
            "/shop/country_infos/20",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/address",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 0,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {"mode": "billing"},
            },
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        first_name = urllib.parse.quote_plus(names.get_first_name())
        last_name = urllib.parse.quote_plus(names.get_last_name())
        name = urllib.parse.quote_plus(names.get_full_name())
        company_name = urllib.parse.quote_plus(names.get_full_name())

        with self.client.request(
            "POST",
            "/shop/address",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "cache-control": "max-age=0",
                "content-type": "application/x-www-form-urlencoded",
                "origin": f"{self.host}",
                "priority": "u=0, i",
                "referer": f"{self.host}shop/address",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            data=f"name={name}&email={first_name}%40{last_name}.local&phone=gfdgsfdgs&company_name={company_name}&vat=gfsdgd&street=gsdggfgfgfsd&street2=gffgfgfds&zip=gfdsgff&city=gfdsdgfs&country_id=20&state_id=&use_same=1&csrf_token={csrf_token}&submitted=1&partner_id=-1&mode=billing&callback=&field_required=name%2Cstreet",
            catch_response=True,
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.client.request(
            "GET",
            "/shop/confirm_order",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "cache-control": "max-age=0",
                "priority": "u=0, i",
                "referer": f"{self.host}shop/address",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.client.request(
            "GET",
            "/shop/payment",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "cache-control": "max-age=0",
                "priority": "u=0, i",
                "referer": f"{self.host}shop/address",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            soup = BeautifulSoup(resp.text, 'lxml')
            access_token = soup.select_one("form[data-access-token]")["data-access-token"]

        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.rest(
            "POST",
            "/shop/access_point/get",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/payment",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={"id": 0, "jsonrpc": "2.0", "method": "call", "params": {}},
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.rest(
            "POST",
            "/shop/update_carrier",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/payment",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 1,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {"carrier_id": "1"},
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/shop/carrier_rate_shipment",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/payment",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 2,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {"carrier_id": "1"},
            },
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.rest(
            "POST",
            f"/shop/payment/transaction/{order_id}",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}shop/payment",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 3,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "provider_id": 15,
                    "payment_method_id": 199,
                    "token_id": None,
                    "amount": None,
                    "flow": "redirect",
                    "tokenization_requested": False,
                    "landing_route": "/shop/payment/validate",
                    "is_validation": False,
                    "access_token": access_token,
                    "csrf_token": csrf_token,
                },
            },
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/payment/custom/process",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "cache-control": "max-age=0",
                "content-type": "application/x-www-form-urlencoded",
                "origin": f"{self.host}",
                "priority": "u=0, i",
                "referer": f"{self.host}shop/payment",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            data="reference=S46778",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/payment/status",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "cache-control": "max-age=0",
                "priority": "u=0, i",
                "referer": f"{self.host}shop/payment",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/payment/status/poll",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "origin": f"{self.host}",
                "priority": "u=1, i",
                "referer": f"{self.host}payment/status",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            json={
                "id": 0,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "csrf_token": csrf_token
                },
            },
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)

        with self.client.request(
            "GET",
            "/shop/payment/validate",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "priority": "u=0, i",
                "referer": f"{self.host}payment/status",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(randint(min_sleep, max_sleep) / 1000.0)
        
        with self.client.request(
            "GET",
            "/shop/confirmation",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "priority": "u=0, i",
                "referer": f"{self.host}payment/status",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(WebShop)
