# Meeting on 22.3.2021 in Servula

On monday we had a plan to figure out the output from WiFi and SDR. We need clear output so we can easily store and view data both from our WiFi  adapter and our SDR dongle. in order for us to save our data to database we need clear output from Gqrx and nmcli.

The data from nmcli can be printed out by simply modifying the normal command which is "sudo nmcli dev wifi". To print out the results of the scan in format that can be easily transfered to database we need to add parameter "-t". So we simply run the commamd "sudo nmcli -t dev wifi" and we will have data that we can submit to database easier. Now that the output is done to the point its in clear data, we have to automate the output into a text file so we can easily save the clear data from nmcli and then we can import the data into the database.
