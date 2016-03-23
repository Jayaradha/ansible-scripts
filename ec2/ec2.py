import boto.ec2
conn = boto.ec2.connect_to_region('us-west-2')
conn.start_instances("i-afdb8d68")

