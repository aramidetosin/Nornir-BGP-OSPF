from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_config


def underlay(task):
    device = str(f'{task.host.hostname}')
    num = device[-1]
    loopback_ip = f"10.10.10.{str(num)}"

    loopback_commands = ['interface lo0', f'ip address {loopback_ip} 255.255.255.255', 'ip ospf 1 area 0']
    deploy_loopback = task.run(netmiko_send_config, config_commands=loopback_commands)
    ospf_commands = ['router ospf 1', f'router-id {loopback_ip}']
    deploy_ospf = task.run(netmiko_send_config, config_commands=ospf_commands)
    interface_commands = ['interface G0/0',
                          'ip ospf network point-to-point',
                          'ip ospf 1 area 0',
                          'interface G0/1',
                          'ip ospf network point-to-point',
                          'ip ospf 1 area 0'
                          ]
    deploy_interface = task.run(netmiko_send_config, config_commands=interface_commands)
    for i in range(1, 9):
        if str(i) == str(num):
            continue
        bgp_commands = ['router bgp ' + str(task.host['asn']),
                        'neighbor 10.10.10.' + str(i) + ' remote-as ' + str(task.host['asn']),
                        'neighbor 10.10.10.' + str(i) + ' update-source loopback0',
                        'neighbor 10.10.10.' + str(i) + ' password cisco',
                        'neighbor 10.10.10.' + str(i) + ' timers 10 30']
        deploy_bgp = task.run(netmiko_send_config, config_commands=bgp_commands)


def main() -> None:
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=underlay)
    print_result(result)


if __name__ == '__main__':
    main()
