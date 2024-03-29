#!/bin/bash

#export TRUSR=%testrail.usr%
#export TRPWD=%testrail.pwd%
#export SUITEID=5
#export SUITE=unit
echo "./bin/scripts/runTests $@"

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

runname=$RUN_NAME
if [ "$runname" == "" ]; then
	#SC=`echo {$suite^^}`
	runname="LOCAL_RUN_$suite"
fi


if [ "$TEAMCITY" == "" ]; then
	if [ "$TRUSR" = "" ] || [ "$TRPWD" == "" ]; then
		echo "Error: set username password first"
		exit 1
	fi
	cp etc/testrail.cfg testrail.cfg.override 
	sed -i "s/!TC_TESTRAIL_USR!/$TRUSR/" testrail.cfg.override 
	sed -i "s/!TC_TESTRAIL_PWD!/$TRPWD/" testrail.cfg.override 
	sed -i "s/!TC_TESTRAIL_SID!/$suiteid/" testrail.cfg.override 
fi

testrailstuff=""
if [ "$NEED_TESTRAILREPORT" != "" ]; then
	testrailstuff="--testrail --tr-testrun-name="$runname" --tr-config=testrail.cfg.override"
fi

echo "pytest --cov=xProject --testdox $testrailstuff $suitestr"
pytest --cov=xProject --testdox $testrailstuff $suitestr 
coverage html	
