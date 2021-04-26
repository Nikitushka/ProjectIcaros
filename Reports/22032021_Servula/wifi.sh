#!/bin/bash
while true;
        do
        printf "\n=+=+=+=+=+=+=+=+= $(date) =+=+=+=+=+=+=+=+=\n\n" >> wifi_output.txt;
        echo "$(nmcli -t dev wifi list ifname wlan1 --rescan yes)" >> wifi_output.txt;
        printf "\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n" >> wifi_output.txt
        sleep 300;
        done
