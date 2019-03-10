#!/usr/bin/env python
import os
import sys

# os
_platform = sys.platform.lower()


freebsd = "freebsd" in _platform
linux = "linux" in _platform
mac = "darwin" in _platform
osx = "darwin" in _platform
windows = "win32" in _platform or "cygwin" in _platform
cygwin = "cygwin" in _platform
unix = not windows and not cygwin

# python versions


py2 = sys.version_info[0] == 2
py3 = sys.version_info[0] == 3


def is_docker():
    if os.path.exists('/proc/self/cgroup'):
        with open('/proc/self/cgroup', 'r') as procfile:
            for line in procfile:
                fields = line.strip().split('/')
                if fields[1] == 'docker':
                    return True
    return False


docker = is_docker()
