# Simple cli DNS changer by REDSA

import os
import shutil

# Path to the resolv.conf file
RESOLV_CONF_PATH = '/etc/resolv.conf'

# Backup file path
BACKUP_PATH = '/etc/resolv.conf.backup'

# New dns servers you want to set
SHECAN_DNS_SERVERS = [
    'nameserver 178.22.122.100\n'
    'nameserver 185.51.200.2'
]
GOOGLE_DNS_SERVERS = [
    'nameserver 8.8.8.8\n'
    'nameserver 8.8.4.4'
]
CLOUDF_DNS_SERVERS = [
    'nameserver 1.1.1.1'
]
NEXTDNS_DNS_SERVERS = [
    'nameserver 45.90.28.232\n'
    'nameserver 45.90.30.232'
]

def backup_resolv_conf():
    if not os.path.exists(BACKUP_PATH):
        shutil.copy(RESOLV_CONF_PATH,BACKUP_PATH)
        print("Backup of resolv.conf created.")
    else:
        print("Backup already exists.")

def change_dns_shecan():
    with open(RESOLV_CONF_PATH, 'w') as f:
        for dns_server in SHECAN_DNS_SERVERS:
            f.write(f"{dns_server}\n")
    print("DNS server updated.")

def change_dns_google():
    with open(RESOLV_CONF_PATH, 'w') as f:
        for dns_server in GOOGLE_DNS_SERVERS:
            f.write(f"{dns_server}\n")
    print("DNS server updated.")

def change_dns_cloudf():
    with open(RESOLV_CONF_PATH, 'w') as f:
        for dns_server in CLOUDF_DNS_SERVERS:
            f.write(f"{dns_server}\n")
    print("DNS server updated.")

def change_dns_next():
    with open(RESOLV_CONF_PATH, 'w') as f:
        for dns_server in NEXTDNS_DNS_SERVERS:
            f.write(f"{dns_server}\n")
    print("DNS server updated.")

def restore_resolv_conf():
    if os.path.exists(BACKUP_PATH):
        shutil.copy(BACKUP_PATH,RESOLV_CONF_PATH)
        os.remove(BACKUP_PATH)
        print("Original resolv.conf file restored.")
    else:
        print("No backup found. Cannot restore.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Temporary Cli DNS changer')
    parser.add_argument('action', choices=['shecan', 'google', 'cloudflare', 'nextdns', 'restore'], help="Action to perform: change to shecan(Ir), google, cloudflare, nextdns and Restore")

    args = parser.parse_args()

    if args.action == 'shecan':
        backup_resolv_conf()
        change_dns_shecan()
    elif args.action == 'google':
        backup_resolv_conf()
        change_dns_google()
    elif args.action == 'cloudflare':
        backup_resolv_conf()
        change_dns_cloudf()
    elif args.action == 'nextdns':
        backup_resolv_conf()
        change_dns_next()
    elif args.action == 'restore':
        restore_resolv_conf()
    else:
        print("Invalid action specified.")
