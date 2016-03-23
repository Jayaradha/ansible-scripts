import time
import boto
import boto.ec2.elb
import boto.utils

def get_elb():
    elb_conn = boto.ec2.elb.connect_to_region(region_name='us-west-2')
    return elb_conn.get_all_load_balancers('botoelb')[0]

def elb_health():
	elb = get_elb()
	timeout = time.time() + 60*5 # 5 minutes
	while True:	
		health = elb.get_instance_health('i-afdb8d68')[0]
        	assert health.instance_id == 'i-afdb8d68'
        	assert time.time() < timeout
        	if health.state == 'InService':
           	 break
        	time.sleep(1)
	print 'Instance %s now successfully InService in ELB %s (took %d seconds)' % (instance_id, elb.name, time.time() - start)


elb_health()
