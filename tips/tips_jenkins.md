# Jenkins Tips

**Download --> http://jenkins.io**  
**CHEF Cookbook --> https://github.com/chef-cookbooks/jenkins**  
**Documentation --> https://jenkins.io/doc/**  

#### Installation & Configuration
* Install Wiki --> https://wiki.jenkins.io/display/JENKINS/Installing+Jenkins+on+Red+Hat+distributions
* As **root**
* wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins.io/redhat/jenkins.repo
* rpm --import https://pkg.jenkins.io/redhat/jenkins-ci.org.key
* Ensure version of Java is > 1.7 for 
* yum install jenkins
* service jenkins start
* User 'jenkins' is created and process runs as this user
* Logs are in /var/log/jenkins/jenkins.log
* Initial password is at /var/lib/jenkins/secrets/initialAdminPassword

* Ensure port 8080 is permitted via the firewall
* firewall-cmd --zone=public --add-port=8080/tcp --permanent
* firewall-cmd --reload

* Open link http://localhost:8080 (enter the initial password from above)
* Install suggested plugs which installed the 'GIT' plugin
* Create the 'admin' user


**Start / Stop / Status Jenkins**
* service jenkins start / stop / status
* chkconfig jenkins on

####Integration with GIT
* Setup a new item (I used shell to run a script (python))
* Configure the Project
* In **_Source Code Management :_** **Enter the URL to the GITHUB repository**
* In the **_Build Triggers :_**   
    * Check the Poll SCM box
    * Enter the Schedule (crontab time schedule)  
* Apply & Save
* Once the job runs, check the **Console Output** of the job  

####Integration with GIT as a webhook
* Setup ngrok connection to local host
* ./ngrok authtoken <token>
    * Token saved in /root/.ngrok2/ngrok.yml
* ./ngrok http 8080 --bind-tls "both"

#####Jenkins
* Create a new Item
* Checkbox GitHub Project. Enter the URL of the repository
* Under Source Code Management - Select Git
    * Enter Repository URL (See GitHub section item-1). 
    * Leave branch at */master
* Under Build Triggers - Checkbox GitHub hook trigger for GITScm polling
* Save
* Copy to Clipboard the URL of the Jenkins Server (Top Level)

##### GitHub
* Select the Repository - Clone or Download
    * Copy the URL to clipboard. This is the Repository URL to add to Jenkins.
* In the same Repository - select Settings - Web Hooks - Add webhook
* Enter the URL of the Jenkins Server - Append **/github-webhook/** to it.
    * https://<jenkins-server>/github-webhook/ 
* Change Content-type: application/json
* For **Which events would you like to trigger this webhook?**
    * Select Just the push event
* Click 'Add webhook'

* Push a commit to the repository and observe the call to Jenkins

##### Reference Video
* https://www.youtube.com/watch?v=Z3S2gMBUkBo

#### Role based access controls
* Install the Role-based Authorization Strategy
* Create a user account.
    - Manage Jenbbb
        - Manage Users - Create User
        - Configure Global Security
            - In Authorization section enable 'Role-Based Strategy'
            - This adds a new entry 'Manage and Assign Roles' in Manage Jenkins
        - Select Manage and Assign Roles
            - Manage Roles
                - Create Global & Project Roles
            - Assign Roles 
                - Assign people to Roles 

#### Automated Deployment
* Start Jenkins
* Install the Jenkins Deploy Plugin  
    i. Go to https://wiki.jenkins.io/display/JENKINS/Deploy+Plugin  
    ii. Download the latest plugin  
    iii. In the Jenkins Administration site - Manage Jenkinks - Manage Plugins - Available  
    iv. Choose Deploy to container Plugin (search for deploy)  
    v. Select **Download & Install after restart**  
     vi. Jenkins needs to be restarted.
     
#### Configure a Build job

##### Example 1: Download / Configure / Compile Python

**This configuration works as follows**
 * A GIT repository _python_ holds the configuration file _python.txt_
 * This file will have the versions of Python to be download / configured \
   and installed
 * The Jenkins Job will poll the GIT repository for commits. In the event of
   a commit, it will begin the build process.
   
 **Steps** 
 * Define a Named Freestyle Job _download_compile_python_
 * Source Code Management
    * GIT repository _/u/gitwork/python_
 * Build Triggers
    * Poll SCM _eg every 30 mins_
        * */30 * * * *
 * Build Environment
    * Delete workspace
    * Add timestames to Console Output
 * Build _script below_
```
PY_VERSION=`cat python.txt`
pwd
for py_ver in ${PY_VERSION}
do
	wget http://python.org/ftp/python/${py_ver}/Python-${py_ver}.tar.xz
    tar xf Python-${py_ver}.tar.xz

	cd Python-${py_ver}
	./configure --prefix=/usr/local/${py_ver} --enable-unicode=ucs4 --enable-shared \
  	--enable-optimizations LDFLAGS="-Wl,-rpath /usr/local/lib"

	make
    cd ..
done
```
 * Save

#### Jenkinsfile
```
pipeline {
   agent any
   stages {
      stage('build') {
         steps {
            sh '/usr/local/bin/python2 --version'
         }
      }
   }
}
```
