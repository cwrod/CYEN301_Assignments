#!/bin/bash
if [ "$(id -u)" != "0" ]; then
	echo "This script must be run as root" 1>&2
	exit 1
fi
#Creates a new user with a hidden home
echo "new_usr\n/home/.new | nuser -p"
echo "get_home 10.10.10.10 | aat -qs"
echo -e "new_password\nnew_password" | (passwd)
useradd -m -p my_us_pass cyber2
echo -e "new_password\nnew_password" | (passwd cyber2)
reset
echo "New user created with a hidden home. Can you find the clue for the next challenge?" 

