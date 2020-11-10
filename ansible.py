import os

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
