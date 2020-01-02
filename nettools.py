#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# python net_tools module

import os
import re
import subprocess
import platform


def legal_ip(ip):
    compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    try:
        if compile_ip.match(ip):
            return True
        else:
            return False
    except TypeError:
        # print ip
        return False


def search_mac():
    macs = []
    system = platform.system()
    if system == "Windows":
        cmd = "arp -a"
        output = subprocess.getstatusoutput(cmd)
        if output[0] == 0:
            res_lines = output[1].split("\n")
            for line in res_lines:
                line = line.split(" ")
                if len(line) < 5:
                    continue
                line = [i.strip() for i in line if i.strip() != '']
                if len(line) == 3:
                    if line[2] == "动态":
                        macs.append({"mac": line[1], "ip": line[0]})
    elif system == "Linux":
        cmd = "arp"
        res = subprocess.getstatusoutput(cmd)
        for line in res[1].split('\n'):
            if len(line) == 80:
                continue
            line = line.split(" ")
            line = [i.strip() for i in line if i.strip() != '']
            if legal_ip(line[0]) and line[2] != "(incomplete)":
                macs.append({"mac": line[2], "ip": line[0]})
    return macs


if __name__ == "__main__":
    print(search_mac())
