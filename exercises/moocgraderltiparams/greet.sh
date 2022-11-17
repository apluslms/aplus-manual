#!/bin/sh

cat greeting
echo -n " "
jq -r '.lis_person_name_full' lti.json

