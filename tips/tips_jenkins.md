# Jenkins Tips

**Download --> http://jenkins.io**  
**Documentation --> **  

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
