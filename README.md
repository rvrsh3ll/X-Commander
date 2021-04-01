# X-Commander
 MySQLX Multitool

## Why?
I found there to be a lack of easy-to-use solutions for attacking MySQLX or XDevAPI. 

## RTFM
[XDevAPI Guide](https://dev.mysql.com/doc/x-devapi-userguide/en/)

## Brute Force
python3 x-commander.py -u admin --passwordfile passwords.txt -t 192.168.164.132 --verbose -s

![Brute Force Example](/img/brute_success.png)

## Query
python3 x-commander.py -u admin -P admin -t targetIP --query "SHOW DATABASES" --verbose

![Brute Force Example](/img/databases.png)