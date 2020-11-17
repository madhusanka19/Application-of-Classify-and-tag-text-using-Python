#Name      : Madhusanka W.W
#IT Number : IT17087216

import os

path= input(" Enter the file path ")

try:  
    os.chdir(path)
    print("Directory changed")
except OSError:
    print("Can't change the working Directory")
files = os.listdir(path)

arr = ["Document Name    ","  Tags attached"]
keyword = 'Cryptographic private keys'
keyword2 = 'cardholder name'
keyword3 = 'service code'
keyword4 = 'Expiration code'
keyword5 = 'PIN'
keyword6 = 'Social security number'
keyword7 = 'Student number'
keyword8 = 'Name of the student'

keyword9 = 'Financial Account Number'
keyword10 = 'Medical information'
keyword11 = 'Health information'
keyword12 = 'State-Issued'

keyword13 = 'Account Numbers'
keyword14 = 'Certificate licence number'
keyword15 = 'URL'
keyword16 = 'Fax Number'
x=0
for file in files:
    if os.path.isfile(file):
        f=open(os.path.join(path,file),'r')
        arr.append(file)
        
        for x in f:
            if keyword in x:
                              
                arr.append('AV')

            #---------------------------------------------------------------------------------------    
            if keyword2 in x or keyword3 in x or keyword4 in x or keyword5 in x:
                
                arr.append('PCI')

            #---------------------------------------------------------------------------------------        
            if keyword6 in x or keyword7 in x or keyword8 in x:
                
                arr.append('PIER')
                
            #---------------------------------------------------------------------------------------    
            if keyword9 in x or keyword10 in x or keyword11 in x or keyword12 in x:
                
                arr.append('PII')
                
            #---------------------------------------------------------------------------------------    
            if keyword13 in x or keyword14 in x or keyword15 in x or keyword16 in x:
                
                arr.append('PHI')

x = 0
line = ""
for i in arr:
    x+=1
    line += "%s " % i
    if not x%2:
        line += "\n"

print(line)


      
