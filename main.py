
#!/usr/bin/env python3

import argparse
import sys
import subprocess
import logging
import pystyle
import signal
import time
from pystyle import *
from rich import print
from modules.domain import Domain
from modules.live import Live
from modules.snoop import Cache
parser = argparse.ArgumentParser()
parser.add_argument('start', type=str, help='Start DCSnoop')
parser.add_argument('-w', '--wordlist', default="list.txt", help='Specify a url wordlist file')
parser.add_argument('-d', '--domain', default=None, help='Specify a domain to check')
parser.add_argument('-v', '--verbose', help='Show more info (will print lots)', action='store_true')
parser.add_argument('-l', '--live', help='Enters live mode', action='store_true')

args = parser.parse_args()
logo = """
                                         )  (  (    (
                                         (  )  () @@  )  (( (
                                     (      (  )( @@  (  )) ) (
                                   (    (  ( ()( /---\   (()( (
     _______                            )  ) )(@ !O O! )@@  ( ) ) )
    <   ____)                      ) (  ( )( ()@ \ o / (@@@@@ ( ()( )
 /--|  |(  o|                     (  )  ) ((@@(@@ !o! @@@@(@@@@@)() (
|   >   \___|                      ) ( @)@@)@ /---\-/---\ )@@@@@()( )              DCSnoop! Snoop that cache...
|  /---------+                    (@@@@)@@@( // /-----\ \\ @@@)@@@@@(  .
| |    \ =========______/|@@@@@@@@@@@@@(@@@ // @ /---\ @ \\ @(@@@(@@@ .  .
|  \   \\=========------\|@@@@@@@@@@@@@@@@@ O @@@ /-\ @@@ O @@(@@)@@ @   .
|   \   \----+--\-)))           @@@@@@@@@@ !! @@@@ % @@@@ !! @@)@@@ .. .
|   |\______|_)))/             .    @@@@@@ !! @@ /---\ @@ !! @@(@@@ @ . .
 \__==========           *        .    @@ /MM  /\O   O/\  MM\ @@@@@@@. .
    |   |-\   \          (       .      @ !!!  !! \-/ !!  !!! @@@@@ .
    |   |  \   \          )      .     .  @@@@ !!     !!  .(. @.  .. .
    |   |   \   \        (    /   .(  . \)). ( |O  )( O! @@@@ . )      .
    |   |   /   /         ) (      )).  ((  .) !! ((( !! @@ (. ((. .   .
    |   |  /   /   ()  ))   ))   .( ( ( ) ). ( !!  )( !! ) ((   ))  ..
    |   |_<   /   ( ) ( (  ) )   (( )  )).) ((/ |  (  | \(  )) ((. ).
____<_____\\__\__(___)_))_((_(____))__(_(___.oooO_____Oooo.(_(_)_)((_
"""
print(logo)

if args.live:
    if args.domain:
        Live.snoop(args.domain, args.verbose)
    else:
        print("Please specify a domain with the -d flag!")

if args.domain:
    Domain.snoop(args.domain, args.verbose)
else:
    Cache.snoop(args.wordlist, args.verbose)

