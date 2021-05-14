import csv

# take in latitude and longitude and return a list containing frenquency and strength dictionaries
def csv_parse(lat, lon):
	with open("./output/sdr.csv", newline='', mode="r") as log:
		csv_reader = csv.reader(log, delimiter=",")
		line_count = 0
		result = {"lat": lat, "lon": lon}
		out = []
		for row in csv_reader:
			freq_low = float(row[2])/1e6
			freq_high = float(row[3])/1e6
			freq_step = float(row[4])/1e6
		
			# Iterate over dB values on one line:
			for idx, dB in enumerate(row[6:]):
				line_count += 1
				# Write frequency db pair if db more than -12:
				if float(dB) > -12:
					freq = freq_low + idx * freq_step
					result.update({"sdr_frequency": freq})
					result.update({"signal_strength": dB})
					out.append(dict(result))
	return out

# take in latitude and longitude and return a list containing security & SSID
def wifi_parse(lat,lon):
	with open("./output/wifi_out", mode="r") as log:
		result = {"lat": lat, "lon": lon}
		out = []
		discard = ["IN-USE", "BSSID", "BARS", "MODE", "SIGNAL", "CHAN", "RATE"] # keys we skip
		count = 0
		for line in log:
			if "IN-USE" in line and count > 0: # when the next 'IN-USE' key after the first one is encountered, append the dict into the output list
				out.append(dict(result)) 
			elif any(bad in line for bad in discard): # if the keys declared in the list are encountered, proceed to the next line without doing anything
				continue
			else:			
				key, value = line.split(':')
				result.update({key: value.strip('\n')})
				count += 1
	return out

