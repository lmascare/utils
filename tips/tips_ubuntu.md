# Ubuntu Tips

#### Desktop Software
```apple js
sudo apt-get update
sudo apt-get install ubuntu-desktop
```
#### Create Volumes
* lvdisplay    - Display properties of a volume group with volumes
* pvs --all    - Dispays all physical volumes and associated volume groups
* lvmdiskscan  - Scans all devices visible to LVM

**Create a Volume Group, Logical Volume and Filesystem** 
```apple js
vgcreate vg_u /dev/sdb1
lvcreate --name lv_u --size 68G vg_u
mkfs -t ext4 /dev/vg_u/lv_u
```

#### Mount an ISO volume
[Download Ubuntu Server](https://releases.ubuntu.com/20.04.2/ubuntu-20.04.2-live-server-amd64.iso?_ga=2.86706715.2027099331.1614530455-940045818.1612478744)
```text
mkdir -p /media/iso
mount -o loop <path_to_iso> /media/iso
```



