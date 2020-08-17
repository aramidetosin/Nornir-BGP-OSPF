list_ip = ['192.168.1.191',
           '192.168.1.192',
           '192.168.1.193',
           '192.168.1.194',
           '192.168.1.195',
           '192.168.1.196',
           '192.168.1.197',
           '192.168.1.198']

with open("testbed.yaml", "w") as file:
    file.write("---\n")
    file.write("testbed:\n")
    file.write("  credentials:\n")
    file.write("    default:\n")
    file.write("      username: 'cisco'\n")
    file.write("      password: 'cisco'\n")
    file.write("devices:\n")
    for num , ip in enumerate(list_ip):
        file.write(f'  R{num+1}:\n')
        file.write(f'    alias: R{num+1}\n')
        file.write(f'    os: iosxe\n')
        file.write(f'    type: IOSv\n')
        file.write(f'    connections:\n')
        file.write(f'      defaults:\n')
        file.write(f'        class: unicon.Unicon\n')
        file.write(f'      console:\n')
        file.write(f'        protocol: ssh\n')
        file.write(f'        ip: {ip}\n')

        file.write(f'    custom:\n')
        file.write(f'      abstration:\n')
        file.write(f'         order: [os, type]\n')