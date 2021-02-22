#### Check Firewall rules for ssh
esxcli network firewall ruleset list --ruleset-id sshClient

#### Enable ssh
esxcli network firewall ruleset set --ruleset-id sshClient --enabled=true
