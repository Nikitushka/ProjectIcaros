# Introduction
This document serves as an index of different types of competitors we have in terms of mapping radiotransmitters and signals.

The criteria for being selected as a "competitor" are google queries containing "sdr map", "radio transmitter map" and "wireless signal map".

Specific keywords will be **boldened** and explained at the bottom, in the glossary. 

# Competitors:
## [fmscan](https://fmscan.org/)
#### [From fmscan's help page:](https://fmscan.org/help-en.htm "FMSCAN  - frequencies for any place and transmitter maps")
_The FM band looks different wherever you go._

_If you only a move into the next city there will be different stations on other frequencies. FMSCAN can calculate what to expect. It's a free tool.
Whether you just want to take a closer look at your stations at home or you are about to travel some distant spot - this tool helps to explore FM and AM radio._

#### _Transmitter maps_
_The Network Maps section makes it easy to find frequencies of a specific station if you're moving through a certain area. This has been automatized with the **RDS** technology. But RDS often fails with weaker stations. Setting the frequency manually might deliver you many more stations than **RDS** would find._

#### _FMLIST - the world-wide frequency database_
_Part of the data come from public sources. In addition to that FMLIST includes many observations from people who like to listen to distant stations (DXers). These hobbyists are also the most intense users of the database. Combining all this information makes FMLIST unique. In Southern Europe for example you won't gain much from the official sources. FMLIST has become very comprehensive over the years. Günter Lorenz started the FMLIST project in Germany in the late 80ies. FMSCAN and FMMAP have been on the internet since 2000._

The map feature only shows radio towers, but clicking on said towers on the map can display which radio stations and frequencies are broadcasted from them.

![fmscan map](https://github.com/Nikitushka/ProjectIcaros/blob/drafts/Reports/competitor_mapping/images/fms_1.jpg)

## [CellMapper](https://cellmapper.net/map "Cellular Tower and Signal Map")
#### [From CellMapper's FAQ:](https://cellmapper.freshdesk.com/support/solutions/articles/28000006999-what-is-the-cellmapper- "What is the CellMapper? : CellMapper")
_CellMapper is Cellular Coverage Map application. On CellMapper Map you can check your own provider mobile network coverage. Also you can see your provider mobile tower locations on map._

The map itself displays different **air interfaces** and network coverage for 2G, 3G, 4G and 5G networks for providers world-wide. The UI also provided possibilities to search for locations, towers, **BSIC** (Base Station Identity Code), **PCI** (Physical Cell ID), **PSC** (Primary Scrambling Code), along with applying different filters for searching.

![CellMapper map](https://github.com/Nikitushka/ProjectIcaros/blob/drafts/Reports/competitor_mapping/images/CellMapper_1.jpg)

Upon selecting an **air interface**, different information on said **air interface** can be viewed:

![Air Interface Information](https://github.com/Nikitushka/ProjectIcaros/blob/drafts/Reports/competitor_mapping/images/CellMapper_2.jpg)

## [KiwiSDR](http://kiwisdr.com/ "KiwiSDR: Wide-band SDR + GPS cape for the BeagleBone Black") [Map Section](http://rx.linkfanel.net/ "Wideband shortwave radio receiver map")

The KiwiSDR website offers a Map section, which shows different KiwiSDR receivers around the world users can connect to:

![KiwiSDR map](https://github.com/Nikitushka/ProjectIcaros/blob/drafts/Reports/competitor_mapping/images/KiwiSDR_1.jpg)

Once an SDR has been selected, a user can use this receiver to tune in to different frequency ranges and listen to incoming signals to that SDR, along with recording capabilities.

![SDR](https://github.com/Nikitushka/ProjectIcaros/blob/drafts/Reports/competitor_mapping/images/KiwiSDR_2.jpg)

So technically, while KiwiSDR has the SDR map capability, it is only reserved for KiwiSDR's that are open to establish a connection to.

# Glossary

**RDS** = RDS or Radio Data System is standard on most car radios and hi-fi tuners today. RDS is used on VHF FM radio broadcast transmissions and provides a number of facilities that are of great use to all radio listeners, but particularly to those radio listeners in cars. RDS enables traffic reports to be received more easily, and provides many facilities including enabling the radio station name to be displayed on the radio display. Source: [electronics-notes.com](https://www.electronics-notes.com/articles/audio-video/broadcast-audio/rds-radio-data-system-basics-tutorial.php "Radio Data System, RDS Tutorial » Electronics Notes")

**air interface** = _In cellular telephone communications, the air interface is the radio-frequency portion of the circuit between the cellular phone set or wireless modem (usually portable or mobile) and the active base station._ Source: [searchmobilecomputing.techtarget.com](https://searchmobilecomputing.techtarget.com/definition/air-interface#:~:text=In%20cellular%20telephone%20communications%2C%20the,and%20the%20active%20base%20station.)

**BSIC** = The Base Station Identity Code (BSIC) is a code used in GSM (The Global System for Mobile communications - a wireless telecommunications standard) to uniquely identify a base station. The code is needed because it is possible that mobile stations receive the broadcast channel of more than one base station on the same frequency. This is due to frequency re-use in a cellular network. Source: [Telecom ABC](http://www.telecomabc.com/b/bsic.html "BSIC - Base Station Identity Code - Telecom ABC") 

**PCI** = Physicall Cell ID's are used in E-UTRA systems to identify a cell. Its value is dependant on the combination of PSS (Primary Synchronization Signal), numbered 0 to 2 and the SSS (Secondary Synchronization Signal) numbered 0 to 167. This effectively allows for 504 combinations which are reused in the cell planning and optimization phases. The PCI value can be reused within the network and different radio carriers on the same eNB can also reuse the same PCI. Source: [MPRICIAL.com](https://www.mpirical.com/glossary/pci-physical-cell-identity "PCI - Physicall Cell Identity")

**PSC** = Scrambling Codes are used to identify and distinguish cells from one another in WCDMA networks. These SCs are reported by the mobile users to the network to declare which cells they are able to connect to. Source [Institute of Electrical and Electronics Engineers / IEEE Xplore, Scrambling code planning and optimization for UMTS system, Abstract](https://ieeexplore.ieee.org/document/6952571 "Scrambling code planning and optimization for UMTS system - IEEE Conference Publication")
