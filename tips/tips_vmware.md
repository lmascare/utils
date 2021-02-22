#### Check Firewall rules for ssh
esxcli network firewall ruleset list --ruleset-id sshClient

#### Enable ssh
esxcli network firewall ruleset set --ruleset-id sshClient --enabled=true

#### Install HP Array Diagnostic Utility (hpacucli) in Vmware
https://api.rackspace.com/blog/array-diagnostic-utility-reports-in-vmware-esxi/
