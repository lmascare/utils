#
# The file contains the schema for lifecycle
#
create user 'lifecycle'@'localhost' identified by 'password';
grant all privileges on lifecycle.* to 'lifecycle'@'localhost' \
identified by 'password';

create database lifecycle default character set UFT8;
use lifecycle;

# 
# This table is used to track the system as it goes through
# activity --> builds, refresh, new hostname, decommission
# 
# This way we accurate track a system as it is 
# -- First built
# -- Refreshed with new harware
# -- Frame gets assigned a new hostname
# -- de-commissioned
#
create table lc_frame (
hostname       varchar(20) not null,
serialno       varchar(10) not null,
activity       varchar(20) not null,
hardware_type  varchar(20) not null,
num_cpus       varchar(20) not null,
ram_size       varchar(20) not null,
activity_date  date not null,
);

#
# This table tracks every tunable changed on a 
# given host during its lifcycle
# 
# current value --> the value live on the host
# desired value --> intended value that's in the configuration file
#
create table lc_tunables (
hostname       varchar(20) not null,
module         varchar(20) not null,
tunable_parameter varchar(20) not null,
current_value  varchar(20) not null,
desired_value  varchar(20) not null,
tuned_date     date not null,
);

# This table tracks the upgrade lifecycle of a host
# upgrade_tag# --> xoslevel, fmri etc.
#
create table lc_upgrade (
hostname       varchar(20) not null,
os_major_ver   varchar(20) not null,
os_minor_ver   varchar(20) not null,
os_micro_ver   varchar(20) not null,
upgrade_date   date not null,
upgrade_tag1    varchar(20) not null,
upgradecustom_tag2    varchar(20),
);

# Table to track the FW lifecycle of a host
# where fw_tag1 --> OBP or null
#
create table lc_firmware (
hostname       varchar(20) not null,
hardware_type  varchar(20) not null,
serialno       varchar(10) not null,
fw_version     varchar(20) not null,
fw_date        date not null,
fw_tag1        varchar(20),
fw_tag2        varchar(20),
);

#
# Table to track the symbolic links / dirs across a host
#
create table lc_sym_dir (
hostname       varchar(20) not null,
sym_dir        varchar(20) not null,
source_loc     varchar(100) not null,
target_loc     varchar(100) not null,
sd_perms       varchar(20) not null,
sd_owner       varchar(20) not null,
sd_group       varchar(20) not null,
sd_date        date not null,
);

# Table of lun count and sizes 
# LUN size will default to GB
#
create table lc_luns (
hostname      varchar(20) not null,
lun_count      int(4) not null,
lun_size       int(4) not null,
lun_date       date not null,
);

# Table of Filesystems on a host
# where fs_size & used defaults to GB
#
create table lc_fs (
hostname       varchar(20) not null,
fs_mountpt     varchar(20) not null,
fs_mountopt    varchar(20) not null,
fs_type        varchar(10) not null,
fs_size        int(4) not null,
fs_used        int(4) not null,
fs_date        date not null,
);

# Table of NFS Filesystems on a host
#
create table lc_nfs (
hostname       varchar(20) not null,
nfs_host       varchar(20) not null,
nfs_volume     varchar(10) not null,
nfs_mountpt    varchar(20) not null,
nfs_mountopt   varchar(20) not null,
nfs_size       int(4) not null,
nfs_used       int(4) not null,
nfs_date       date not null,
);
