# KNEC KCSE School Results Checker
A python automation script that uses the school code of a school to brute force the KNEC servers to yield the grades of everyone in the whole school

## V1
The school code is hard coded alongside the range of index numbers needed.

## Schools available
- OUR LADY OF MT.CARMEL MARYHILL GIRLS HIGH SCHOOL
- ST.CLARE GIRLS' SECONDARY-ELBURGON
- MOI GIRLS' SCHOOL NAIROBI
- THE KENYA HIGH SCHOOL
- NAIROBI SCHOOL
- LENANA SCHOOL
- KAREN ' C ' SECONDARY   SCHOOL
- MOI GIRLS' HIGH SCHOOL- ELDORET
- ALLIANCE HIGH SCHOOL
- ALLIANCE GIRLS HIGH SCHOOL

## Dependencies
Esnure you have Python installed. I used Python 3.11.5 for on the machine I executed the code on.

```
Python 3.11.5
```

Install selenium

```
pip install selenium
```

By default selenium obtains the webdriver needed provided you have version 4.6 and later.

## Feature Requests
- Asynchronous handling
- Conversion to .xlsx rather than .txt upon completion for Data Analysis
- Support for MacOS
- Support for Windows 10
- Support for Chrome
- Support for Edge
- Migration to Mojo to minimise overhead and utilisation of the GPU instead of the CPU

## All Hardware Configurations That Have Run It

The machine below ran very hot and could only execute only one instance efficiently.

```
Processor	12th Gen Intel(R) Core(TM) i7-1250U   1.10 GHz
Installed RAM	16.0 GB (15.7 GB usable)
Opearating System Windows 11 Home (23H2)
Graphics card Intel(R) Iris(R) Xe Graphics
Storage SK Hynix BC& HM512GD£JX013N 512 GB
Python Version 3.11.5
```

The machine below ran really well. RAM was well economised. There was asynchronous handling of the requests when the script was ran in two instances on the same machine.

```
Processor 10th Gen Intel(R) Core(TM) i7-10700  2.90 GHz
Installed RAM 8.0 GB
Operating System Ubuntu 22.04 LTS
Graphics card Mesa Intel(R) UHD Graphics 630 (CML GT2)
Storage SSD 2.0 TB
Python Version 3.10.12
```


