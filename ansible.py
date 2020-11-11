import os

<<<<<<< HEAD
def file_handling_ansible():
	fh = open('/root/ip.txt','w')
	fh.write('')	
	
=======
def ansible_config():
    fh = open('/etc/ansible/ansible.cfg','w+')
    fh.write('[defaults] \n inventory = /root/ip.txt \n host_key_checking = false \n')
    fh.close()

def file_handling_ansible():
    ip_address = input("Enter IP address of client device: ")    
    username = input("Enter the user name of client device: ")
    password = input("Enter the password of client device: ")

    fh = open('root/ip.txt','w+')
    fh.write('{}  ansible_ssh_user = {}  ansible_ssh_pass = {}'.format(ip_address , username , password))
    fh.close()    

>>>>>>> f44d403acd8bbeeb28d7475314ce7bc6713c4108

while True:
    print("""
        ANSIBLE OPERATIONS

        press 1: TO install ansible
        press 2: TO COnfigure ansible
        press 3: TO enter IP, username and password of the system on which you want run commands using ansible
        press 4: Enter your ansible commands
        press 5: To exit from ansible menu
    """)
    ch = int(input("Enter your choice: "))

    if ch == 1:
        os.system ("pip3 install ansible")

    elif ch == 2:
        print("COnfigure ansible")

    elif ch == 3:
        print("TO enter IP, username and password of the system on which you want run commands using ansible")

    elif ch == 4:
        print("Enter your ansible commands")

    elif ch == 5:
        exit
    
    break
