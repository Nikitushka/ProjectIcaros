We started the creation of our SDR mapping application by planning the parts we need.
The toughest part was to plan our database and to find the information we needed to store.
The database was planned to be iplemented with postgresql.
It should atleast have tables for SDR data and Wifi data.

SDR should have:

* signal
* signal strength
* location (Long,Lat)
* possible name

Wifi should have:

* SSID
* location (Long,Lat)
* wifi strenght
* Protection 

These to tables together need to create a third table.

Nikita started the backend creation of the project by also installing the postgresql to our raspberry pi.
As I haven't used the postgresql before I started by installing it on my own virtual box.
This way I could also test and learn how to do things first.
To start working with the postgreSQL you first need to install it. I followed the official document's for the installation.

On a later date the group had a meeting and we discussed more about the database structure. 
We talked about the amount of tables needed and confirmed that all could be done with one but we decided to use two.
In the meeting we also discussed what data we wanted on the database.
The following is the list we started to make the database tables with.

SDR:

* Scan id
* Signal strength
* Frequency
* Longitude & Latitude
* modulation

WIFI:

* Scan id
* SSID & BSSID
* Signal strength
* Longitude & Latitude
* Encryption

Creating the database started with the following command, which creates the database for the selected user in postgresql.
* CREATE DATABASE icaros;
To create the tables we use the CREATE TABLE command, which we will type as such.
* CREATE TABLE sdr (scan_id INT PRIMARY KEY, strength int, frequency numeric, lon numeric, lat numeric, modulation varchar(4));
* CREATE TABLE wifi (scan_id INT PRIMARY KEY, SSID varchar(40), BSSID varchar(40), strength int, lon numeric, lat numeric, encryption varchar(80));

Now we have our first tables we can use to do testing for our mapping app. Now we need to input some data. Nikita found a way we can get sdr data in csv format so we will be taking a look at it in our next meeting.
