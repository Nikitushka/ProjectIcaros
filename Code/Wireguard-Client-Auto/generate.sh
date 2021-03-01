#!/bin/bash
IP=10.200.200.$1;

# check if the argument passed to this script is null, if it is: echo usage
if [ -z "$1" ]
then
	echo "usage: sudo bash generate.sh <desired-IP-address-end>";
else
	echo "Creating .wireguard directory in /home...";
	mkdir ~/.wireguard;
	cd ~/.wireguard; 

	echo "Generating wireguard client keys in ~/.wireguard/ ...";
	wg genkey | tee client_private_key | wg pubkey > client_public_key;
	
	echo "Using ssh to add new user on the VPN Server (You'll have to enter sysadm password twice)...";
	PUBKEY=$(cat client_public_key);
	PRIVATEKEY=$(cat client_private_key);
	# VPN Server IP hidden for security reasons, changed to localhost instead
	ssh -t sysadm@localhost "sudo -S wg set wg0 peer $PUBKEY allowed-ips $IP/32";
	
	echo "Generating wg0-client.conf in /etc/wireguard ...";
	# Change endpoint IP from localhost to VPN Server IP 
	CONFIG="$(cat <<-EOF
	[Interface]
	Address = $IP/32
	PrivateKey = $PRIVATEKEY
	DNS = 10.200.200.1

	[Peer]
	PublicKey = X7kCaXkoE+O4wgjBHR2NXXIqh9z8w93ZlZSxwdbAFDg=
	Endpoint = localhost:51820
	AllowedIPs = 0.0.0.0/0
	PersistentKeepalive = 21
	EOF
	)"
	echo "$CONFIG" > /etc/wireguard/wg0-client.conf;
	
	echo "installing resolvconf just to be sure..."
	sleep 3;
	sudo apt install resolvconf;

	echo "!! DONE !!";
	sleep 1;
	echo "You can now bring up the VPN interface with 'sudo wg-quick up wg0-client' and bring it down with 'sudo wg-quick down wg0-client'";
	sleep 1;
	echo "!! DONE !!";

fi
