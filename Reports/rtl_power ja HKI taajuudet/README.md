# How can we automate our radio mapping easier

To automate our mapping of signals we receive, we have to decide on the frequencies we want to listen to and how big of a bin size we need for rtl_power to be able to accurately report the strength of the signal. We can do this by planning how the rtl_power will run and by researching on the local frequencies (radios and such). 

## RTL_Power

### What is rtl_power?

rtl_power is a wideband spectrum monitoring tool. This tool will help us to monitor a wide range of frequencies automatically and it is able to save the strength of each frequency into a CSV file and from there we can put the data into our database. We can run a command like this: ```rtl_power -f 80M:120M:125k output.csv```. This command will scan and save the output simultaneously into a single file. The scan will start from 80MHz and it will end at 120MHz. It will take samples of the signal gain in bins of 125kHz so all the invidual signals should be visible. rtl_power measures signal strength in gain of the signal is decibels. 

An example output could be that in frequency 88,6MHz there is more gain and then again frequencies 88,7MHz, 88,8MHz and 88,9MHz would have less gain and then again 89,0MHz would have more gain. Frequencies 88,6MHz and 89MHz both have known radio stations in Helsinki area where all tests will be done. 

### How does rtl_power make automation easier?

rtl_power is a great tool for us since it will be able to run scan on a very wide range of frequencies and then simultaneously save it all into a single file. Alternative options would have included using Gqrx with CLI option, but using this option would have been heavy for our hardware since to use the CLI of Gqrx you need to have the GUI open all the time. Our hardware, which is Raspberry Pi 3 can't handle the GUI while we run scans on WiFi and radio signals. Using rtl_power to scan frequencies automate the scanning of wider range and also reduces needed hardware. Using Gqrx also would not have been as automatic as rtl_power is, since using Gqrx we didn't find any way to scan a wide range of frequencies. If we were to automate Gqrx CLI to scan wide range of frequencies and then for it to save all data into single .txt file, we would have had to do a lot more work then was needed. 

## Known radio stations and their frequencies

Here is a list of known radio stations in Helsinki and their frequencies. While SDR captures a lot of other signals too, easiest way to make sure our device works is to see that mainstream radio stations are captured. The list:
``` 
* 87,9MHz - Yle Radio 1
* 88,6MHz - Radio Helsinki
* 89,0MHz - Radio Dei
* 91,9MHz - YleX
* 92,5MHz - Radio Aalto
* 94,0MHz - Yle Radio Suomi
* 94,9MHz - Radio Rock
* 96,2MHz - Iskelmä
* 98,1MHz - Radio SuomiPOP
* 98,9MHz - Yle Radio Extrem
* 100,0MHz - Radio KLF
* 101,1MHz - Yle Radio Vega
* 102,8MHz - Bassoradio
* 103,7MHz - Yle Radio Peili
* 104,6MHz - The Voice
* 105,5MHz - Järviradio
* 106,2MHz - Radio Nova
```

These are most of the mainstream radios. There are few more but not all of them share the frequencies in known sources. Next step for us is to be able to automate the input of data into the database with location of the moment the scan was ran. 
