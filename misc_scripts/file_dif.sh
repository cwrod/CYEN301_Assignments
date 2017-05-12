#!/bin/bash

original=hack.sh
new=hack2.sh

original_ssh=/backup/motd
new_ssh=/etc/motd

original_html=/backup/index.html
new_htm=/var/www/html/index.html

original_ftp=/backup/vsftpd.conf
new_ftp=/etc/vsftpd.conf



while true; do 
	if ! cmp -s "$original" "$new"
	then
		echo "Test"
		rm $new
		cp $original $new
	fi
	sleep 0.25
done
