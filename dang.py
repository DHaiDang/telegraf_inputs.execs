import subprocess
import re
print(1)
def health_check_services_inside_container(container_name, name_services):
	check_metrics = str(subprocess.check_output(['docker', 'exec', container_name, 'screen', '-ls']))
	if re.search( name_services, check_metrics ):
		return "Still_alive"
	else:
		return "Die"
print(1)
if __name__ == '__main__':
    print("CHECK_STATUS,status=" + health_check_services_inside_container("dangdh_ubuntu", "e962d98ef288"))
	#print("dang")

