import ops
import iopc

pkg_path = ""
output_dir = ""
output_rootfs_dir = ""

def set_global(args):
    global pkg_path
    global output_dir
    global output_rootfs_dir
    global mkinitramfs
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    output_rootfs_dir = ops.path_join(args["output_path"], "rootfs")

def MAIN_ENV(args):
    set_global(args)

    return False

def MAIN_EXTRACT(args):
    set_global(args)

    ops.pkg_mkdir(output_rootfs_dir, "bin")
    ops.pkg_mkdir(output_rootfs_dir, "dev")
    ops.pkg_mkdir(output_rootfs_dir, "etc")
    ops.pkg_mkdir(output_rootfs_dir, "lib")
    ops.pkg_mkdir(output_rootfs_dir, "mnt")
    ops.pkg_mkdir(output_rootfs_dir, "newroot")
    ops.pkg_mkdir(output_rootfs_dir, "root")
    ops.pkg_mkdir(output_rootfs_dir, "sbin")
    ops.pkg_mkdir(output_rootfs_dir, "proc")
    ops.pkg_mkdir(output_rootfs_dir, "sys")
    ops.mknod_char(ops.path_join(output_rootfs_dir, "dev"), "console", "5", "1")
    ops.mknod_char(ops.path_join(output_rootfs_dir, "dev"), "null", "1", "3")

    ops.copyto(ops.path_join(pkg_path, "init"), output_rootfs_dir)

    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(output_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)

    return True

def MAIN_BUILD(args):
    set_global(args)

    return False

def MAIN_INSTALL(args):
    set_global(args)

    src_lib = ops.path_join(output_rootfs_dir, ".")
    iopc.installBin(args["pkg_name"], src_lib, "")

    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)

    return False

def MAIN(args):
    set_global(args)

