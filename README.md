# DCSnoop
DCSnoop - Snoop on that DNS cache!

## What is DNS Cache?
DNS cache refers to the temporary storage of information about previous DNS lookups on a machine's OS or web browser. Keeping a local copy of a DNS lookup allows your OS or browser to quickly retrieve it and thus a website's URL can be resolved to its corresponding IP much more efficiently.
## What does this tool do?
This tool sends a non recursive query to your home network's DNS server (usually located at `192.168.1.1`) and if the request is successfull, it means that the website is in the DNS cache as if it were not the request would fail. For example, if you were to run the tool against the domain google.com, and it returned that it was not in local DNS cache, if you then visited it in your browser and reran it would state that it is in your local DNS cache. This is because your router has stored the request temporarily for faster access in a certain time period.
## Usage

### Live Mode


## Installation
```
git clone https://github.com/benjibrown/DCSnoop
cd DCSnoop
pip3 install -r requirements.txt
python3 main.py
```
## Contributing
