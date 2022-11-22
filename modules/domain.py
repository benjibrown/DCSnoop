import argparse
import sys
import subprocess
import logging
import pystyle
import signal
import time
import rich
from pystyle import *
from rich import print
st = time.time()
class Domain():
    def __init__():
        return
    def snoop(dom, verbose=False):
        timestamp = time.strftime('%H:%M:%S')
        if verbose == True:
            out = subprocess.Popen(['nslookup', '-norecurse', dom],
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT)
            stdout,stderr = out.communicate()
            if "Non-".encode("utf-8") in stdout:
                print("---------------------------------------------------------------------------------------------")
                print(f"[green]{stdout}[/green]")
                print(f"[{timestamp}] [green]{dom} found in network DNS Cache! [/green]")
            else:
                print("---------------------------------------------------------------------------------------------")
                print(f"[red]{stdout}[/red]")
                print(f"[{timestamp}] [red]{dom} not found in network DNS Cache![/red]")
            et = time.time()
            elapsed_time = et - st
            print(f"Finished in {elapsed_time} seconds")
            exit()
        out = subprocess.Popen(['nslookup', '-norecurse', dom],
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT)
        stdout,stderr = out.communicate()
        if "Non-".encode("utf-8") in stdout:
            print("---------------------------------------------------------------------------------------------")
            print(f"[{timestamp}] [green]{dom} found in network DNS Cache! [/green]")
        else:
            print("---------------------------------------------------------------------------------------------")
            print(f"[{timestamp}] [red]{dom} not found in network DNS Cache![/red]")
        et = time.time()
        elapsed_time = et - st
        print(f"Finished in {elapsed_time} seconds")
        exit()
