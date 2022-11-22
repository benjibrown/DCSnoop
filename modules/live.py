import argparse
import sys
import subprocess
import time
import logging
import pystyle
import signal
import time
import rich
from pystyle import *
from rich import print
st = time.time()
class Live():
    def __init__(domain):
        return
    def snoop(domain, verbose=False):
        count = 1
        timestamp = time.strftime('%H:%M:%S')
        if verbose == True:
            while True:
                out = subprocess.Popen(['nslookup', '-norecurse', domain],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.STDOUT)
                stdout,stderr = out.communicate()
                if "Non-".encode("utf-8") in stdout:
                    print("---------------------------------------------------------------------------------------------")
                    print(f"[green]{stdout}[/green]")
                    print(f"[{timestamp}] [green]{domain} found in network DNS Cache!")
                    et = time.time()
                    elapsed_time = et - st
                    print(f"Completed {count} tests in {elapsed_time} seconds")
                    exit()
                else:
                    print("---------------------------------------------------------------------------------------------")
                    print(f"[red]{stdout}[/red]")
                    print(f"[{timestamp}] [red]{domain} not found in network DNS Cache!")
                time.sleep(0.05)
                count +=1

        while True:
            out = subprocess.Popen(['nslookup', '-norecurse', domain],
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT)
            stdout,stderr = out.communicate()
            if "Non-".encode("utf-8") in stdout:
                print("---------------------------------------------------------------------------------------------")
                print(f"[{timestamp}] [bold green]{domain} found in network DNS Cache!")
                et = time.time()
                elapsed_time = et - st
                print(f"Completed {count} tests in {elapsed_time} seconds")
                exit()
            else:
                print("---------------------------------------------------------------------------------------------")
                print(f"[{timestamp}] [bold red]{domain} not found in network DNS Cache!")
                # Try not to DDoS website - sleeping for 0.05 seconds per iteration
            time.sleep(0.05)
            count +=1
        
