import subprocess

def health_check_services_inside_container(container_name):
    sub_command_check_1 = 'pwd'
    sub_command_check_2 = ''
    check_metrics = subprocess.check_output(['docker', 'exec', container_name, sub_command_check_1, sub_command_check_2])

    # if re.search("services_1",check_services) and re.search("services_2",check_services):
    #     return("services_1 and services_2")
    # if re.search("services_1", check_services) or re.search("services_2", check_services):
    #     return re.search("services_1", check_services) if "services_2" else "services_1"
    # else:
    #     return None
    return str(check_metrics)

if __name__ == '__main__':
    check_services = health_check_services_inside_container("dangdh_ubuntu")
    logs = "Checkservices,Pwd_directory={service1}"
    print(logs.format(service1=check_services))
    # if(check_services == None):
    #     logs = "Checkservices,Services_1={service1}, Services_2={service2}"
    #     print (logs.format(service1=1,service2=0))
    # else:
    #     logs = "Checkservices,Services_1={service1}, Services_2={service2}"
    #     print (logs.format(service1=1,service2=0))

