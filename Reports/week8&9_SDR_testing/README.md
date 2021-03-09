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

### Research on RTL-SDR and how it works with Gqrx

