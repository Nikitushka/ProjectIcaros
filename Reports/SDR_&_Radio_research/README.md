# How does SDR work?

## What is SDR? 

Software-defined radio (SDR) is a radio communications system where instead of having components implemented in hardware (for example mixers, filters, aplifiers, modulators and demodulators), they are implemented by means of software on your computer or another system. With SDR you can listen to many different broadcrasts and signals including broadcast stations, aircraft, HAM radios, weather services and many other services and broadcasts. SDR is fairly new technology that was very expensive at the beginning. At later date SDR has become fairly cheap since for commercial use there are multiple solutions to use SDR with less equipment. 

#### What do you need to operate SDR yourself?
You are going to need an antenna or multiple antennas that can listen to signals. You will also need the SDR receiver that can receive the actual transmission and then transfer the data to your last component that you need, which is a computer or another device that can run SDR software. For antenna and the receiver there are multiple choices ranging from cheap to very expensive hardware. There are also few websites where you can listen to SDR from web interface.


## How did radios work before SDR?
Radios have been around for a long time. You have been able to listen to your favourite radio stations for long time. Human ears cannot hear the frequenzy the radio is broadcasting, so how does the radio hear it and turn it into a noise that us humans can hear. This is where modulation and demodulation steps into the ring. The transmitter transmits the signal in a pure wave of constant frequency, which we call carrier wave. The carrier wave itself doesn't transmit data that has meaning to us such as speech. For us to be able to transmit speech, we need another wave on top of the carrier called input signal. This process where we impose the input signal on the carrier wave is called modulation. With modulation you can either modulate the amplitude of the carrier wave where you change the "height" of the signal so that it can contain the speech information or you can modulate the frequency (how often the current changes direction in a second) of the carrier. 

#### What is the difference with AM (Amplitude Modulation) and FM (Frequency Modulation)?
FM radio works basically the same way as AM radio does. The difference in these modulations are how the carrier wave is modulated or altered. With AM radio the amplitude of the signal is varied to incorporate the sound information. Where as in FM the frequency of the carrier signal is varied. 

## How does the digital radio work?
The important part of how we can digitize radios is ADC or analog to digital converter. This converter can as it says in the name convert analog signal into digital signal. The technical part about how humans have managed to turn analog signals to digital signals with cheap ADCs that have little processing power is called quadrature amplitude modulation (QAM). This method uses a phaseshift of 90 degrees to bend the theoritical negative frequencys to Q axis. Using QAM the carrier waves amplitude and phase are modulated and thereby this doubles the effective bandwitch. 


Sources:

- https://www.pbs.org/wgbh/aso/tryit/radio/radiorelayer.html#:~:text=The%20difference%20is%20in%20how,the%20carrier%20signal%20is%20varied.
- https://www.youtube.com/watch?v=xQVm-YTKR9s&t=253s
- https://en.wikipedia.org/wiki/Software-defined_radio
- https://www.electronics-notes.com/articles/radio/modulation/quadrature-amplitude-modulation-what-is-qam-basics.php
