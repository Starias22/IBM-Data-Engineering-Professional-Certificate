# Module 4: 

## Practice Project
touch rx_poc.log 
ls
echo -e  "year\tmonth\tday\tobs_tmp\tfc_tmp" > rx_poc.log 
cat rx_poc.log 

touch rx_poc.sh

echo "#! /bin/bash" > rx_poc.sh

chmod u+x rx_poc.sh

raw_data_file=raw_data_$(date "+%Y%m%d")
touch $raw_data_file

city=casablanca
curl wttr.in/$city -o $raw_data_file   #or --output



grep "°C"  $raw_data_file > temperatures.txt

obs_tmp=$(head -1 temperatures.txt | tr -s " " | xargs | cut -d " "  -f4)

echo $obs_tmp

fc_tmp=$(head  -3 temperatures.txt | tail -1 | tr -s " " | xargs | cut -d "C" -f2 | cut -d " " -f6)

echo $fc_tmp

hour=$(date -u "+%H")

echo $hour

day=$(date -u  "+%d")

echo $day

month=$(date -u  "+%m")
echo $month

year=$(date -u  "+%Y")

echo $year

echo -e  "$year\t$month\t$day\t$obs_tmp\t$fc_tmp">> rx_poc.log 

cat rx_poc.log 

date

date -u

date -u

![alt text](image.png)

System time is 4 hours behind Universal Time
Casablanca is UTC+1 so 12h at Casablanca is 11h AM UTC; 11-4=7
So 12h at Casablance is equivalent to 7H AM in our system


```sh
#! /bin/bash
# Create the raw data file
raw_data_file=raw_data_$(date "+%Y%m%d")
touch $raw_data_file

# Download the raw data into a file
city=casablanca
curl wttr.in/$city -o $raw_data_file 

# Store the temperatures into a file
grep "°C"  $raw_data_file > temperatures.txt
# Store observed temparature and forcast temperature
obs_tmp=$(head -1 temperatures.txt | tr -s " " | xargs | cut -d " "  -f4)
fc_tmp=$(head  -3 temperatures.txt | tail -1 | tr -s " " | xargs | cut -d "C" -f2 | cut -d " " -f6)

# Store current hour, day, month and year
hour=$(date -u "+%H")
day=$(date -u  "+%d")
month=$(date -u  "+%m")
year=$(date -u  "+%Y")

# Append the data to the logfile
echo -e  "$year\t$month\t$day\t$obs_tmp\t$fc_tmp">> rx_poc.log
```

crontab -e

```sh
# m h  dom mon dow   command
  0 7   *   *   *     /home/project/rx_poc.sh
```

## Reading: Cheat Sheet: Linux Commands and Shell Scripting
[Cumulative Cheat Sheet - Hands-On Introduction to Linux Commands and Shell Scripting](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTVNraWxsc05ldHdvcmstTFgwMTE3RU4tZWRYL2xhYnMvTTRfQ3VtdWxhdGl2ZV9DaGVhdF9TaGVldF9lZFgucGRmLm1kIiwidG9vbF90eXBlIjoiaW5zdHJ1Y3Rpb25hbC1sYWIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcxMTYzODYzOH0.ziNAtnS2Kt0XG5g9eP-NXikeWrrbJrIxGu8MkQBfojg)


wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/backup.sh


![alt text](./resources/15-executable.png)    

wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/important-documents.zip

unzip -DDo important-documents.zip

touch important-documents/*

![alt text](./resources/16-backup-complete.png)

![alt text](./resources/17-crontab.png)

