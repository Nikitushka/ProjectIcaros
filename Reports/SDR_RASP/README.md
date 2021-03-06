# RTL-SDR

Started researching about RTL-SDR technology so that we can start the project as soon as possible when our RTL-SDR dongel arrives.

First I started looking into how RTL-SDR radios work with youtube videos. Many of the videos gave good basic information about what to buy if you want to start with SDR.
We already have purchased one of the suggested devices and it is on it's way.
https://www.rtl-sdr.com/product/rtl-sdr-blog-r820t2-rtl2832u-1ppm-tcxo-sma-software-defined-radio-with-dipole-antenna-kit/

After looking at videos I started playing around how to use the websdr. 
Websdr is a page full of different SDR devices around the world that you can use to listen to the signals.

Using the sdr at first was difficult. 
Many of websdr sites offer easy tags where to find different channels.
This was a good way to start practicing how to pinpoint the signal so we could get the optimal sound quality.
After a while I started to explore signals with out tags. 
The task proved difficult but not impossible. 
After exploring found a signal that consisted of small beeps. 
Looking at the tag it said it is a pager on frequenzy 26150.00kHz.
To find spesific signal traffic (for example airlines) you can usually google the right range of frequenzys.

## Raspberry pi - Installation
To get a headstart I started to install Raspberry pi 4 with Raspbian os.
The first installation of Kali linux we hade failed because of driver problems with a small screen that is on the Raspberry pi. 
This second Raspberry pi is to be used on the sdr research with the sdr-dongle.
The OS we are using is the basic installation of raspbian (version 2021-01-11). 
We are installing differrent software on the raspberry pi:
* GNU radio for sdr
* Wireguard for remote access
* Openssh server for remote access
* VNC for remote access with desktop

During the installation ran into a problem with raspberry pi and monitor. 
The raspberry pi didn't want to show up on the monitor or the built-in monitor.
The problem seems to be with raspberry pi's mini hdmi connector.
The problem was fixed with enough tries. Also the built-in monitor started to work when I installed the drivers again and rebooted the system.
Also when trying to configure the raspberry pi to be seen with VNC viewer ran into connection problem.
Congifurations have failed and I can't connect to the pi. 
The problem seems to be with the accounts.
Later continued working with the VNC and manged to get connection with it and ssh in the local network.

## Managing connections

After getting our SDR pi working I started on building the setup. We need the setup to be portable in order to be able to go around and map these signal that are found everywhere.
Firstly I started to configure our pi to be accessable with ssh from my own network.
Setting up the connections was easy as raspbian offers ssh to be enabled with a quick switch.
Next step was to change some settings in my router so that we could get connection to the pi.
I navigated to the IP address of my routers management page. These management pages can be found just by using google.
From the router I needed to Port Forward the ssh access so that other project members could get the access.

Next I started to work with VNC to get a remote desktop access to the pi.
To use the VNC you need to install the vnc server on your platform of choice. I used this article from RASPBERRY PI FOUNDATION https://www.raspberrypi.org/documentation/remote-access/vnc/ 
To start installing the VNC connection we need to run following commands that install us the needed packages.
* sudo apt update
* sudo apt install realvnc-vnc-server realvnc-vnc-viewer
Next thing we need to do is to enable the VNC server. As we are using Raspbian in this machine we can use the raspi-config.
* sudo raspi-config
From the menu we need to find and enable the VNC.
To use the VNC you will need to start the vncserver by using command 'vncserver'. After using the command you should see the IP and port information, also the catch phrase to identify that you are connecting to the right device.
To use the VNC remote desktop you need to have a VNC viewer installed and you need to know the device IP, correct port number and the configured VNC password.
