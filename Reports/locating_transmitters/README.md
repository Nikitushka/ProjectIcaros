# Locating the signal with RTL-SDR

At this moment there are few applications that can with a help of a few RTL-SDRs find the direction of the signal that the application is listening to. The few RTL-SDRs collect the signals direction and then after the application has taken enough readings from multiple locations it can calculate the general location of the transmitter with the readings from many directions. Good example would be KerberosSDR that was created for the purpose of locating signal. KerberosSDR has it's own rig that has 4 RTL-SDR receivers on it. The project has it's own software too that will with multiple readings from different locations be able to locate the transmitter within few hundred meters. Here is an interesting article about the KerberosSDR: https://www.rtl-sdr.com/locating-a-radio-transmitter-with-direction-finding-techniques-and-kerberossdr-our-4-tuner-coherent-rtl-sdr/. 

### Locating the signal with one RTL-SDR is near impossible. There are few different options to locating transmitter:

#### Direction finding (DF)

To find a direction of the transmission what you need at least is an 1 receiver and 1 rotatable directional antenna. This way doesn't work well since you would need to know the direction the signal is coming from. The accuracy of the bearing using this method can be very low since there can be reflections that would interfere with the actual direction. The correct way of direction finding is used with many receivers, even 4 or 5 in many cases. The way that direction finding works with multiple receivers is that there is one center antenna that provides reference to the other receivers around it. This way the direction can be found more accurately with help of a software.

#### Cross-bearing direction finding

This way you would be using 2 different set locations for receiving the signal. This method also requires rotatable directional antenna. with this method the signal would be received from different angles and with this information the general direction can be calculated.

#### Multilateration using triangulation and the time difference of arrival of the signal

This is the method that is most accurate in locating the transmission. This method works with 3 different receiver locations that would best to be in a triangle formation. This would assume that the transmitter is within the triangle and then one would calculate the time it took for the signal to arrive to each different location the signal is being captured. 

### In conclusion

Locating the exact location of a signal and pinpointing it on a map will be near impossible thing to do without large amount of work and capability to buy large amount of hardware. I will present the finding to our group and we will continue the research on the subject.

##### Sources:

* All the information can be found from https://www.rtl-sdr.com/ and https://www.rtl-sdr.com/forum/.
