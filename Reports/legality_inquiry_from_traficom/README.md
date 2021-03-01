# Intro
This document is the result of the exchange we had with Traficom during our inquiry for Finnish regulations on the legality of our project concerning frequency listening/recording and analysis/decoding. The exchange is originally in finnish, but the relevant parts are translated to English.

Initially we contacted a finnish ISP, DNA, if they could help us with our questions or refer us somewhere, with them later forwarding us to a Traficom contact form.

# The exchange in Finnish (Original)

## Lähettämämme sähköposti Traficomille
Hei! Tarvitsemme apua/neuvoa meidän tänä keväänä toteutettavan projektimme laillisiin rajoihin.

Lyhyesti projektistamme:

Olemme neljän henkilön tiimi Haaga-Heliasta ja tämän lukukauden aikana teemme ICT projektia SDR-radioon liittyen.

Projektimme lopputulos on tehdä Raspberry Pi:tä, LDR-SDR antennia (ohjelmistoradio) ja monitoroivaa (sekä mahdollisesti injektoivaa) verkkokorttia käyttävä prototyyppi, joka pystyisi kuuntelemaan sekä kartoittamaan (siis kartalle) erilaisia langattomia signaaleja. Tämän prototyypin avulla tahdomme tehdä tutkimusta, jonka lopputuloksena olisi tuoda kaikki keräämänne tieto järkeväksi kokonaisuudeksi käyttäen myös meidän omia komponentteja.

Koska suuri osa tästä projektista koskee tietoturvaa ja sen tutkimista, on meille erittäin tärkeää selvittää eettisten rajoitteiden lisäksi myös lailliset rajoitteet ja tähän liittyen koostimme teille muutaman kysymyksen, mihin toivottavasti saisimme teidän kautta vastauksia.

1. Onko olemassa joitain taajuksia/kaistoja, mitä suomen telekommunikaatiolainsäädännön mukaan ei saisi kuunnella/äänittää tai lähettämää tietoa saa analysoida/purkaa.

2. Mitä mahdollista tietoa langattomista lähettimistä ja niiden lähettämästä tiedosta (esimerkiksi laajakaista, mahdolliset muut langattomat lähettimet esim. ostoskeskuksessa) ei saa avoimesti julkaista internetiin esimerkiksi kartalle tietoineen?

3. Onko jotain muuta mitä meidän pitäisi pitää mielessä/varoa projektin aikana?

Kiitos paljon ajastanne ja avusta näihin lakiin liittyviin kysymyksiin, onko se teille OK, että laitamme kiitokset Traficomille avustuksesta nettisivullemme/blogiimme?

## Vastaus
Hei,

Alla vastauksia kysymyksiinne.

1) Sähköisen viestinnän luottamuksellisuutta käsitellään sähköisen viestinnän palveluista annetun lain https://www.finlex.fi/fi/laki/ajantasa/2014/20140917) pykälässä 136. Pykälässä todetaan että radioviestintä on lähtökohtaisesti luottamuksellista paitsi ne erikseen luetellut liikennelajit, joita luottamuksellisuus ei koske. Mitään erikseen tehtyä jakoa taajuusalueittain ei tässä tai muualla luottamuksellisuuden suhteen ole tehty. Radioviestinnän luottamuksellisuushan ei sinänsä estä viestinnän kuuntelua tai jopa tallentamista omaan käyttöön, mutta viestinnän sisältöä ei saa käyttää hyväksi tai ilmaista ilman viestinnän osapuolten suostumusta.

2) Nähdäkseni mikään ei estä yleiseen käyttöön tarkoitettujen lähettimien, kuten matkaviestintukiasemien tai suurta yleisöä palvelevien WLAN-tukiasemien, sijaintiteitojen taajuuksien, lähetyskeilojen suuntien tms. julkaisemista. Nämä tiedothan eivät ole viestinnän sisältö- tai välitystietoja.  Esimerkkejä tällaisesta toiminnasta on vaikka harrastelijodien eri sivuille, kuten [http://www.cellmapper.net,]www.cellmapper.net, keräämät tiedot matkapuhelintukiasemista.

3) Eipä muuta tule mieleeni kuin tuo sähköisen viestinnän palveluista annetun lain pykälä 136 tai oikeastaan koko lain osa VI, viestinnän  luottamuksellisuus ja yksityisyyden suoja. Ne kannattaa lukea läpi ajatuksella. 

En ole itse koulutukseltani lakimies vaan ihan puhtaasti insinööritaustainen. En siis osaa ottaa kantaa monimutkaisiin juridisiin kysymyksiin, mutta välitän ne toki tarvittaessa lakimiehillemme vastattaviksi

# Exchange in English

## Initial email from us

Hello! We need help/advice concerning the legal boundaries of our project implementation during this spring

Shortly about our project:

We are a team of four people from Haaga-Helia and during this semester we are working on a project working with SDR.

The end result of our project is to create a prototype utilizing Raspberry PI, an LDR-SDR antenna ja a network card with the capabilities to monitor (and possibly inject) -
that could listen to and map (on an actual map) different types of wireless signals. With this prototype we would like to do research, with the end result being us bringing
the information we collected into a coherent whole.

Because a big chunk of this project is concerned with information security, it is of utmost importance to us to research legal boundaries along with the ethical ones.
With this we have assembled a set of questions, with which we hope that we will receive answers through you.

1. Are there frequencies/tracks, that we cannot listen to/record or analyse/decode according to the Finnish Telecomunnications Law?

2. What possible information from wireless transmitters and information transmitted by them (for example a router, other possible wireless trasmitters for example in a mall)
can we not openly publish on the internet, for example on a map with additional information?

3. Is there something else that we should keep in mind/be careful of during our project?

Thank you very much for your time and help with these legal questions, is it OK for you if we publish a thank you to Traficom for your help on our website/blog?

## The Response

Hello,

Below are the answers to your questions.

1) The confidentiality of electronic communication service law are dealt with https://www.finlex.fi/fi/laki/ajantasa/2014/20140917 section 136. In that section it is concluded, that 
radio communication is confidential, with exception to the types of traffic that are not confidential. Any specific divide in frequency in areas are not made here or anywhere else in terms of confidentiality. The confidentiality of radiocommunication in itself does not prohibit listening or saving for personal use, but the contents of the communication cannot be used or expressed withat the agreement of the communicating side.

2) As far as I can see nothing prohibits the publishing of transmitters meant for public usage, like mobile base stations or WLAN base servicing a big userbase, location information frequencies, transmission beam directions, etc.

3) Nothing else comes to mind other than the section 136 of electronic communication law or whole part VI, confidence in communication and the protection of privacy. Those should be read with care.

I have an engineering background and I'm not a lawyer by education so I cannot help you with complicated juridical questions, but I ofcourse can forward them to our lawyer to be answered.
