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

class Cache():
    def __init__(wordlist):
        return
    def snoop(wordlist, verbose=False):
        st = time.time()
        timestamp = time.strftime('%H:%M:%S')
        with open(wordlist) as domains:
            count = 1
            if verbose == True:
                for line in domains:
                    out = subprocess.Popen(['nslookup', '-norecurse', line], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.STDOUT)
                    stdout,stderr = out.communicate()
                    url = line.strip("\n")
                    if "Non-".encode("utf-8") in stdout:
                        print("---------------------------------------------------------------------------------------------")
                        print(f"[green]{stdout}[/green]")
                        print(f"\n[{timestamp}] [green]{url} found in network DNS Cache! | {count} tests completed! [/green]")
                    else:
                        print("---------------------------------------------------------------------------------------------")
                        print(f"[red]{stdout}[/red]")
                        print(f"\n[{timestamp}] [red]{url} not found in network DNS Cache! | {count} tests completed![/red]")
                    count +=1
                        

                et = time.time()
                elapsed_time = et - st
                count = count - 1
                print(f"Completed {count} tests in {elapsed_time} seconds")
                exit()



            
            for line in domains:
                out = subprocess.Popen(['nslookup', '-norecurse', line], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.STDOUT)
                stdout,stderr = out.communicate()
                url = line.strip("\n")
                if "Non-".encode("utf-8") in stdout:
                    print("---------------------------------------------------------------------------------------------")
                    print(f"[{timestamp}] [green]{url} found in network DNS Cache! | {count} tests completed! [/green]")
                else:
                    print("---------------------------------------------------------------------------------------------")
                    print(f"[{timestamp}] [red]{url} not found in network DNS Cache! | {count} tests completed![/red]")
                count +=1
            et = time.time()
            elapsed_time = et - st
            count = count - 1
            print(f"Completed {count} tests in {elapsed_time} seconds")
            exit()
