PATH="$PATH:/usr/local/bin"
APP_NAME="petclinic"
APP_REPO_NAME="huseyin-repo/petclinic-app-qa"
APP_STACK_NAME="Huseyin-petclinic-App-QA-1"
CFN_KEYPAIR="huseyin-petclinic-qa.key"
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION="us-east-1"
ECR_REGISTRY="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
export ANSIBLE_PRIVATE_KEY_FILE="${JENKINS_HOME}/.ssh/${CFN_KEYPAIR}"
export ANSIBLE_HOST_KEY_CHECKING="False"
echo 'Packaging the App into Jars with Maven'
. ./jenkins/package-with-maven-container.sh
echo 'Preparing QA Tags for Docker Images'
. ./jenkins/prepare-tags-ecr-for-qa-docker-images.sh
echo 'Building App QA Images'
. ./jenkins/build-qa-docker-images-for-ecr.sh
echo "Pushing App QA Images to ECR Repo"
. ./jenkins/push-qa-docker-images-to-ecr.sh
echo 'Deploying App on Swarm'
. ./ansible/scripts/deploy_app_on_qa_environment.sh
echo 'Deleting all local images'
docker image prune -af