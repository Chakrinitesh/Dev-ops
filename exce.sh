#!/bin/bash
packer version
packer validate packer.json
if [ $? -eq 0 ]
then
echo "if the code the is validate, lets build"
#packer build packer.json 2>&1 | tee output.txt
tail -2 output.txt | head -2 | awk 'match($0, /ami-.*/) { print substr($0, RSTART, RLENGTH) }' > ami.txt
AMIID=$(cat ami.txt)
#echo "variable imagename { default = \"$AMIID\" }" >> variables.tf
terraform init
terraform apply -auto-approve
else
echo "the code has erroe please check"
fi
