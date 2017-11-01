# Tips for Rapid7 InsightVM

### Support Info
 * info@rapid7.com
 * 866.7Rapid7

### System details
 * 8GB recommended
 * Listens on port 3780
 * DB port 5435
 * Username --> lmascare password --> <unix>
 * Admin Console --> https://localhost:3780

### First steps Nexpose Console
 * Download from Rapid7.com.
 * Get the License Key mailed to you
 * cd /u/nexpose/nsc
 * ./nsc.sh
 * To enable access to the webserver
    * firewall-cmd --zone=public --add-port=3780/tcp --permanent
    * firewall-cmd --reload
 * Login to http://127.0.0.1:3780
    * Takes quite a while to create the Postgres DB and schema
    * Enter username and password
    * Enter License Key
        * Takes a while

### Start / Stop 
 * service nexposeconsole start / stop
 * systemctl nexpose start / stop
 * Preventing from start on boot
   * update-rc.d nexpose remove
   
### Administration
 * Create administrative accounts
 * Local scan engine is created by default
 * Scan templates of interest
    * CIS 
    * Discovery Scan
 * Setup credentials on Windows
