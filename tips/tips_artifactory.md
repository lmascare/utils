## Artifactory Tips

#### Download from http://jfrog.com
https://www.jfrog.com/confluence/display/RTF/Installing+Artifactory#InstallingArtifactory-DefaultAdminUser
https://www.jfrog.com/confluence/display/RTF4X/Welcome+to+Artifactory

#### Install as root
* rpm -i jfrog-artifactory-oss-5.5.1.rpm
* It creates an artifactory user and group
* Installs in /opt/jfrog/artifactory
* To use with MySQL
     * /opt/jfrog/artifactory/bin/configure.mysql.sh
     * Enter 
        * admin user / password (root / <passwd>)
        * artifactory user / password (artifactory / )
        * It downloads JDBC connector for MySQL
            * mysql-connector-java-5.1.24.jar
            
     * 
#### Start / Stop / Status
* To start / stop / status artifactory
      * systemctl start artifactory.service
      * systemctl stop artifactory.service
      * systemctl status artifactory.service
* PID in /var/opt/jfrog/run/artifactory.pid

#### Configuration
* Default port 8081
* http://localhost:8081
* Password for 'admin' user
* Create 'generic-local' repository

#### Operational
* Upload a file 
  * curl -u<USERNAME>:<PASSWORD> -T <PATH_TO_FILE> \
  "http://172.31.251.63:8081/artifactory/generic-local/<TARGET_FILE_PATH>"
  
* Download a file
  * curl -u<USERNAME>:<PASSWORD> \
  -O "http://172.31.251.63:8081/artifactory/generic-local/<TARGET_FILE_PATH>"
