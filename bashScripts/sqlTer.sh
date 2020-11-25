#!/bin/bash
MainMenu()
{
while [ "$CHOICE" != "START" ]
do
clear
echo "================================================================="
echo "|                    Oracle All Inclusive Tool                 |"
echo "|                          NATURE BASE                         |"
echo "|           Main Menu-Select Desired Operation(s):             |"
echo "|        <CTRL-Z Anytime to Enter Interactive CMD Prompt>      |"
echo "-----------------------------------------------------------------"
echo " $IS_SELECTEDM M)  ViewManual"
echo " "
echo " $IS_SELECTED1 1)  Drop Tables"
echo " $IS_SELECTED2 2)  Create Tables"
echo " $IS_SELECTED3 3)  Populate Tables"
echo " $IS_SELECTED4 4)  Query Tables"
echo " $IS_SELECTED4 5)  To enter interactive mode"
echo " "
echo " $IS_SELECTEDE E)  End/Exit"
echo "Choose: "
read CHOICE
if [ "$CHOICE" == "0" ]
then
bash "runSqlFile.sh" "test.sql"
wait %!
elif [ "$CHOICE" == "1" ]
then
bash "runSqlFile.sh" "deletetables.sql"
wait %!
elif [ "$CHOICE" == "2" ]
then
bash "runSqlFile.sh" "createtables.sql"
wait %!
elif [ "$CHOICE" == "3" ]
then
bash "runSqlFile.sh" "populate.sql"
wait %!
elif [ "$CHOICE" == "4" ]
then
bash "runSqlFile.sh" "queries.sql"
wait %!
elif [ "$CHOICE" == "5" ]
then
bash "runSqlFile.sh" "command"
wait %!
elif [ "$CHOICE" == "E" ]
then
exit
fi
done
}


ProgramStart()
{
StartMessage
while [ 1 ]
do
MainMenu
done
}

ProgramStart


