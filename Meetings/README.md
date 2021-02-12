# Note:
These meeting notes are all done in finnish.

## 25.1.2021

Hacking RIG

Toivottuja ominaisuuksia:

  * Joko Raspberry Zero, tai Pi 4
  * Multitool (softaradio, kartoitus, WiFi)
  * Remote access (SSH)
  * Stealth (???)
  * SaltStack konfiguraatio (masterilta konffin droppaus)
  * 3D-tulostettu case
  * SDR (Kysytään Terolta)
  * IOT
  * RFID hacking
  * Sneaky front-end (ja back-end tietysti)
  * Testaus? How do I...?

Kysytään Teron inputtia. Softaradiosta selvitys, mitä kannattaisi duunata sen kanssa, mikä scope (yksittäinen spesifi kaista vs. 200MHz leveudeltä dataa).

SDR vaatii antennin, sekä jonkin rajapinnan keskusteluun. Mikä frontti? Ulkoinen vai integroitu näyttö.

## 27.1.2021

Teron input:
* Ytimen ja teeman rakennus/tarkennus.
* Rasp3 hyvä vaihtoehto ettei lämpene liikaa.
* Suositteli tilata LDR-SDR asap
* HACK-RF
* Taajuudet riippuu softasta: suositteli gqrx:ää. gnuradio, mut ei kuulemma nii kiva. pysdr "näytti hyvältä" joten terolla ei siis salee oo tän suhteen kokemusta
* monitorointi & injektointi verkkokortti
* https://projectintrusion.wordpress.com/ => wifihyökkäyksiä/rautaa varten
* wireguard tai openvpn takaovea varten, suositteli enemmän wireguardia


* **kartta keskiöön**
* kännykkäpaikannuksen hyödyntäminen
* etäisyyksien laskeminen verkkoja varten? suositteli tutkia
* avoin rajapinta
* maastokartat kuulemma aika kova => kansalaisen karttapaikka, ei tarvii enää lupii + ilmainen
* ehkä saadaan esimerkkiä Teron vihamielisestä etähallintajärjestelmästä

Tero painotti että kartta vois olla hyvä sitova ominaisuus kaikelle

Perjantaina 29.01.2021 voi tavata jitsissä 9-10 jos tarvii jelppii
* Pitäs kävästä kysyy et miten sponssaus toimii rautaa varten

Oma miitti Jitsin jälkee about 12 jälkeen

## 29.1.2021

@The_Elmo#2894 @aksuiivari#9336 kävi jitsissä, jotai laitteita saa, mut se on auki että mistä ja miten niitä tulee
Koulu ei myöskään tarjoo mitään rahaa, mut yhteistyökumppanien kautta saa tod näk jonku sponsorship dealin.

Pöytäkirjan aloitus, laitettii jäätävästi matskuu #materials channelii ja shitpostattii sellaset 3 tuntii

Nähdään w05 keskiviikkona 2021-02-03 kello 14:15. Projektisuunnitelmien viime hetken tarkastelu ennen esityksiä.

Ens kerta ma 1.2. klo 14 

## 5.2.2021

Esitettiin projektisuunnitelma

Teron huomiot:
* Lisenssit
* Jatkuva julkaisu asap
* Pitää ottaa kantaa etiikkaan
* Lainsäädännön selvittäminen
* Kannattaa mainostaa
* Mitä tää on? Red teaming emulation vai nykyisen "radiomaailman" selvittämistä
* Vihdoin tuli palaute: => dropbox vittuun =>
* Signaalien analysointi ja automaattinen lajittelu 
* !HOX! POTENTIAALIA HELSECIIN !HOX!
* erillisiä artikkeleita ongelmista ja niiden ratkaisuista (this weeks problems - blog) tyyppinen?

Ens kerta ma 8.2.2021 14 eteenpäin servulassa

Teron kanssa nähdään Ke 10.2. 14:15 jitsissä

## 8.2.2021 Servola
installed kali image with rufus and usb
input/output error, kuinka solvasimme: reformat, repartition and reinstall the image

built-in monitor incompatible with kali

4h/nuppi äbout

## 10.02.2021 jitsi
sudo smartctl -a /dev/sda # pystyy kattoo lisäinfoo toho i/o errorii liittyen
nmcli dev wifi # näyttää lähellä olevat asemat
t. tero

dokumentit kilpailijoista ja web-sdr:stä

TERO: "KIRJOTTAKAA KAIKKI YLÖS"

wifi - preferred network tai wifi kortti hommii

conclusions: täl viikol vois dokumentoida (vähintää lyhyesti) mitä kilpailijoita löytyy yms 

teron avainsana karttaa varten: interpolointi

offline - openstreetmap-kansalaisen karttapaikka

http://terokarvinen.com/2012/getting-started-with-openlayers-and-openstreetmap/

## TAPAAMINEN 10.02.2021

Tapaamisessa käytyjä asioita:

  * Raportointi kaikesta: ongelmatilanteet, niiden ratkaisu, asioiden selvitykset
  * Raportoinnin julkaisu: WordPress, GitHub. 


Seuraavie työvaiheita viikolle 6:

  * Wordpressiin artikkeli (kuvia, aiempien ongelmatilanteiden kuvaus jne.) Tommi otti vastuun
  * GitHubin pystyttäminen ja sinne tavaran puskeminen. Aki otti selvitettäväkseen Gitin pystyttämisen
  * Karttasovellusten, sekä rajapintojen selvitys ja kokeilu. Elmo kokeilee settejä virtuaalikoneilla ja läppärillä.
  * Trellon mahdollinen pystytys työnjakoa ja seurantaa varten.

Kukin työstää itse tai muiden kanssa ja kirjoittelee muistiinpanoja/raportteja tapahtumista.

### Komentoja

smart
sudo smartctl -a /dev/sda
$ nmcli dev wifi

### KARTTOIHIN LIITTYVÄÄ

https://asiointi.maanmittauslaitos.fi/karttapaikka/ (offline)
openstreetmap (online)
http://terokarvinen.com/2012/getting-started-with-openlayers-and-openstreetmap/
