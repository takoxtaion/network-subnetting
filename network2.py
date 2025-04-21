ip_input = input("IP Address (e.g. 192.168.1.5/24): ")


ip_address, slash = ip_input.split("/")
ip_list = [int(octet) for octet in ip_address.split(".")]
slash = int(slash)

def calculate_subnet_mask(slash):
    mask = []
    full_bytes = slash // 8
    remaining_bits = slash % 8

    for _ in range(full_bytes):
        mask.append(255)

    if remaining_bits:
        mask.append(256 - (2 ** (8 - remaining_bits)))

    while len(mask) < 4:
        mask.append(0)

    return mask


def calculate_network_address(ip_list, subnet_mask):
    network = []
    for i in range(4):
        network.append(ip_list[i] & subnet_mask[i])
    return network


def calculate_broadcast_address(network_address, subnet_mask):
    broadcast = []
    for i in range(4):
        broadcast.append(network_address[i] | (255 - subnet_mask[i]))
    return broadcast


def list_to_ip(ip_list):
    return ".".join(str(x) for x in ip_list)


subnet_mask = calculate_subnet_mask(slash)
network_address = calculate_network_address(ip_list, subnet_mask)
broadcast_address = calculate_broadcast_address(network_address, subnet_mask)


print(f"\nIP Address: {ip_address}/{slash}")
print(f"Network Address: {list_to_ip(network_address)}")
print(f"Broadcast Address: {list_to_ip(broadcast_address)}")
print(f"Subnet Mask: {list_to_ip(subnet_mask)}")

