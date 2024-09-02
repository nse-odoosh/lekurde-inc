#!/bin/bash
if [ -z "$4" ]
  then
      echo "No argument supplied"
      echo "lt_master.sh test_file nbr_workers concurrency time spawn_rate"
      exit 1
fi

# Launch master and collect datas in csv
locust -f $1 --headless --users $3 --spawn-rate $5 --run-time $4m --master --expect-workers=$2 --csv=results/$2-$3-$4
