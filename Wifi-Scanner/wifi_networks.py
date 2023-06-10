import subprocess


def get_wifi_networks():
    ''' Returns a list of available Wi-Fi networks sorted by signal strength
    - uses the airport command line tool to get a list of available Wi-Fi networks
    - airport command line tool is only available on Mac OS X
    '''
    command = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s'
    output = subprocess.check_output(command, shell=True).decode()
    networks = output.strip().split('\n')[1:]

    network_name = [network[:network.find(':') - 2].strip()
                    for network in networks]

    bssid = [network[network.find(
        ':') - 2:network.find(':') + 15].strip() for network in networks]

    rssi = [network[network.rfind(
        ':') + 3:network.rfind(':') + 7].strip() for network in networks]

    channels = [network[network.rfind(
        ':') + 7:network.rfind(':') + 16].strip() for network in networks]

    security = [network[network.find('None'):] if network.find('None') != -1 else network[network.find('WEP'):] if network.find(
        'WEP') != -1 else network[network.find('WPA'):] if network.find('WPA') != -1 else network[network.find('WPA2'):] for network in networks]

    networks = [network_name[i] + ' | ' + bssid[i] + ' | ' + rssi[i] + ' | ' +
                channels[i] + ' | ' + security[i] for i in range(len(network_name))]

    networks = sorted(networks, key=lambda x: int(
        x.split(' | ')[2]), reverse=True)

    return networks


def output_networks(networks):
    '''Prints a list of available Wi-Fi networks in the terminal'''
    print('Available Wi-Fi Networks:')
    for network in networks:
        print(network)


def create_markdown_file(networks):
    '''Creates a markdown file with all available Wi-Fi networks'''
    with open('wifi_networks.md', 'w') as f:
        f.write('Available Wi-Fi Networks:\n')
        f.write('| Network Name | BSSID | RSSI | Channel | Security |\n')
        f.write('| --- | --- | --- | --- | --- |\n')
        for network in networks:
            f.write('| {} | {} | {} | {} | {} |\n'.format(
                *network.split(' | ')))


def main():
    networks = get_wifi_networks()
    output_networks(networks)
    create_markdown_file(networks)


if __name__ == '__main__':
    main()