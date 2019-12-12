from colorama import Fore, Style
import os
import sys

__authors__ = u'"TIBTHINK, Faded-Atlas"'
__version__ = '0.3'


def logo():
    print(Fore.RED + u"""

▓█████▄ ▓█████ ▄▄▄      ▓█████▄     █     █░ ▄▄▄     ▄▄▄█████▓ ▄████▄   ██░ ██  ███▄ ▄███▓▓█████  ███▄    █ 
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▓█░ █ ░█░▒████▄   ▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █ 
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▒█░ █ ░█ ▒██  ▀█▄ ▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░▓██    ▓██░▒███   ▓██  ▀█ ██▒
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ░█░ █ ░█ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██ ▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░░██▒██▓  ▓█   ▓██▒ ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓▒██▒   ░██▒░▒████▒▒██░   ▓██░
▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▓░▒ ▒   ▒▒   ▓▒█░ ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ 
░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒      ▒ ░ ░    ▒   ▒▒ ░   ░      ░  ▒    ▒ ░▒░ ░░  ░      ░ ░ ░  ░░ ░░   ░ ▒░
░ ░  ░    ░    ░   ▒    ░ ░  ░      ░   ░    ░   ▒    ░      ░         ░  ░░ ░░      ░      ░      ░   ░ ░ 
░       ░  ░     ░  ░   ░           ░          ░  ░        ░ ░       ░  ░  ░       ░      ░  ░         ░ 
░                       ░                                    ░                                             
            
Code name: bassoon
Created by: {__authors__}
Version: {__version__} 
            """.format(__authors__=__authors__, __version__=__version__))

def toolsLogo():
    print(Fore.RED + u"""
    
▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
             ░ ░      ░ ░      ░  ░      ░  
                                            
""")
