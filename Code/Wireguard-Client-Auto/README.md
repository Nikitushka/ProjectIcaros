# $ whatis generate.sh
This is a quick bash script written in order to ease the burden of creating the private and public keys for our WireGuard VPN server, sending them over SSH and creating a config file.

### NOTE: The github release of this script does **NOT** have the IP address of our VPN server and it has to be manually inserted into the script at commented locations.

## Prerequisites
Before running the script, ensure that wireguard is installed. 

The instructions for installing wireguard can be found at 
[The official WireGuard website](https://www.wireguard.com/install/ "Installation - Wireguard")

## Usage
The script should be run through sudo or root and the last 1-3 digits of the IP address should be passed to the script, for example:
```
sudo bash generate.sh 123
```
This would generate the client IP to be 10.200.200.123

After the script is done running, the wg0-client interface can be brought up with:
```
sudo wg-quick up wg0-client
```
And brought down with:
```
sudo wg-quick down wg0-client
```

## References
In order to install wireguard on the server and to write this script I used this guide written by CK: [ckn.io - WireGuard VPN: Typical Setup](https://www.ckn.io/blog/2017/11/14/wireguard-vpn-typical-setup/)
#### NOTE: THIS GUIDE HAS A PROBLEM WITH THE DNS SETUP, IN ORDER TO FIX IT - [REFER TO THIS REPORT](https://github.com/Nikitushka/ProjectIcaros/tree/main/Reports/dns_problems)
