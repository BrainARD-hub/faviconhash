import argparse
import requests
import hashlib
from colorama import init, Fore, Style

# create an argument parser
parser = argparse.ArgumentParser(description=f'{Fore.BLUE}{Style.BRIGHT}Favicon Hash Generator{Style.RESET_ALL} - by John Doe')

# add the URL argument
parser.add_argument('-u', '--url', type=str, required=True, help='The website URL')

# parse the command-line arguments
args = parser.parse_args()

# make a request to the website to retrieve the favicon
response = requests.get(args.url + '/favicon.ico')

# calculate the md5 hash of the favicon content
favicon_hash = hashlib.md5(response.content).hexdigest()

print(f'{Fore.GREEN}Favicon hash:{Style.RESET_ALL} {favicon_hash}')
