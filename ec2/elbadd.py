import time
import boto
import boto.ec2.elb
import boto.utils
import sys

def get_elb():
    elb_conn = boto.ec2.elb.connect_to_region(region_name='us-east-1')
    return elb_conn.get_all_load_balancers('boto')[0]

def add_this_instance_to_elb():
	elb = get_elb()
	elb.register_instances(sys.argv[1])
        print 'adding %s from ELB %s' % (sys.argv[1], elb.name)

print 'Added'

add_this_instance_to_elb()
