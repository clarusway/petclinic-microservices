PATH="$PATH:/usr/local/bin"
APP_NAME="petclinic"
CFN_KEYPAIR="huseyin-${APP_NAME}-qa.key"
AWS_REGION="us-east-1"
aws ec2 create-key-pair --region ${AWS_REGION} --key-name ${CFN_KEYPAIR} --query "KeyMaterial" --output text > ${CFN_KEYPAIR}
chmod 400 ${CFN_KEYPAIR}
cp ${CFN_KEYPAIR} ${JENKINS_HOME}/.ssh/${CFN_KEYPAIR}
ls -al ${JENKINS_HOME}/.ssh