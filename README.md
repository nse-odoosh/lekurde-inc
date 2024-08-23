# Tested intance

Module lekurde contains dependencies for a e-commerce load test.
Once installed populate the database with required datas:

```
odoo-bin populate --size=large
```

# Perform load test

## Create venv

```
$ python3 -m venv lt_venv
$ source lt_venv/bin/activate
$ python3 -m pip install -r load_test/requirements.txt
```

## Activate venv

If not already done:
```
$ source lt_venv/bin/activate
```

## Set passwords for load test

Load testing is performed with various random backend users. TO make this possible,
the load script must be aware of login/passwords. A small script define passwords for users.
Depending on the number of users, this can takes a while.

Of course, don't run this on a production database.

```
$ cd load_test
$ python3 lt_users.py
```
The result will be a `usr.txt` file containing login/password pairs.

## launch locust web interface

```
$ cd load_test
$ locust -f lt_ebusiness.py
```

then open a web browser on http://localhost:8089

## launch locust without web interface

```
$ locust -f lt_ebusiness.py --headless --users 100 --spawn-rate 10 --run-time 2m
```

Results are available in csv format, in the results subfolder