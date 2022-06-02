!#/bin/bash

while getopts u:p: flag
do
    case "${flag}" in
        u) username=${OPTARG};;
        a) password=${OPTARG};;
    esac
done
echo "Username: $username";
echo "Password: $password";
