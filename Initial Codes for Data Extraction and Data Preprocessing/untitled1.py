# -*- coding: utf-8 -*-
   
   

import wget

map1={
 "17":"ARIYALUR",
"2":"CHENNAI",
"12":"COIMBATORE",
"18":"CUDDALORE",
"5":"DHARMAPURI",
"13":"DINDIGUL",
"10":"ERODE",
"3":"KANCHEEPURAM",
"30":"KANNIYAKUMARI",
"14":"KARUR",
"24":"MADURAI",
"19":"NAGAPATTINAM",
"9":"NAMAKKAL",
"16":"PERAMBALUR",
"22":"PUDUKKOTTAI",
"27":"RAMANATHAPURAM",
"8":"SALEM",
"23":"SIVAGANGA",
"21":"THANJAVUR",
"25":"THENI",
"11":"THE NILGIRIS",
"1":"THIRUVALLUR",
"20":"THIRUVARUR",
"28":"THOOTHUKKUDI",
"15":"TIRUCHIRAPALLI",
"29":"TIRUNELVELI",
"6":"TIRUVANNAMALAI",
"4":"VELLORE",
"7":"VILUPPURAM",
"26":"VIRUDHUNAGAR"
   }
print(map1["1"])
print(len(map1))
for i in range(1,31):
    str1=map1[str(i)]
    url="https://www.indiawaterportal.org/met_data/data/csv/33/"+str(i)+"/1/1952/2002"
    url2="https://www.indiawaterportal.org/met_data/data/excel/33/"+str(i)+"/1/1952/2002"
    #wget.download(url ,str1+".csv")
    wget.download( url2 , str1+".xls" )  
#print(results.text)