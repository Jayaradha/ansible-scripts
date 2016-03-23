import time
import boto
import boto.ec2.elb
import boto.utils
import sys

def get_elb():
    elb_conn = boto.ec2.elb.connect_to_region(region_name='us-east-1')
    return elb_conn.get_all_load_balancers('boto')[0]

def remove_this_instance_from_elb():
        elb = get_elb()
        elb.deregister_instances(sys.argv[1])
        print 'Removing %s from ELB %s' % (sys.argv[1], elb.name)


print 'Removed'

remove_this_instance_from_elb()
