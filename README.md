# favihash

Favihash is a portable and modular python3 tool designed to quickly generate the favicon hash of a target domain to be use on [shodan](https://www.shodan.io/) or [binaryedge](https://www.binaryedge.io/) to gather more assets of a target

# Install

### Run from terminal

```
git clone https://github.com/BrainARD-hub/favihash.git
cd favihash
pip3 install -r requirements.txt

```
# Usage

#### As a command line for single url

```
python3 favi.py -u <DOMAIN>

```
#### As a command line for list of urls

```
python3 favi.py -l url.txt

```
Example: python3 favi.py [-h] [-u] [-l] domains

--------------------------------------------------------------------------------


# License
Favihash is currently under development by [@factor](https://www.linkedin.com/in/ahmedfactor/) and it's released under the GPL 3 license.
