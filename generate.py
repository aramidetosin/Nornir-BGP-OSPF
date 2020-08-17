list_ip = ['192.168.1.191',
           '192.168.1.192',
           '192.168.1.193',
           '192.168.1.194',
           '192.168.1.195',
           '192.168.1.196',
           '192.168.1.197',
           '192.168.1.198']


with open("hosts.yaml", "w") as file:
    file.write("---\n")
    for num , ip in enumerate(list_ip):
        file.write(f'R{num+1}:\n')
        file.write(f'    hostname: {ip}\n')
        file.write(f'    data:\n')
        file.write(f'        asn: 65001\n')

with open("config.yaml", "w") as file:
    file.write("---\n")
    file.write("core:\n")
    file.write("    num_workers: 100\n")
    file.write("inventory:\n")
    file.write("    plugin: nornir.plugins.inventory.simple.SimpleInventory\n")
    file.write("    options:\n")
    file.write('        host_file: "hosts.yaml"\n')
    file.write('        group_file: "groups.yaml"\n')
    file.write('        defaults_file: "defaults.yaml"\n')

with open("defaults.yaml", "w") as file:
    file.write("---\n")
    file.write("username: cisco\n")
    file.write("password: cisco\n")
    file.write("platform: 'ios'\n")


with open("groups.yaml", "w") as file:
    file.write("---\n")
    file.write("cisco_group:\n")
    file.write("    platform: 'ios'\n")