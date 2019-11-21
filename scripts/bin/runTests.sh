#!/bin/bash

runname=$RUN_NAME
if [ "$runname" == "" ]; then
	runname="LOCAL_RUN"
fi

suiteid=$2
if [ "$suiteid" == "" ]; then
	suiteidstr=""
else
	suiteidstr="--tr-testrun-suite_id=$suiteid"
fi

suite=$4
if [ "$suite" != "" ]; then
	suitestr="tests/$suite/*"
else
	suitestr="tests/"
fi


if [ "$TRUSR" = "" ] || [ "$TRPWD" == "" ]; then
	echo "Error: set username password first"
	exit 1
else
	if [ "$TEAMCITY" == "" ]; then
		cp etc/testrail.cfg testrail.cfg.override 
		sed -i "s/!TC_TESTRAIL_USR!/$TRUSR/" testrail.cfg.override 
		sed -i "s/!TC_TESTRAIL_PWD!/$TRPWD/" testrail.cfg.override 
		sed -i "s/!TC_TESTRAIL_SID!/$suiteid/" testrail.cfg.override 
	fi
fi

echo "Inovcation: pytest --cov=xProject --testdox --testrail $suiteidstr --tr-testrun-name="$runname" --tr-config=testrail.cfg.override $suitestr "
pytest --cov=xProject --testdox --testrail --tr-testrun-name="$runname" --tr-config=etc/testrail.cfg $suitestr 
coverage html
