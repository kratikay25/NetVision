# NetVision Architecture

## Overview

NetVision is an agent-based network monitoring platform.

### Components

### Server

- Accepts agent connections
- Routes packets
- Stores connected agents
- Displays dashboard
- Generates alerts
- Stores logs

### Agent

- Registers with server
- Sends heartbeat
- Sends system information
- Receives commands

### Shared

- Packet serialization
- JSON protocol
- Constants
- Exceptions

## Communication

Agent

↓

REGISTER

↓

WELCOME

↓

HEARTBEAT

↓

SYSTEM_INFO

↓

COMMAND

↓

COMMAND_RESPONSE

↓

DISCONNECT