import boto
import sys

ec2 = boto.connect_ec2()
elb = boto.connect_elb()

elb_conn = boto.ec2.elb.connect_to_region(region_name='us-west-2')
load_balancer =  elb_conn.get_all_load_balancers('boto')[0]

#load_balancer = elb.get_all_load_balancers('botoelb')[0]
health = load_balancer.get_instance_health()
instances = ec2.get_only_instances(instance_ids=[instance.id for instance in load_balancer.instances])
headers = ['Instance ID', 'Address', 'Flavor', 'Status']
row_format = "{:>15}" * (len(headers) + 1)
print row_format.format("",*headers)

for instance in instances:
    print row_format.format('',*[instance.id, instance.ip_address, instance.instance_type, [str(i.state) for i in health if i.instance_id == instance.id ][0]])
	print instance.id,instance.instance_type,instance.state

