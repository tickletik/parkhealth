#!/bin/sh
for file in `ls *.$1`
do	
	sed s'/django\.loc/parkhealth\.dev/g' < $file > blah
	mv blah $file	
done	


