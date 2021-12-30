'''
a = 20
b = 30

print(a+b)
'''
'''
a = 1
print(type(a))

b = 'Akash'
print(type(b))

c = 10.30
print(type(c))

a = 10
d = a+10j
print(type(d))
'''

#---------- function ---------------------
'''
def add():
    print(10-20)

add()



def a():
    print("today we leaarn about function")
    def today():
        print("this is second function")
    today()
    
a()

'''
#------------parametrised function and non-parameterised function-----------


'''
def m1():
    print(10+20)    #non - parametrised function
m1()



def m1(x,y):
    print(x+y)      #parametrised function
m1(10,20)




var = int(input("enter number"))

a=10
b=var
x = a+b
print(x)



a = int(input("enter value for a :"))
b = int(input("enter value for b :"))


def ab(a,b):
    print(a-b)
ab(a,b)






queue = ["Amar", "Akbar", "Anthony"]
queue.append("Ram")
queue.append("Iqbal")
print(queue)
  
# Removes the first item
print(queue.pop(1))
  
print(queue)
  
# Removes the first item
print(queue.pop(1))
  
print(queue)

'''

#Antivirus is generating system logs with the following format.
'''
SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1


Write a program to take the above string as an input and provide the following output as a dictionary

{
    cat: C2,
    cs1Labelsubcat,
    cs1: DNS_TUNNELING,
    cs2Label: vueUrls,
    cs2: https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650,
    cs3Label: Tags,
    cs3: USA,Finance,
    cs4Label: Url,
    cs4: https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323,
    cn1Label: severityScore,
    cn1: 900,
    msg: Malicious activity was reported in CAAS\=  A threat intelligence rule has been automatically created in DAAS.,
    dhost: bad.com,
    dst: 1.1.1.1
}
'''

log = "SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1"
l1 = log.split('|')
#print(l1)

d1={}
for ele in l1:
    if '=' in ele:
        l2 = ele.split()
        for ele in l2:
            if '=' in ele:
                l3 = ele.split('=')
                k = l3[0]
                v = l3[1]
                d1[k]=v


print(d1)


























