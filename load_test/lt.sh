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
