#!/bin/bash

runname=$RUN_NAME
if [ "$runname" == "" ]; then
	runname="LOCAL_RUN"
fi

suiteid=$SUITEID
if [ "$suiteid" == "" ]; then
	suiteidstr=""
else
	suiteidstr="--tr-testrun--suite_id=$suiteid"
fi

suite=$SUITE
if [ "$suite" == "" ]; then
	suitestr="tests/$suite/"
else
	suitestr="tests/"
fi


if [ "$TRUSR" == "" ] || [ "$TRPWD" == "" ]; then
	echo "Error: set username password first"
	exit 1
fi

echo "Inovcation: pytest --cov=xProject --testdox --testrail $suiteidstr --tr-email=$TRUSR --tr-password=$TRPWD --tr-testrun-name="$runname" --tr-config=etc/testrail.cfg $suitestr "
pytest --cov=xProject --testdox --testrail $suiteidstr --tr-email=$TRUSR --tr-password=$TRPWD --tr-testrun-name="$runname" --tr-config=etc/testrail.cfg $suitestr 
coverage html
