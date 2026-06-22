# Networking

Networking is a group of computers and devices linked together in a way that allows them to communicate and share resources with each other.
E.g. Laptop, printers, smartphones etc.

## How computer network work?
### 1. Establishing a Network
- First, physical or wireless connections must be made to form the network infrastructure.

- Devices (like computers, servers, and smartphones) are linked using physical cables (like Ethernet or fiber optics) or wireless technologies (like Wi-Fi and cellular networks).

### 2. Communication Protocols
- Once the network is physically established, devices must speak the same language to communicate efficiently. This "language" is called a Protocol.

- Key Examples: 
    - TCP/IP: The fundamental protocol suite that powers the entire Internet.
    - HTTP/HTTPS: Used for loading web pages.
    - FTP: Used for transferring files.

### 3. Data Packetization (Data Transmission)
- Before data is sent, it is broken down into smaller, manageable chunks called packets.

- Why? Large files (like a video) would clog the network if sent all at once. Packets allow the network to distribute traffic evenly. Each packet contains the actual data, plus a "header" with the source and destination IP addresses.

### 4. Routing and Switching
- A packet rarely travels in a straight line from source to destination. It takes a dynamic journey across the network, guided by specialized hardware.

- The Devices: 
    - Switches: Connect devices within the same local network (like inside your home or office).
    - Routers: Act as traffic cops that direct packets between different networks (like connecting your home network to the global Internet).

### 5. Data Reassembly, Receipt, and Confirmation
- The receiving device collects all the incoming packets, puts them back in the correct order, and checks for errors.

- The Feedback Loop: If a packet arrives corrupted or gets lost along the way, the receiving device asks the sender to retransmit it. Once everything arrives perfectly, a confirmation (ACK) is finalized, and the data is displayed to the user.