# PROJECT MAY NOT WORK AS INTENDED, PLEASE REPORT ANY ISSUES


# DCSnoop
DCSnoop - Snoop on that DNS cache!

## Disclaimer
I and any contributor cannot be held responsible for any damages caused by this script. This tool has been created for educational purposes only.

## What is DNS Cache?
DNS cache refers to the temporary storage of information about previous DNS lookups on a machine's OS or web browser. Keeping a local copy of a DNS lookup allows your OS or browser to quickly retrieve it and thus a website's URL can be resolved to its corresponding IP much more efficiently.
## What does this tool do?
This tool will send a non-recursive query to your home network's DNS server (usually `192.168.1.1`). From here it is checked if the query was successful. If this request fails, the requested website is considered **not** in the network's **DNS cache**. Success indicates that the selected URL **is** cached.
## Usage
> With a wordlist
```python
python3 main.py -w [wordlist] start
```
> Verbose mode (will print lots of scrambled stuff)
```python
python3 main.py -v start
```
> Specified Domain
```python
python3 -d [domain] start
```
### Live Mode
Live mode, constantly checks a specific domain and will only end when it is found in the network's DNS Cache. The main idea of this is to give a general approximation of when a url was visited on a network you are connected to.
> Usage
```
python3 -l -d [domain] start
```
## Installation
```
git clone https://github.com/benjibrown/DCSnoop
cd DCSnoop
pip3 install -r requirements.txt
python3 main.py
```
## Contributing

If you would like to contribute to this repository, please submit an issue or pull request. Many thanks :)
