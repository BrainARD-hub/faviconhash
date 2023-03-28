# hashgenerator

Hashgenerator is a portable and modular python3 tool designed to quickly generate the favicon hash of a target domain to be use on [@shodan](https://www.shodan.io/) or to gather more IPs of the target

# Install

### Run from folder

```
git clone https://github.com/BrainARD-hub/hashgenerator.git
cd hashgenerator
pip3 install -r requirements.txt

```
# Usage

#### As a command line for single url

```
python3 hashgen.py -u <DOMAIN>

```
#### As a command line for list of urls

```
python3 hashgen.py -l url.txt

```
Example: python3 hashgen [-h] [-u] [-l] 
                         https://www.hackerone.com

--------------------------------------------------------------------------------


# License
Hashgenerator is currently under development by [@factor](https://www.linkedin.com/in/ahmedfactor/) and it's released under the GPL 3 license.
