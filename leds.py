import socket

def _send_artdmx(ip, port, universe, dmx_data):
    # Art-Net packet constants
    ARTNET_HEADER = b'Art-Net\x00'
    OPCODE = b'\x00\x50'  # OpCode for ArtDmx packet is 0x5000
    PROTOCOL_VERSION = b'\x00\x0e'  # Art-Net version 14
    SEQUENCE = b'\x00'  # Sequence byte, can be 0 for no sequence
    PHYSICAL = b'\x00'  # Physical input port
    UNIVERSE = universe.to_bytes(2, byteorder='little')  # Universe, little-endian
    LENGTH = len(dmx_data).to_bytes(2, byteorder='big')  # Data length

    # Combine all parts to form the ArtDmx packet
    packet = ARTNET_HEADER + OPCODE + PROTOCOL_VERSION + SEQUENCE + PHYSICAL + UNIVERSE + LENGTH + dmx_data

    # Send packet using UDP to the specified IP address and port
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(packet, (ip, port))

def send_leds(ip, port, universe, rgb_array):
    # Flatten the RGB array to a DMX data byte array
    dmx_data = bytes([channel for rgb in rgb_array for channel in rgb])

    # Send the ArtDmx packet
    _send_artdmx(ip, port, universe, dmx_data)
