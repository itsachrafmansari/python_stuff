import subprocess

networks = []
name_len = 0
pass_len = 0

print("Searching for known Networks...\n\n")

# getting meta data
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

# Get a list of all known networks
wlan_profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp1252').split('\n')

# Find the password of every network
for wlan_profile in wlan_profiles:
    network_password = ""
    if "All User Profile" in wlan_profile:
        network_name = wlan_profile.split(":")[1][1:-1]

        # Get wlan_profile details
        profile_details = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', f"{network_name}", 'key=clear']
        ).decode('cp1252').split('\n')

        # Extract the profile's password
        for detail in profile_details:
            if "Key Content" in detail:
                network_password = detail.split(":")[1][1:-1]

        # Add the network to the networks list and check the length of its name and password
        networks.append((network_name, network_password))
        if len(network_name) > name_len:
            name_len = len(network_name)
        if len(network_password) > pass_len:
            pass_len = len(network_password)

# Sort networks by their names
networks.sort(key=lambda network: network[0])

# Display all the known networks
if networks:
    print(f"|  {'Names':<{name_len}}  |  {'Passwords':<{pass_len}}  |\n{'-'*(name_len+pass_len+11)}")
    for network in networks:
        print(f"|  {network[0]:<{name_len}}  |  {network[1]:<{pass_len}}  |")
else:
    print("Did not find any known networks !")


input("\n\nPress Enter to exit\n\n")
