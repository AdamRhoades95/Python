#!/bin/bash

mysql -u root -pshr4l1f3 -e "USE Test; SELECT * FROM accounts;"

echo now the fun begins

echo enter a new id that is not in the above table: 
read ID

echo enter an email:
read email

echo enter your age
read age

echo what is your primary language? 
read language

echo what is your first name
read FName

echo what is you last name
read LName

mysql -u root -pshr4l1f3 -e "USE Test;
INSERT INTO accounts VALUE('$ID', '$email', '$age', '$language', '$LName', '$FName');
SELECT * FROM accounts"




