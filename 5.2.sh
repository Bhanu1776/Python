#!/bin/sh
echo "Enter a number to print it's multiplication table : "
read number
i=1
while [ $i -lt 11 ]
do
 echo "$number X $i = $(( $number * $i ))"
 i=`expr $i + 1`
done