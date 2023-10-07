import imp
from sys import platform

def os_extension() -> str:
    if platform == "win32":
        return "exe"
    elif platform == "linux" or platform == "linux2":
        return "elf"
    else:
        return "app"


def project_name() -> str:
    p = imp.load_source("ckl_properties", "./ckl_properties.py")
    return getattr(p, "name")