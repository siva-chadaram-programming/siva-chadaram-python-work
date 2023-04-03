#! /bin/bash

echo "Enter name : "
read name
echo "Entered name : $name "

##########Multiple Inputs######

echo "Enter animals : "
read animal1 animal2 animal3 
echo "Entered animals : $animal1, $animal2, $animal3"

###input value return in same line####

read -p 'Enter username : ' user_var
echo "username :  $user_var"

#input value hide in console
read -p 'Enter username : ' user_val 
read -sp 'Enter userpassword : ' pass_var
echo "password : $pass_Var "

#input in the array form##

echo "Enter Names : "
read -a names
echo "Names : ${names[0]}, ${names[1]}"

#Defalut variable when no varialble defined#
#REPLY

echo "Enter name : "
read 
echo "$REPLY"
