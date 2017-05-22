import ops
import iopc

def MAIN_ENV(args):
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]

    return False

def MAIN_EXTRACT(args):
    pkg_path = args["pkg_path"]
    output_dir = ops.path_join(args["output_path"], "rootfs")

    ops.pkg_mkdir(output_dir, "bin")
    ops.pkg_mkdir(output_dir, "dev")
    ops.pkg_mkdir(output_dir, "etc")
    ops.pkg_mkdir(output_dir, "lib")
    ops.pkg_mkdir(output_dir, "mnt")
    ops.pkg_mkdir(output_dir, "newroot")
    ops.pkg_mkdir(output_dir, "root")
    ops.pkg_mkdir(output_dir, "sbin")
    ops.pkg_mkdir(output_dir, "proc")
    ops.pkg_mkdir(output_dir, "sys")

    ops.copyto(ops.path_join(pkg_path, "init"), output_dir)

    return True

def MAIN_CONFIGURE(args):
    output_dir = args["output_path"]
    return True

def MAIN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN_INSTALL(args):
    output_dir = ops.path_join(args["output_path"], "rootfs")

    src_lib = ops.path_join(output_dir, ".")
    iopc.installBin(args["pkg_name"], src_lib, "")

    return False

def MAIN_CLEAN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN(args):
    print "linux kernel"

