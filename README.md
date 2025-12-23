# pick_pdu – Configurable Ethernet PDU Builder & UDP Sender

## Overview

**pick_pdu** is a Python-based framework for **building, managing, and transmitting Ethernet PDUs over UDP**.
It follows a **protocol-accurate PDU model** commonly used in automotive and embedded Ethernet systems.

The project has been **tested end-to-end between Windows 11 and a Raspberry Pi**, validating interoperability across desktop and embedded Linux environments.

---

** Usage **
	# please check the tests folder how to build pdus and signals

## Ethernet PDU Model

Every Ethernet PDU handled by this project follows the structure below:

```
+-------------------+-------------------+----------------------+
|   PDU ID (4 B)    |  Length (4 B)     |     Payload Data     |
+-------------------+-------------------+----------------------+
```

- **PDU ID (4 bytes)** – Unique identifier for the PDU
- **Length (4 bytes)** – Payload length in bytes
- **Payload** – Collection of signals packed sequentially

---

## Signal-Oriented Payload Design

The payload consists of **N signals**, where each signal has:
- Position in the payload
- Endianness (Little Endian or Big Endian)

```
UDP
	PDU1 
	  Payload
	  │
	  ├── Signal A (Little Endian)
	  ├── Signal B (Little Endian)
	  ├── Signal C (Little Endian)
	  └── ...
  
	PDU2
	  Payload
	  │
	  ├── Signal A (Little Endian)
	  ├── Signal B (Little Endian)
	  ├── Signal C (Little Endian)
	  └── ...
	  
	PDU3 
	  Payload
	  │
	  ├── Signal A (Little Endian)
	  ├── Signal B (Little Endian)
	  ├── Signal C (Little Endian)
	  └── ...
	  
	# you can also use signal bits with big endian as well
```

Endianness is handled **per PDU**, not per ** signal **.

---

## What This Framework Enables

### PDU-Level Operations
- Add new PDUs
- Remove existing PDUs
- Modify PDU IDs
- Automatic payload length calculation

### Signal-Level Operations
- Add signals to a PDU
- Remove signals from a PDU
- Control signal ordering
- Support mixed endianness across the different PDU

This mirrors real-world automotive protocol configuration tools.

---

## Project Structure & Responsibilities

```
pick_pdu/
│
├── main.py
│   Entry point for building and sending PDUs
│
├── jsons/
│   ├── pdus.json
│   │   Declarative PDU and signal definitions
│   │
│   └── json_file_operations.py
│       JSON parsing and validation
│
├── pdus/
│   ├── pdu.py
│   │   Core PDU abstraction
│   │
│   ├── pdu_builder.py
│   │   Builds PDUs dynamically from definitions
│   │
│   └── pdu_cyclic_timer.py
│       Cyclic transmission support
│
├── utils/
│   ├── pdu_utils.py
│   │   Signal packing and endianness handling
│   │
│   ├── packet_utils.py
│   │   Binary packet formatting
│   │
│   ├── udp_sender.py
│   │   UDP transport (protocol-agnostic)
│   │
│   ├── ip_utils.py
│   │   IP address handling
│   │
│   └── ip_port_builder.py
│       IP/Port configuration utilities
│
└── tests/
    Unit tests for signals and PDUs
```

---

## Layered Architecture

```
+-----------------------------------+
| PDU Definition (JSON)             |
+-----------------------------------+
              ↓
+-----------------------------------+
| PDU Builder & Signal Management   |
+-----------------------------------+
              ↓
+-----------------------------------+
| Packet Formatting (Bytes)         |
+-----------------------------------+
              ↓
+-----------------------------------+
| UDP Transport                     |
+-----------------------------------+
              ↓
+-----------------------------------+
| Network (Windows ↔ Raspberry Pi)  |
+-----------------------------------+
```

Each layer is isolated and independently extensible.

---

## Tested Environment

- **Sender**: Windows 11
- **Receiver**: Raspberry Pi (Linux)
- **Transport**: UDP over Ethernet

This confirms portability across desktop and embedded platforms.

---

## Real-World Applications

- Automotive Ethernet PDUs
- SOME/IP / DoIP-style packet modeling
- Network simulation tools
- Embedded protocol experimentation
- Educational protocol stack design

---

## Design Philosophy

- Data-driven protocol definition
- Clear separation of concerns
- Transport independence
- Protocol-accurate modeling

---

## Future Extensions

- UDP receiver and PDU decoder
- CRC / validation layer
- Logging and packet inspection
- CAN or SOME/IP integration

---

## Author

**Mithun Thejaswini**  
Automotive & Embedded Networking  
