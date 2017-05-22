#!/bin/sh

mountfs() {
    /bin/mount -t proc proc /proc
    /bin/mount -t devtmpfs devtmpfs /dev
    /bin/mount -t sysfs sysfs /sys
    /bin/mount -t vfat /dev/sda1 /mnt
}

switch2root() {
    /bin/mount -t squashfs /mnt/rootfs.squashfs /newroot
    exec switch_root /newroot /init
}

umountfs() {
    /bin/umount /proc
    /bin/umount /sys
}

rootfs_exist() {
    umountfs
    switch2root
}

rootfs_not_exist() {
    exec /bin/sh
}

mountfs
[ -f /mnt/rootfs.squashfs ] && rootfs_exist || rootfs_not_exist
