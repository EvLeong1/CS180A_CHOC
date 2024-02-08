# Meeting with Ms. Sayrs (CHOC Sponsor) - 2/8/24

## Meeting Notes

- currently in Trauma Bay after injury if a persons heart rate drops the machine starts beeping

- want to create shock index (pediatric adjusted shock index) (sipa)
	- need to calculate it quickly to be used in Trauma Bay
	- Linked through a sensor to your heart rate
	- want to understand shock with the parameters we have
	- feed in fake heart rate/ blood pressure data and demonstrate that it will *ding* at the certain cutpoints based on the sipa requirement
	- want relationship between shock and failure of the device
 
- PBRC = given blood
- SIPA
	- Shock Index Pediatric Adjusted

- hemoglobin down = bleeding out (above 7 is good, below not so good)

- parameters
	- 3 main parameters
		- blood given
		- sipa
		- hemoglobin
	- shock
	- max heart rate/ minimum distolic blood pressure (she will send formula)
	- weather or not they are given blood
	- each paramters has cutpoints per age
		 - 1.22 for baby is considered shock but not for toddler etc. 
	- hemoglobin ( if not stable above 7, take patient to the Operating Room)
	- relationship between the parameters will try to tell us if the patient is in shock 

- ct scan is a report saying whether or not a blush is found in the patient

- our task is to tell what the cutpoints, ex: how far can hemoglobin drop before we decide to do surgery? for the paramters

- impute hemoglobin data

## End Deliverables
### Nueral Network 
- Find cut points

### Device (Interface)
- Feed in data (age, heart rate, blood pressure) and it runs the cutpoints for shock
- Simple Interface
	- Enter parameters, beeps 
- Beeps when a patient meets shock criteria
- would eventually want to convert to a phsycial product 
		