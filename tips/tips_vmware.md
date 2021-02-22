#### Check Firewall rules for ssh
esxcli network firewall ruleset list --ruleset-id sshClient

#### Enable ssh
esxcli network firewall ruleset set --ruleset-id sshClient --enabled=true

#### Install HP Array Diagnostic Utility (hpacucli) in Vmware
https://api.rackspace.com/blog/array-diagnostic-utility-reports-in-vmware-esxi/

#### Execute the utility
wget http://vibsdepot.hpe.com/hpq/feb2013/esxi-5x-vibs/hpacucli/hpacucli-9.40-12.0.vib
esxcli software vib install –f –v /tmp/hpacucli-9.40-12.0.vib
