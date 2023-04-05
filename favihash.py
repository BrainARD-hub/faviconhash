import sys
import requests
import mmh3
import codecs
import argparse
import subprocess
from termcolor import colored


# Define the script name in a stylish way
SCRIPT_NAME = """

 ________                _   ____  ____                __       
|_   __  |              (_) |_   ||   _|              [  |      
  | |_ \_|,--.  _   __  __    | |__| |   ,--.   .--.   | |--.   
  |  _|  `'_\ :[ \ [  ][  |   |  __  |  `'_\ : ( (`\]  | .-. |  
 _| |_   // | |,\ \/ /  | |  _| |  | |_ // | |, `'.'.  | | | |  
|_____|  \'-;__/ \__/  [___]|____||____|\'-;__/[\__) )[___]|__] 
                                                                   
                                                                                                                                                                                                        
 Author: Ahmed Habeeb @F4ct0r                                                                                                                                           
"""
# Print the script name
colorName = colored(SCRIPT_NAME, 'green', attrs=['bold'])
print(colorName)

# Define the TIPS in a stylish way
TIPS = """
Use your result on SHODAN or BINARYEDGE to discover more assets 
of your target.
"""
# Print the tips
colorTIP = colored(TIPS, 'red', attrs=['bold'])
print(colorTIP)

# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="URL to download favicon from")
parser.add_argument("-l", "--list", help="Path to a file containing a list of URLs")
args = parser.parse_args()

def process_url(url):
    try:
        response = requests.get(url + '/favicon.ico')
        response.raise_for_status()
        favicon = response.content
    except requests.exceptions.RequestException:
        subprocess_result = subprocess.run(['curl', '-s', '-l', '-k', url+'/favicon.ico'], stdout=subprocess.PIPE)
        favicon = subprocess_result.stdout
    hash_value = mmh3.hash(codecs.encode(favicon, "base64"))
    result_text = f"Hash value of favicon from {url}: {hash_value}"
    colored_text = colored(result_text, 'yellow', attrs=['bold'])
    print(colored_text)

if args.url:
    process_url(args.url)
elif args.list:
    with open(args.list, 'r') as f:
        urls = f.read().splitlines()
        for url in urls:
            process_url(url)
else:
    print("No URL specified. Use -u or --url to specify a URL or -l or --list to specify a file containing a list of URLs.")
