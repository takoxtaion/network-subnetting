# Network Tools

This repository contains Python scripts for networking tasks related to IP addressing and subnetting.

## Scripts

### `network1.py`
- **Purpose**: Calculates subnet masks, first available host address of subnet 1, and the maximum number of hosts for a given network and subnets required.
- **Usage**: 
  - Enter the **Network ID** and **Subnets Required**, and the script will output the subnet mask, first available host address, and max hosts per subnet.

### `network2.py`
- **Purpose**: Determines the network address, broadcast address, and subnet mask for a given IP address and CIDR notation.
- **Usage**: 
  - Enter an **IP address** and its **CIDR** (e.g., `105.190.75.240/22`) and the script will output the network address, broadcast address, and subnet mask.

## Requirements

- Python 3.x
- No additional libraries required.

## Usage

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/takoxtaion/network-subnetting.git
   ```
   
2. Navigate to the project folder:

  ```bash
  cd network-subnetting
  ```

3. Run the scripts using Python 3:
  ```bash
  python3 network1.py
  python3 network2.py
  ```

## Example

### For network1.py:

- Network ID: 207.87.203.0
- Subnets Required: 3
- Output:

  ```bash
  Network ID: 207.87.203.0
  Class: C
  Subnet Mask: 255.255.255.192
  1st Available Host Address of Subnet 1: 207.87.203.65
  Max # of Hosts/Subnet: 62
  ```

### For network2.py:

- IP Address: 105.190.75.240/22
- Output:

  ```bash
  IP Address: 105.190.75.240/22
  Network Address: 105.190.72.0
  Broadcast Address: 105.190.75.255
  Subnet Mask: 255.255.252.0
  ```


