* sudo useradd -c 'Hadoop User' -c /home/hadoop hadoop (lmascare)
*  
* sudo chown hadeep:hadoop /home/hadoop
* su - hadoop
* mkdir .ssh ; chmod 700 .ssh
* Download java from http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
* sudo mv jdk1.8.0_121 /usr/local

* Download hadoop from hadoop.apache.org
* su to root
* cd /usr/local ; gunzip -c ~/Downloads/hadoop-2.7.3.tar.gz | tar xf -
* mv hadoop-2.7.3 hadoop

* Update .bashrc
* JAVA_HOME=/usr/local/jdk1.8.0_121
* HADOOP_HOME=/usr/local/hadoop
* PATH=$PATH:${JAVA_HOME}/bin:${HADOOP_HOME}/bin
* export PATH
* 
* Run example
* mkdir input ; cp /usr/local/hadoop/*.txt input
* hadoop jar
* /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar
* \
* wordcount input output


