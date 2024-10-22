#!/bin/bash
##########Config##########
#targetpath="/home/joey/Desktop/ShootSave/"
targetpath="./ShootSave"
##########################
currentdate=$(date "+%Y_%m_%d_%H_%M_%S")
logpath=$targetpath/$currentdate/

a=0
while [ -d "$logpath" ]
	do
		let a++
		logpath=$path"("$a")/"
	done
echo $logpath

mkdir -p $logpath

logfile=$logpath"stand.log"
errfile=$logpath"error.log"
touch $logfile
touch $errfile

#python3 /home/joey/github/jetson-nano-shoot/shoot.py $logpath 1>$logfile 2>$errfile
python3 /home/joey/github/jetson-nano-shoot/shoot.py $logpath