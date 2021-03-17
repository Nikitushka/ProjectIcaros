# Testing SDR on Raspberry Pi 4 via VNC Viewer

### Taking control of the Raspberry Pi with VNC Viewer

Our Raspberry Pi has it's own small monitor, but because of the resolution and the difficulty of use, we prefer to connect to the Raspberry Pi via means where we can have graphical view of the desktop. 
For this use i use VNC Viewer which is really handy when i want to quickly do something with the Raspi. It all starts with launching Raspi and launching the VNC Viewer. Then i connect to designated local IP through VNC client and i can log in with Raspi's logins.

### First tests on SDR on my part

We want to test if we could listen to broadcasts and to test can we even find them. The first thing is to test can we even hear basic counds from example soundcloud.
As it stands our Raspi doesn't transfer sound over HDMI nor over 3,5mm audio. After some research i found Raspi's own guide to audio, and went through system options to set output to 3,5mm. 
The guide can be found [here](https://www.raspberrypi.org/documentation/configuration/audio-config.md#:~:text=The%20Raspberry%20Pi%20has%20up,present%2C%20and%20a%20headphone%20jack.&text=If%20your%20HDMI%20monitor%20or,plugged%20into%20the%20headphone%20jack).

After this i want to try and find some signal i could listen to. After launching Gqrx we can instantly see green on our otherwise blue waterfall view. When we focus on parts where there is green, the static changes a little bit, but we still cannot hear anyhting.
Even though we see green on our waterfall, we cannot hear anything from these waterfalls. I will do more research about RTL-SDR and i will get back to trying after the research.

![Waterfall view on Rasbian](https://github.com/Nikitushka/ProjectIcaros/blob/drafts/Reports/week8%269_SDR_testing/raspigqrx1_9_3_2021.PNG)

### Trying out different OS's and finding success

Because of the failures we experienced through Rasbian and Windows 10, we decided to try out our SDR on POP OS that was installed on a laptop. After following simple instructions from [Ranous](https://ranous.wordpress.com/) we were able to actually get a waterfall that looked how it is supposed to. Also we could actually hear the transmissions which were mostly different music. 

![Waterfall on POP OS](https://github.com/Nikitushka/ProjectIcaros/blob/drafts/Reports/week8%269_SDR_testing/IMG_20210314_182700.jpg)

Ranous has this very simple to follow [guide](https://ranous.files.wordpress.com/2016/03/rtl-sdr4linux_quickstartv10-16.pdf) that we used in all of our unix based devices. After the confirmation that our SDR dongle works, and that we can hear transmissions on POP OS, we decided to start looking for OS that would work on our Raspberry Pi 4 that has 4GB of RAM. We first tried Kali Linux and we couldn't get the dongle working with Ranous's guide. After this we tried Xubuntu 19.10 for Raspberry Pi 4, but we also could not get any waterfall view from CubicSDR or Gqrx. After this we were little bit disappointed, but i quickly looked into what is the most recent OS for Raspberry Pi 4 and found out that there was a very good guide to installing Xubuntu 20.10 for Raspberry Pi 4 [here](https://ubuntu.com/tutorials/how-to-install-ubuntu-desktop-on-raspberry-pi-4#1-overview).

After following the above guide on how to install Xubuntu 20.10 and launching the Raspi, we followed Ranous's guide on how to install RTL-SDR drivers from [osmocom.org](http://git.osmocom.org/), and how to set up the RTL-SDR dongle, so Xubuntu wouldn't use default drivers which are for TV devices because this would not work well with osmocoms drivers. After we were done following Ranous's guide we rebooted the Raspi and plugged in our SDR dongle and started up CubicSDR. Instantly without modifying any settings our waterfall view looked like what it was on POP OS on laptop. After plugging in speakers and listening on different signals we could hear different music. 

![Waterfall on Xubuntu 20.10 on Raspi](https://github.com/Nikitushka/ProjectIcaros/blob/drafts/Reports/week8%269_SDR_testing/IMG_20210315_201318.jpg)

Our next mission is to figure out usage of different SDR softwares and how to enhance what we hear. After that we can move to figuring out how to continue the project in a way that we find out how to extract data from said software.
