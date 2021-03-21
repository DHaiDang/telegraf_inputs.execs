import os
import subprocess
import re

def health_check_services():
    #check_services = str(os.system("screen -ls"))
    #print("day ra"+check_services)
    check_services = str(subprocess.check_output(['screen','-ls']))
    #print("hello "+str(check_services))
    if re.search("services_1",check_services) and re.search("services_2",check_services):
        return("services_1 and services_2")
    if re.search("services_1", check_services) or re.search("services_2", check_services):
        return re.search("services_1", check_services) if "services_2" else "services_1"
    else:
        return None
#def check_container_running():

if __name__ == "__main__":
    check_services = str(health_check_services())
    print("inside " + check_services)
    if(check_services == None):
        logs = "Checkservices,Services_1={service1}, Services_2={service2}"
        print (logs.format(service1=1,service2=0))
    else:
        logs = "Checkservices,Services_1={service1}, Services_2={service2}"
        print (logs.format(service1=1,service2=0))