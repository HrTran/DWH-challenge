# DWH coding challenge
This challenge demonstrates how to use pandas for processing CDC data.

## Build
Build container with Dockerfile
    
    docker build -t dwh-challenge .


Run the code
    
    docker run dwh-challenge

The result from point 1 and 2 will be appeared in the console.

## Point 3
Transaction has been made on the following table

| Types | timestamp | value |
|-------|-----------|-------|
| Credit card | 1578313800000 | 12000 |
|| 1578420000000 | 19000 |
|| 1579361400000 | 37000 |
| Saving accounts | 1577955600000 | 15000 |
|| 1578648600000 | 40000 |
|| 1578654000000 | 21000 |
||  1579505400000 | 33000 |

=> There are 7 transactions in total.