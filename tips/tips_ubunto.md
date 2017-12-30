# Ubuntu Tips

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

