import os
def docker():
	print("Welcome to Docker services")
	
	while(1):
		print("1.Start Docker Services \n2.Stop Docker Services \n3.Launch OS container \n4.Pull OS Image from Docker \n5.Check Images Available \n6.Exit Services /n")
		n = int(input())
		if(n==1):
			cmd = "systemctl start docker"
			os.system(cmd)
			print("Your docker service succefully started")
		elif(n==2):
			cmd = "systemctl stop docker"
			os.system(cmd)
			print("Your docker service succefully stopped")
		elif(n==3):
			print("OS Available")
			cmd="docker images"
			os.system(cmd)
			print("Enter the OS you want to launch")
			OS= input()
			print("Enter the OS name")
			OS_name=input()
			cmd="docker run -it --name {} {}".format(OS_name,OS)
			os.system(cmd)
			print("OS Launched Successfully") 
		elif(n==4):
			print("Enter the OS name you want to install")
			OS = input()
			cmd="docker pull {}".format(OS)
			os.system(cmd)
		elif(n==5):
			print("OS Available")
			cmd="docker images"
			os.system(cmd)
		elif(n==6):
			print("Thankyou for using docker services")
			break


def config_yum():      #to be modified
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


def hadoop_pyscript(ip, hdfs_name_tag, hdfs_value_tag, node_type, dn_no):
    ip = '"' + ip + '"'
    line_8 = 'nn_ip = ' + ip + '\n'
    line_9 = 'file_handling("' + hdfs_name_tag + '", "'+ hdfs_value_tag + '", "hdfs-site.xml")\n'
    pyscript = ['import os\n', 
    'os.system("pip3 install gdown")\n', 
    'os.system("gdown --id 1S7rpt9ituQQF8R0kYxWYMhfsmWPL3BOe")\n', 
    'os.system("gdown --id 15M3sTqRfiP8WKsHFNOcfK9IggRsd5ZEu")\n', 
    'os.system("rpm -ivh /root/jdk-8u171-linux-x64.rpm")\n', 
    'os.system("rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")\n', 
    '\n', 
    'def file_handling(name_tag, value_tag, file_name):\n', 
    '\tname_tag = "<name>" + name_tag + "</name>\\n"\n', 
    '\tvalue_tag = "<value>" + value_tag + "</value>\\n"\n', 
    '\tdir = "/etc/hadoop/" + file_name\n', 
    '\n', 
    '\thdfs_file_lines = [\'<?xml version="1.0"?>\\n\', \'<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\\n\',\n', 
    '\t\'\\n\', \'<!-- Put site-specific property overrides in this file. -->\\n\', \'\\n\', \'<configuration>\\n\', \'<property>\\n\',\n', 
    '\tname_tag, value_tag, \'</property>\\n\', \'</configuration>\\n\']\n', 
    '\n', 
    '\thdfs_file = open(dir, "w")\n', 
    '\thdfs_file.writelines(hdfs_file_lines)\n', 
    '\thdfs_file.close()\n'
    '\n',
    line_8, 
    line_9, 
    'value_tag = "hdfs://" + nn_ip + ":9001"\n', 
    'file_handling("fs.default.name", value_tag , "core-site.xml")\n', 
    '\n']

    if node_type == 'N':
        pyscript.append('\nos.system("rm -rf /nn")')
        pyscript.append('\nos.system("mkdir /nn")')
        pyscript.append('\nos.system("hadoop namenode -format")')
        pyscript.append('\nos.system("systemctl stop firewalld")')
        pyscript.append('\nos.system("hadoop-daemon.sh start namenode")')
    elif node_type == 'D':
        cmd = 'rm -rf /dn' + str(dn_no)
        pyscript.append(cmd)
        cmd = '\nos.system("mkdir /dn'+ str(dn_no) +'")'
        pyscript.append(cmd)
        pyscript.append('\nos.system("systemctl stop firewalld")')
        pyscript.append('\nos.system("hadoop-daemon.sh start datanode")')
    elif node_type == 'C':
        pyscript.pop(21)
        pyscript.append('\nos.system("systemctl stop firewalld")')
        #pyscript.append('\nos.system("hadoop-daemon.sh start namenode")')

    hdfs_file = open('imp.py', 'w')
    hdfs_file.writelines(pyscript)
    hdfs_file.close()

    cmd = "scp imp.py root@" + ip + ":/root"
    os.system(cmd)
    cmd = "ssh root@" + ip + " python3 /root/imp.py"
    os.system(cmd)


def config_hadoop():
    nn = input("Enter Name Node's IP: ")
    hadoop_pyscript(nn, 'dfs.name.dir', '/nn', 'N', 0)

    dnn = int(input("Number of Data Nodes: "))
    for i in range(dnn):
        dn = input("Enter Data Node {}'s IP: ".format(i+1))
        dn_dir = '/dn' + (i+1)
        hadoop_pyscript(dn, 'dfs.data.dir', dn_dir, 'D', i+1)

    client = int(input("Number of Client Nodes: "))
    for i in range(client):
        client_ip = input("Enter Client {}'s IP: ".format(i+1))
        hadoop_pyscript(client_ip, '', '', 'C', 0)


#-----------------Work in progress-----------------------------#
def hadoop_client_services():
    choice = int(input('''Available hadoop client services:
    Press 1: To see dfs report
    Press 2: To list files in 
    
    Enter your choice here: '''))
#---------------------------------------------------------------#

def hapoop_services():
    choice = int(input('''Available hadoop services:
    Press 1: To setup a cluster
    Press 2: To use WebUI
    Press 2: To access hadoop client services
    
    Enter your choice here: '''))

    if choice == 1:
        config_hadoop()

    elif choice == 2:
        nn_IP = input('Enter the IP of your cluster\'s Name Node: ')
        cmd = 'firefox ' + nn_IP + ':50070'
        os.system(cmd) 

    elif choice == 3:
        hadoop_client_services()

    else:
        print('Invalid Choice')


def Aws_cli():
	while True:
		os.system("clear")
		print("""Welcome to AWS automation 
		press 1: To install AWS CLI
		press 2: To check the AWS CLI version
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
			exit()
		
		input("press enter to continue to AWS CLI menu")
        
##################################Ansible#########################################

def ansible_config():
    os.system('rm -rf /etc/ansible /root/ansible_inventory')
    os.system('mkdir /etc/ansible')
    os.system('mkdir /root/ansible_inventory')
    os.system('touch /root/ansible_inventory/ip.txt')
    fh = open('/etc/ansible/ansible.cfg','w')
    fh.write('[defaults]\ninventory = /root/ansible_inventory/ip.txt\nhost_key_checking = false \n')
    fh.close()

def write_inventory(group_name, mode):

    ip_address = input("Enter IP address of client device: ")    
    username = input("Enter the user name of client device: ")
    password = input("Enter the password of client device: ")

    file_lines = ['{}  ansible_ssh_user={}  ansible_ssh_pass={}\n'.format(ip_address , username , password)]

    if mode == 'N':
        fh = open('/root/ansible_inventory/ip.txt', 'a+')
        fh.write(group_name)
        fh.write(file_lines)
        fh.close()
    elif mode == 'E':
        fh = open('/root/ansible_inventory/ip.txt', 'r')
        all_lines = fh.readlines()
        fh.close()
        for i, line in enumerate(all_lines):
            if group_name == line:
                all_lines.insert(i+1, file_lines)
                break
        fh = open('/root/ansible_inventory/ip.txt', 'w+')
        fh.write(all_lines)
        fh.close()


def file_handling_ansible():
    group = int(input('''Press 1: To create a new group
Press 2: To add to an existing group

Enter your choice here: '''))
    group_name = input('Enter the group name without using "[]": ')
    group_name = '[' + group_name + ']\n'

    if group == 1:
        write_inventory(group_name, 'N')

    elif group_name == 2:
        write_inventory(group_name, 'E')

    else:
        print('Invalid Choice')

def ansible_services():
	while True:
		print("""
ANSIBLE OPERATIONS

Press 1: TO install ansible
Press 2: TO COnfigure ansible
Press 3: TO enter IP, username and password of the system on which you want run commands using ansible
Press 4: Enter your ansible commands
Press 5: To exit from ansible menu
""")
		ch = int(input("Enter your choice: "))
		if ch == 1:
			os.system ("pip3 install ansible")
		elif ch == 2:
			ansible_config()
		elif ch == 3:
			file_handling_ansible()
		elif ch == 4:
			cmd = input("Enter your ansible commands: ")
			os.system(cmd)
		elif ch == 5:
			break
		
		input("\nPress enter to continue: ")
	
###########################################################################

while True:

    print("""Welcome
    Enter your choice:
    Press 1: To configure yum repository
    Press 2: To access hadoop services
    press 3: To access AWS CLI
    press 4: To acess docker services
    press 5: To access ansible services
    """)

    user_choice1 = int(input("Enter your choice here: "))
    
    if user_choice1 == 1:
        config_yum()   

    elif user_choice1 == 2:
        hapoop_services()
    
    elif user_choice1 == 3:
        Aws_cli()

    elif user_choice1 == 4:
        docker()

    elif user_choice1 == 5:
        ansible_services()

    # add extra functionalities here inside elif

    else:
        print("Invalid Input")
    
    choice_to_loop = input("Press 'y' to continue or 'n' to quit: ")
    if choice_to_loop != 'y' and choice_to_loop != 'Y':
        break
