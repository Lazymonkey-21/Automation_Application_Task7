# Note:
# epel-release-latest-8.noarch.rpm needs to be present at /root/Downloads/autm_t7/ in the controler system
# jdk-8u171-linux-x64.rpm and hadoop-1.2.1-1.x86_64.rpm needs to be present at /root/Downloads/autm_t7/hadoop in the controler system

import os

def config_yum():
    sys = int(input("""Where do you want to configure yum:
    Press 1 for local system
    Press 2 for remote system
    Enter your choice here: """))

    if sys == 1:
        cmd = "rpm -ivh /root/Downloads/autm_t7/epel-release-latest-8.noarch.rpm"
        os.system(cmd)
    elif sys == 2:
        total_remote_sys = int(input("Enter the number of remote systems: "))
        for i in range(total_remote_sys):
            remote_sys_IP = input("Enter Remote System's IP: ")
            cmd = "scp /root/Downloads/autm_t7/epel-release-latest-8.noarch.rpm root@" + remote_sys_IP + ":/root/Downloads/"
            os.system(cmd)
            cmd = "ssh root@" + remote_sys_IP + " rpm -ivh /root/Downloads/epel-release-latest-8.noarch.rpm"
            os.system(cmd)
    else:
        print("Invalid Input")


def config_hadoop():
    nn = input("Enter Name Node's IP: ")
    cmd = "scp -r /root/Downloads/autm_t7/hadoop root@" + nn + ":/root/Downloads/"
    os.system(cmd)
    cmd = "ssh root@" + nn + " rpm -ivh /root/Downloads/hadoop/jdk-8u171-linux-x64.rpm"
    os.system(cmd)
    cmd = "ssh root@" + nn + " rpm -ivh /root/Downloads/hadoop/hadoop-1.2.1-1.x86_64.rpm  --force"
    os.system(cmd)
    
    nt = "dfs.name.dir"
    vt = "/nn"
    name_tag = "<name>" + nt + "</name>\n"
    value_tag = "<value>" + vt + "</value>\n"
    hdfs_file_lines = ['<?xml version="1.0"?>\n', '<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n',
     '\n', '<!-- Put site-specific property overrides in this file. -->\n', '\n', "<configuration>\n", '<property>\n',
      name_tag, value_tag, '</property>\n', "</configuration>"]
    hdfs_file = open("hdfs-site.xml", "w")
    hdfs_file.writelines(hdfs_file_lines)
    hdfs_file.close()

    #transport this file to NN using scp in os.system 
    cmd = "scp hdfs-site.xml root@" + nn + ":/etc/hadoop"
    os.system(cmd)

    dnn = int(input("Number of Data Nodes: "))
    for i in range(dnn):
        dn = input("Enter Data Node {}'s IP: ".format(i+1))
        cmd = "scp -r /root/Downloads/autm_t7/hadoop root@" + dn + ":/root/Downloads/"
        os.system(cmd)
        cmd = "ssh root@" + dn + " rpm -ivh /root/Downloads/hadoop/jdk-8u171-linux-x64.rpm"
        os.system(cmd)
        cmd = "ssh root@" + dn + " rpm -ivh /root/Downloads/hadoop/hadoop-1.2.1-1.x86_64.rpm  --force"
        os.system(cmd)



def Aws_cli():
	while True:
		os.system("clear")
		print("""Welcome to AWS automation 
		press 1: To install AWS CLI
		press 2:	To check the AWS CLI version
		press 3: To configure ASW CLI
		press 4: To describe all instances
		press 5: To describe a specific instance
		press 6: To create an EC2 instance
		press 7: To start an EC2 instance
		press 8: To stop an EC2 instance
		press 9: To create an EBS volume
		press 10: To attach an EBS volume
		press 11: Exit
		""")

		ch = int(input("enter your choice here:"))
		
		if ch==1:
			os.system("pip3 install awscli --upgrade --user")

		elif ch==2:
			os.system("aws --version")

		elif ch==3:
			os.system("aws configure")

		elif ch==4:
			os.system("aws ec2 describe-instances")

		elif ch==5:
			ins_id = input("enter the instance id: ")
			os.system("aws ec2 describe-instance-status --instance-id {}".format(ins_id))

		elif ch==6:
			img_id = input("Enter image ID: ")
			ins_type = input("Enter instance type: ")
			cnt = input("Enter the number of instances you want to launch: ")
			key_nm = input("Enter AWS key name: ")
			sec_id = input("Enter security group ids: ")
			sub_id = input("Enter subnet id: ")
			
			os.system("asw ec2 run-instances  --image-id {} --instance-type {} --count {} --key-name {} --security-group-ids {} --subnet-id {}".format(img_id , ins_type , cnt , key_nm , sec_id , sub_id))

		elif ch==7:
			ins_id = input("Enter instance Id: ")
			os.system(" aws ec2 start-instances --instance-ids {} ".format(ins_id))

		elif ch==8:
			ins_id = input("Enter instance Id: ")
			os.system(" aws ec2 stop-instances --instance-ids {} ".format(ins_id))

		elif ch==9:
			size = input("Enter the size of stotage in GB: ")
			vol_type = input("Enter volume type: ")
			av_zone = input("Enter the availability zone: ")
			os.system("aws ec2 create-volume --size {} --volume-type {} --availability-zone {}".format(size , vol_type , av_zone))

		elif ch==10:
			vol_id = input("Enter your EBS volume Id: ")
			ins_id = input("Enter your EC2 instance Id: ")
			dev_name = input("Enter your EBS storage name: ")
			os.system("aws ec2 attach-volume  --volume-id {}  --instance-id {} --device {}".format(vol_id , ins_id , dev_name)
			)
		elif ch==11:
			break
		
		input("press enter to continue to AWS CLI menu")




while True:

    print("""Welcome
    Enter your choice:
    Press 1: To configure yum repository
    Press 2: To setup a hadoop cluster
    press 3: To access AWS CLI

    """)

    user_choice1 = int(input("Enter your choice here: "))
    
    if user_choice1 == 1:
        config_yum()   

    elif user_choice1 == 2:
        config_hadoop()
    
    elif user_choice1 == 3:
        Aws_cli()
        
    # add extra functionalities here inside elif

    else:
        print("Invalid Input")
    
    choice_to_loop = input("Press 'y' to continue or 'n' to quit: ")
    if choice_to_loop != 'y' and choice_to_loop != 'Y':
        break