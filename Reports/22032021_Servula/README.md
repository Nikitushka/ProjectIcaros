# Meetings in Servula | Automation of SDR + WiFi output

On monday we had a plan to figure out the output from WiFi and SDR. We need clear output so we can easily store and view data both from our WiFi  adapter and our SDR dongle. in order for us to save our data to database we need clear output from Gqrx and nmcli.

### nmcli clear data and automation

The data from nmcli can be printed out by simply modifying the normal command which is "sudo nmcli dev wifi". To print out the results of the scan in format that can be easily transfered to database we need to add parameter "-t". So we simply run the commamd "sudo nmcli -t dev wifi" and we will have data that we can submit to database easier. Now that the output is done to the point its in clear data, we have to automate the output into a text file so we can easily save the clear data from nmcli and then we can import the data into the database. For this we created a simple script that will automatically scan the hotspots that are in range and will then save the clear data to a textfile. Here is the script we used to automate he scanning of WiFi hotspots.

```
!/bin/bash
while true;
        do
        printf "\n=+=+=+=+=+=+=+=+= $(date) =+=+=+=+=+=+=+=+=\n\n" >> wifi_output.txt;
        echo "$(nmcli -t dev wifi list ifname wlx3c7c3fa24fad --rescan yes)" >> wifi_output.txt;
        printf "\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n" >> wifi_output.txt
        sleep 300;
        done
```

The script will first save the output into a file called "wifi_output.txt". Then the script is defined to run a scan on wifi hotspots using device that in on interface "wlx3c7c3fa24fad". Then the script will sleep for defined time which is now 300 seconds. After the sleep it will run again and print the new data under the previous data. 

### SDR clear data and partial automation

We also need to have clear data from our SDR dongle which would include signal frequency and signal strength. With current signal strength and frequency we can deduce how well the signal is received in the current location and the current time. For this action we also tried to automate it so it would be easy to see the signal strength at the current location every time we would move. We also wanted to have same effect as our WiFi script, so we also would save the output into a single file. Everytime the script would do a scan it will save the output into a single file after the previosly written data. Here is our script.

```

#!/bin/bash
while true;
        do
        printf "\n\n=+=+=+=+=+=+=+=+= $(date) =+=+=+=+=+=+=+=+=\n" >> SDR_output.txt;
        printf "\n=-=-=-= SDR =-=-=-=\n\n" >> SDR_output.txt;
        { echo "f"; sleep 1; echo "l"; sleep 1; } | telnet localhost 7356 >> SDR_output.txt;
        printf "\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=" >> SDR_output.txt
        sleep 300;
        done
```

### New method for automation of SDR

The script we created to get clear data from SDR receiving signal was great for listening to a single frequency and outputting the strength of the signal. However the problem of this solution is that for our project we need to observe wider band of frequencies, which is impossible with only using Gqrx and it's CLI connection. Other problem with this solution is that Gqrx needs to be running in GUI mode for us to be able to use CLI over our wireguard setup. We are running SDR on Raspberry Pi's so it doesn't have large capabilities for power. If we wanted to run both SDR dongle and our WiFi adapter on a single device we need a solution for SDR that doesn't need a heavy GUI. For this problem we found a solution from RTL's own software. We found out that using rtl_power we can easily listen to certain bandwidth and then save the information into CSV file. We followed simple documentation from [KmKeen](http://kmkeen.com/rtl-power/).

Basically we can define a range of frequencies we wish to observe and we can define how often it scans the whole range and how large jumps it does between scans. For example we can define the program to scan everyhting from 80MHz to 110MHz which should include most FM radios in Helsinki. Then we can define it to do scans between every 125kHz. With this we can define it to place output into a single CSV file that we can simply read and input the important data into our database.  

Our next mission is to keep working on the database and the communication between our front and the db. After that we will have to figure out how we can input the data from the CSV file into the database. When all that works we will have to find out how we can use mobile phone to pinpoint our location and keep track of the location and time we were at the location of the scan. 
