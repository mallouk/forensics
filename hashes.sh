#!/bin/bash

DIR=("/bin" "/boot" "/cdrom" "/dev" "/home" "/lib" "/lib64" "/media" "/mnt" "/opt" "/sbin" "/snap" "/srv" "/usr" "/var")

for (( i=0; i<"${#DIR[@]}"; i++ ));
do
	find  ${DIR[${i}]} -type f -exec sha1sum "{}" +
done