# Tips to use CLI and Python with AWS

### IAM 
 * Delete the root access keys in favor of user access keys
 * Activate MFA on root account
 * Create individual IAM users
 * Use groups to assign permissions
 * Apply an IAM password policy (does not apply to root account)
    - Require a strong password policy
    - Rotate passwords policy

### Python Modules to install
 * 
 
### AWS CLI Getting started
```text
pip3 install awscli
pip3 install --upgrade awscli

# Create an aws account for programmatic access
 * In AWS console
    - Go to IAM
    - Go to Users / Add User
    - Enter username
    - Access type 'programmatic'
    - Create group 'awsadmin' with 'AdministratorAccess' Policy
    - Download the CSV and keep safe

# Configure aws cli access. Details are stored in $HOME/.aws
 * aws configure
    - Enter Access Key ID
    - Enter Secret Key
    - Default Regions : <us-east-1> (N Virginia)
    - Default output format : json
```

#### EC2
```text
# Describe regions availble to the account
aws ec2 describe-regions

# Describe the availability zones
aws ec2 describe-availability-zones --region us-east-1

# Get the profile default region
aws configure get region --profile default
```

#### Create access key for a user
aws iam create-access-key