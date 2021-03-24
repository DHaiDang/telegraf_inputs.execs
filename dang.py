from influxdb import InfluxDBClient
import uuid
import random
import time
import subprocess
import re
from datetime import datetime

def health_check_services_inside_container(container_name, name_services):
	# check_metrics = str(subprocess.check_output(['docker', 'exec', container_name, 'screen', '-ls']))
	check_metrics = "e962d98ef288"
	return 1 if re.search(name_services, check_metrics) else 0

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('lolo')

measurement_name = 'dagntest2'
number_of_points = 250000
data_end_time = int(time.time() * 1000)
times = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
status = health_check_services_inside_container("dangdh_ubuntu", "e962d98ef288")

data = []
data.append("{measurement},status={status},lastcheck={lastcheck} code={code},timecheck={timecheck} {timestamp}"
	.format(measurement=measurement_name,
		status="status",
		code=status,
		lastcheck="lastcheck",
		timecheck = 2,
		z=random.randint(0,50),
		timestamp=data_end_time))
current_point_time = data_end_time
for i in range(number_of_points-1):
	current_point_time = current_point_time - random.randint(1,100)
	data.append("{measurement},status={status},lastcheck={lastcheck} code={code},timecheck={timecheck} {timestamp}"
		.format(measurement=measurement_name,
			status="status",
			code=status,
			lastcheck="lastcheck",
			timecheck = 2,
			z=random.randint(0,50),
			timestamp=current_point_time))

client_write_start_time = time.perf_counter()
client.write_points(data, database='lolo', time_precision='ms', batch_size=10000, protocol='line')
client_write_end_time = time.perf_counter()

#print("TimeLock,time_field=time time={time}s".format(time=client_write_end_time - client_write_start_time))
