import subprocess
import re
from datetime import datetime
import logging

def health_check_services_inside_container(container_name, name_services):
    check_metrics = str(subprocess.check_output(['docker', 'exec', container_name, 'screen', '-ls']))
	# print(re.search(name_services,check_metrics))
	if re.search(name_services, container_name):
		log = "/var/log/telegraf/log_telegraf.log"
		logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
		logging.info('Log file.')
		return 0
	else:
		return 1

if __name__ == '__main__':
    current_time = str(datetime.now().strftime("%d/%m/%Y_%H:%M:%S"))
    check_services = str(health_check_services_inside_container("dangdh_ubuntu", "e962d98ef288"))
	print('Check,status='+check_services+',author=dang')