import sys
import requests
import mmh3
import codecs
import argparse
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
args = parser.parse_args()

if args.url:
    try:
        response = requests.get(args.url + '/favicon.ico')
        response.raise_for_status()
        favicon = response.content
        hash_value = mmh3.hash(codecs.encode(favicon, "base64"))
        result_text = f"Hash value of favicon from {args.url}: {hash_value}"
        colored_text = colored(result_text, 'red', attrs=['bold'])
        print(colored_text)
    except requests.exceptions.RequestException:
        error_text = "Error downloading favicon. Check your network connection."
        colored_text = colored(error_text, 'red', attrs=['bold'])
        print(colored_text)
else:
    print("No URL specified. Use -u or --url to specify a URL.")
