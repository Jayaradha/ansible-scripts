
EC2:
===================
This is simple python code to demonstrate how to add or remove instance from ELB and monitor the status oinstances

Pre prerequisites:
1.Install python and boto
2.Amaxon root account
3. Set accesskey and secretkey in your bashprofile

##Instructions
python elbadd.py <instanceID>
python elbremove.py <instanceID>
python elbstatus.py #Note : this can be modified to pass elb name as paramenter

ANSIBLE
===============
Ansible script to install and setup LAMP stack.

Pre prerequisites:
1. Install ansible in your local environment
2. Amazon root account
3. Set accesskey and secretkey in your bashprofile
4. Under hosts file change the ip to your instance IP

##Instructions

ansible-playbook --sudo --inventory-file=hosts playbook.yml -u ubuntu --verbose


##phpadmin:

You now only need to add those variable into playbook.yml
```yaml
phpmyadmin:
  -
    user: mysql user
    pass: mysql password
    hostname: phpmyadmin hostname
    pma_dbname: phpmyadmin database name
```


References
=============
http://docs.ansible.com/
http://labs.qandidate.com/
http://stackoverflow.com/questions/23242067/how-to-install-phpmyadmin-on-debian-by-ansible
http://docs.ansible.com/ansible/apt_module.html

etc


