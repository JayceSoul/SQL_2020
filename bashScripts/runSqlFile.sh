#!/bin/bash

if [ -z "$1" ]
then
exit
fi

if [ "$1" == "command" ]
then
sqlplus64 "CMOZOLA/02099122@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl)))"
else
echo "exit" | sqlplus64 "CMOZOLA/02099122@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl)))" @"$1"
while [ "$LEAVE" != "exit" ]
do
echo "Type 'exit' to exit"
read LEAVE
done
fi

