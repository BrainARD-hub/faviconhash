import sys
import requests
import mmh3
import codecs
import argparse
import subprocess
from termcolor import colored

# Define the script name in a stylish way
SCRIPT_NAME = """

                                                                                                                                            

 ██░ ██  ▄▄▄        ██████  ██░ ██   ▄████ ▓█████  ███▄    █    
▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒ ██▒ ▀█▒▓█   ▀  ██ ▀█   █    
▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██░▄▄▄░▒███   ▓██  ▀█ ██▒   
░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒   
░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░▒▓███▀▒░▒████▒▒██░   ▓██░   
 ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒    
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ░   ░  ░ ░  ░░ ░░   ░ ▒░   
 ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░░ ░   ░    ░      ░   ░ ░    
 ░  ░  ░      ░  ░      ░   ░  ░  ░      ░    ░  ░         ░    
                                                                                                                                                                                                        
 Author: Ahmed Habeeb @F4ct0r                                                                                                                                           
                                                                                                                                            
                                                                                                                                            
"""

# Print the script name
colorName = colored(SCRIPT_NAME, 'green', attrs=['bold'])
print(colorName)


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="URL to download favicon from")
parser.add_argument("-l", "--list", help="Path to a file containing a list of URLs")
args = parser.parse_args()

def process_url(url):
    try:
        response = requests.get(url + '/favicon.ico')
        response.raise_for_status()
        favicon = response.content
        hash_value = mmh3.hash(codecs.encode(favicon, "base64"))
        result_text = f"Hash value of favicon from {url}: {hash_value}"
        colored_text = colored(result_text, 'red', attrs=['bold'])
        print(colored_text)
    except requests.exceptions.RequestException:
        error_text = f"Error downloading favicon from {url}. Trying with curl..."
        colored_text = colored(error_text, 'yellow', attrs=['bold'])
        print(colored_text)
        try:
            output = subprocess.check_output(f"curl -s -l -k {url}/favicon.ico | python3 -c 'import mmh3,sys,codecs; print(mmh3.hash(codecs.encode(sys.stdin.buffer.read(),\"base64\")))'", shell=True)
            hash_value = output.decode('utf-8').strip()
            result_text = f"Hash value of favicon from {url}: {hash_value}"
            colored_text = colored(result_text, 'red', attrs=['bold'])
            print(colored_text)
        except subprocess.CalledProcessError:
            error_text = f"Error downloading favicon from {url} using curl. Check your network connection."
            colored_text = colored(error_text, 'red', attrs=['bold'])
            print(colored_text)
            raise ValueError(error_text)

if args.url:
    process_url(args.url)
elif args.list:
    with open(args.list, 'r') as f:
        urls = f.read().splitlines()
        for url in urls:
            process_url(url)
else:
    error_text = "No URL specified. Use -u or --url to specify a URL or -l or --list to specify a file containing a list of URLs."
    colored_text = colored(error_text, 'red', attrs=['bold'])
    print(colored_text)
    raise ValueError(error_text)
