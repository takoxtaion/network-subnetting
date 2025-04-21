network_id = input("Network ID (e.g. 123.0.0.0): ")
subnets_required = int(input("Subnets Required (e.g. 65): "))


network_id_list = [int(x) for x in network_id.split(".")]


class_dict = {
    "A": 8,
    "B": 16,
    "C": 24
}


def calculate_class(network_id_list):
    first_octet = network_id_list[0]
    if 0 <= first_octet < 128:
        return "A"
    elif 128 <= first_octet < 192:
        return "B"
    elif 192 <= first_octet < 224:
        return "C"


def calculate_bits(subnets_required):
    for n in range(1, 9):
        if subnets_required <= 2 ** n:
            return n


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

    return ".".join(str(octet) for octet in mask)


def first_available_host_address_of_subnet_1(network_id_list, slash):
    new_network_id = network_id_list.copy()
    bits_for_host = 32 - slash
    block_size = 2 ** (8 - (slash % 8)) if slash % 8 != 0 else 1


    octet_to_increment = slash // 8

    new_network_id[octet_to_increment] += block_size

    for i in reversed(range(4)):
        if new_network_id[i] > 255:
            new_network_id[i] -= 256
            if i - 1 >= 0:
                new_network_id[i - 1] += 1


    new_network_id[3] += 1
    for i in reversed(range(4)):
        if new_network_id[i] > 255:
            new_network_id[i] -= 256
            if i - 1 >= 0:
                new_network_id[i - 1] += 1

    return ".".join(str(x) for x in new_network_id)

def max_number_of_hosts_subnet(slash):
    return (2 ** (32 - slash)) - 2


network_class = calculate_class(network_id_list)
slash = class_dict[network_class] + calculate_bits(subnets_required)


print(f"\nNetwork ID: {network_id}")
print(f"Class: {network_class}")
print(f"Subnet Mask: {calculate_subnet_mask(slash)}")
print(f"1st Available Host Address of Subnet 1: {first_available_host_address_of_subnet_1(network_id_list, slash)}")
print(f"Max # of Hosts per Subnet: {max_number_of_hosts_subnet(slash)}")
