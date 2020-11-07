# Note:
# epel-release-latest-8.noarch.rpm needs to be present at /root/Downloads in the controler system
# jdk-8u171-linux-x64.rpm and hadoop-1.2.1-1.x86_64.rpm needs to be present at /root/Downloads/hadoop in the controler system

import os

def config_yum():
    sys = int(input("""Where do you want to configure yum:
    Press 1 for local system
    Press 2 for remote system
    Enter your choice here: """))

    if sys == 1:
        cmd = "rpm -ivh /root/Downloads/epel-release-latest-8.noarch.rpm"
        os.system(cmd)
    elif sys == 2:
        total_remote_sys = int(input("Enter the number of remote systems: "))
        for i in range(total_remote_sys):
            remote_sys_IP = input("Enter Remote System's IP: ")
            cmd = "scp /root/Downloads/epel-release-latest-8.noarch.rpm root@" + remote_sys_IP + ":/root/Downloads/"
            os.system(cmd)
            cmd = "ssh root@" + remote_sys_IP + " rpm -ivh /root/Downloads/epel-release-latest-8.noarch.rpm"
            os.system(cmd)
    else:
        print("Invalid Input")


def config_hadoop():
    nn = input("Enter Name Node's IP: ")
    cmd = "scp -r /root/Downloads/hadoop root@" + nn + ":/root/Downloads/"
    os.system(cmd)
    cmd = "ssh root@" + nn + "rpm -ivh /root/Downloads/hadoop/jdk-8u171-linux-x64.rpm"
    os.system(cmd)
    cmd = "ssh root@" + nn + "rpm -ivh /root/Downloads/hadoop/hadoop-1.2.1-1.x86_64.rpm  --force"
    os.system(cmd)

    dnn = int(input("Number of Data Nodes: "))
    for i in range(dnn):
        dn = input("Enter Data Node {}'s IP: ", i)
        cmd = "scp -r /root/Downloads/hadoop root@" + dn + ":/root/Downloads/"
        os.system(cmd)
        cmd = "ssh root@" + dn + "rpm -ivh /root/Downloads/hadoop/jdk-8u171-linux-x64.rpm"
        os.system(cmd)
        cmd = "ssh root@" + dn + "rpm -ivh /root/Downloads/hadoop/hadoop-1.2.1-1.x86_64.rpm  --force"
        os.system(cmd)

while True:

	print("""Welcome
	Enter your choice:
	Press 1: To configure yum repository
	Press 2: To setup a hadoop cluster
	press 3: To install AWS CLI
	press 4: To check the AWS CLI version
	press 5: To configure ASW CLI
	press 6: To describe all instances
	press 7: To describe a specific instance
	press 8: To create an EC2 instance
	press 9: To start an EC2 instance
	press 10: To stop an EC2 instance
	press 11: To create an EBS volume
	press 12: To attach an EBS volume

	""")

	user_choice1 = int(input("Enter your choice here: "))
	    
	if user_choice1 == 1:
		config_yum()   

	elif user_choice1 == 2:
		config_hadoop()

	elif user_choice1 == 3:
		os.system("pip3 install awscli --upgrade --user") 
		       
	elif user_choice1 == 4:
		os.system("aws --version")

	elif user_choice1 == 5:
		os.system("aws configure")

	elif user_choice1 == 6:
		os.system("aws ec2 describe-instances")

	elif user_choice1 == 7:
		ins_id = input("enter the instance id: ")
		os.system("aws ec2 describe-instance-status --instance-id {}".format(ins_id))

	elif user_choice1 == 8:
		img_id = input("Enter image ID: ")
		ins_type = input("Enter instance type: ")
		cnt = input("Enter the number of instances you want to launch: ")
		key_nm = input("Enter AWS key name: ")
		sec_id = input("Enter security group ids: ")
		sub_id = input("Enter subnet id: ")
			
		os.system("asw ec2 run-instances  --image-id {} --instance-type {} --count {} --key-name {} --security-group-ids {} --subnet-id {}".format(img_id , ins_type , cnt , key_nm , sec_id , sub_id))

	elif user_choice1 == 9:
		ins_id = input("Enter instance Id: ")
		os.system(" aws ec2 start-instances --instance-ids {} ".format(ins_id))

	elif user_choice1 == 10:
		ins_id = input("Enter instance Id: ")
		os.system(" aws ec2 stop-instances --instance-ids {} ".format(ins_id))

	elif user_choice1 == 11:
		size = input("Enter the size of stotage in GB: ")
		vol_type = input("Enter volume type: ")
		av_zone = input("Enter the availability zone: ")
		os.system("aws ec2 create-volume --size {} --volume-type {} --availability-zone {}".format(size , vol_type , av_zone))

	elif user_choice1 == 12:
		vol_id = input("Enter your EBS volume Id: ")
		ins_id = input("Enter your EC2 instance Id: ")
		dev_name = input("Enter your EBS storage name: ")
		os.system("aws ec2 attach-volume  --volume-id {}  --instance-id {} --device {}".format(vol_id , ins_id , dev_name)
			)
		
	    
	# add extra functionalities here inside elif

	else:
		print("Invalid Input")
	    
	choice_to_loop = input("Press 'y' to continue or 'n' to quit: ")
	if choice_to_loop != 'y' and choice_to_loop != 'Y':
		break
