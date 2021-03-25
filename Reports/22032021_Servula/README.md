# Meeting on 22.3.2021 in Servula

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

We also need to have clear data from our SDR dongle which would include signal frequency and signal strength. 
