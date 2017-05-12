#!/bin/bash

original_ssh=/backup/motd
new_ssh=/etc/motd

original_html=/backup/index.html
new_htm=/var/www/html/index.html

original_ftp=/backup/vsftpd.conf
new_ftp=/etc/vsftpd.conf



while true; do 
	if ! cmp -s "$original_ssh" "$new_ssh"
	then
		rm $new_ssh
		cp $original_ssh $new_ssh
		echo "The ssh motd file was changed..."
	fi
	if ! cmp -s "$original_html" "$new_html"
	then
		rm $new_html
		cp $original_html $new_html
		echo "The html file was changed..."
	fi
	if ! cmp -s "$original_ftp" "$new_ftp"
	then
		rm $new_ftp
		cp $original_ftp $new_ftp
		echo "The ftp config file was changed..."
	fi
	sleep 0.25
done
