#!/usr/bin/python


from os import listdir, path
import argparse
import socket

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET




class Host():
    
    def __init__(self, host):
        
        try:
            socket.inet_aton(host)
            self.ip = host
            self.domain = None
        except socket.error:
            self.ip = None
            self.domain = host
        
        self.up = False
        self.tcp_ports = list()
        self.udp_ports = list()
        self.filtered = list()
        self.os = None




def summary(hosts):
    
    for h in hosts:
    
        print ('\n{}'.format(h.ip))
        print '=' * len(h.ip)
    
        for tcp in h.tcp_ports:
            print('{}/TCP'.format(tcp))
    
        for udp in h.udp_ports:
            print('{}/UDP'.format(udp))




def getip(xml):
    address = xml.find('address')
    return address.attrib['addr']




def main(folder, debug):

    files = listdir(folder)
    hosts = list()
    
    for f in files:
        
        if debug:
            print('Parsing {}'.format(f))
        
        try:
            tree = ET.parse(path.join(folder, f))
            root = tree.getroot()
            host_xml = root.find('host')
            host = Host(getip(host_xml))
        except Exception as e:
            if debug:
                print('Wrong fromat (expected nmap XML output)')
            pass
        
        ports_xml = host_xml.find('ports')
        
        for port in ports_xml.findall('port'):
            
            p = port.attrib
            state_xml = port.find('state')
            
            if p['protocol'] == 'tcp':
                if state_xml.attrib['state'] == 'open':
                    host.tcp_ports.append(p['portid'])
                elif state_xml.attrib['state'] == 'open':
                    host.filtered.append(p['portid'])
            elif p['protocol'] == 'udp':
                if state_xml.attrib['state'] == 'open':
                    host.udp_ports.append(p['portid'])
        
        hosts.append(host)
    
    summary(hosts)




if __name__ == '__main__':
    
    args_parser = argparse.ArgumentParser(description='Parse nmap (XML) output.')
    args_parser.add_argument('folder', nargs='?', default='outputs/', help='Path where the nmap outputs are located.')
    args_parser.add_argument('-v', '--verbosity',  action='store_true', help='increase output verbosity.')
    args = args_parser.parse_args()

    main(args.folder, args.verbosity)
