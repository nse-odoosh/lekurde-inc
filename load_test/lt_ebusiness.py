#!/bin/python3
import random
import configparser
import logging

from locust import task, between, run_single_user
from OdooLocust import OdooLocustUser, crm
from lt_webshop import WebShop

config = configparser.ConfigParser()
config.read("conf.ini")
_logger = logging.getLogger()

class BackendSalesMen(OdooLocustUser.OdooLocustUser):
    weight = int(config["weight"].get('saleman', 1))
    wait_time = between(0.1, 1)
    database = config["odoo"]["db"]
    host = config["odoo"]["url"]
    login = "invalid"
    password = "invalid"
    port = 443
    protocol = "jsonrpcs"
    _user_list = []

    def __init__(self, *args, **kwargs):
        with open('usr.txt') as usr_file:
            for line in usr_file.readlines():
                self._user_list.append(line.strip('\n').split(':'))
        return super().__init__(*args, **kwargs)
    
    def on_start(self):
        usr = random.choice(self._user_list)
        self.login = usr[0]
        self.password = usr[1]
        _logger.info(f"Load testing with user {self.login}")
        return super().on_start()

    @task(10)
    def read_partners(self):
        cust_model = self.client.get_model('res.partner')
        cust_ids = cust_model.search([], limit=80)
        prtns = cust_model.read(cust_ids, ['name'])

    tasks = {
        crm.partner.ResPartner: 1,
        crm.lead.CrmLead: 2,
        crm.quotation.SaleOrder: 1,
        read_partners:1,
    }

if __name__ == "__main__":
    run_single_user(BackendSalesMen)
