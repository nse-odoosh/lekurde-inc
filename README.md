# Tested intance

Module lekurde contains dependencies for a e-commerce load test.
Once installed populate the database with required datas:

```
odoo-bin populate --size=large
```

# Perform load test

## Create venv

```
python3 -m venv lt_venv
source lt_venv/bin/activate
python3 -m pip install -r load_test/requirements.txt
```

## Activate venv

If not already done:
```
source lt_venv/bin/activate
```

## Set passwords for load test

Load testing is performed with various random backend users. TO make this possible,
the load script must be aware of login/passwords. A small script define passwords for users.
Depending on the number of users, this can takes a while.

Of course, don't run this on a production database.

```
cd load_test
python3 lt_users.py
```
The result will be a `usr.txt` file containing login/password pairs.

## launch locust web interface

```
cd load_test
locust -f lt_ebusiness.py
```

then open a web browser on http://localhost:8089

## launch locust without web interface

```
locust -f lt_ebusiness.py --headless --users 100 --spawn-rate 10 --run-time 2m
```

## launch locust with workers


lt.sh file:
```bash
#!/bin/bash
if [ -z "$4" ]
  then
      echo "No argument supplied"
      echo "lt.sh test_file nbr_workers concurrency time [rounds]"
      exit 1
fi

nbr_rounds=1
if [ -z "$5" ]
  then
    nbr_rounds=$5
fi

num_test=0
while [[ $num_test -le $nbr_rounds ]]
do
    num_test=$(( $num_test + 1 ))
    # Launch required number of workers
    x=1
    while [[ $x -le $2 ]]
    do
        locust -f $1 --worker --only-summary > /dev/null 2>&1 &
        x=$(( $x + 1 ))
    done
    # Launch master and collect datas in csv
    locust -f $1 --headless --users $3 --spawn-rate $3 --run-time $4m --master --expect-workers=$2 --csv=results/$2-$3-$num_test
done
```

This will launch multiple locust workers, one main worker, and collect statistics in a `results` folder.

Results are available in csv format, in the results subfolder