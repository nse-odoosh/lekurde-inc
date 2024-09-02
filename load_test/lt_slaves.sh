#!/bin/bash
if [ -z "$2" ]
  then
      echo "No argument supplied"
      echo "lt_slaves.sh nbr_workers master_host"
      exit 1
fi

# Launch required number of workers
x=1
while [[ $x -le $1 ]]
do
    locust -f - --worker --only-summary  --master-host $2 > /dev/null 2>&1 &
    x=$(( $x + 1 ))
done
