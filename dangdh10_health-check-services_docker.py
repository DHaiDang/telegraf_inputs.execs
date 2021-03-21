import subprocess
import re
from datetime import datetime


def health_check_services_inside_container(container_name, name_services):
    check_metrics = str(subprocess.check_output(['docker', 'exec', container_name, 'screen', '-ls']))
	# print(re.search(name_services,check_metrics))
	return 1 if re.search(name_services, check_metrics) else 0

if __name__ == '__main__':
    current_time = str(datetime.now().strftime("%d/%m/%Y_%H:%M:%S"))
    check_services = str(health_check_services_inside_container("dangdh_ubuntu", "e962d98ef288"))
	print('Check,tag1='+check_services+',tag2='+current_time+' i=dangdh')



# from datetime import datetime
# current_time = datetime.now().strftime("%d/%m/%Y_%H:%M:%S")
# print('Check,tag1=a,tag2='+str(current_time)+' i=42i')