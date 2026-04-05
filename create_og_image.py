#!/usr/bin/env python3
"""Create a simple OG screenshot placeholder for Merxex."""

import struct
import zlib

def create_png(width, height, bg_color, text_color, text_x, text_y, text):
    """Create a minimal PNG with solid background and text."""
    def png_chunk(chunk_type, data):
        chunk_len = struct.pack('>I', len(data))
        chunk_crc = struct.pack('>I', zlib.crc32(chunk_type + data) & 0xffffffff)
        return chunk_len + chunk_type + data + chunk_crc

    # PNG signature
    signature = b'\x89PNG\r\n\x1a\n'

    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    ihdr = png_chunk(b'IHDR', ihdr_data)

    # Create raw image data (RGB)
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'  # Filter byte
        for x in range(width):
            if y >= text_y - 15 and y <= text_y + 15 and x >= text_x - len(text) * 10 and x <= text_x + len(text) * 10:
                # Simple text area - use text color
                raw_data += bytes(text_color)
            else:
                raw_data += bytes(bg_color)

    # IDAT chunk (compressed image data)
    compressed = zlib.compress(raw_data, 9)
    idat = png_chunk(b'IDAT', compressed)

    # IEND chunk
    iend = png_chunk(b'IEND', b'')

    return signature + ihdr + idat + iend

# Merxex branding colors
bg_color = (102, 126, 234)  # Purple gradient start
text_color = (255, 255, 255)  # White text

# Create 1200x630 OG image
img_data = create_png(1200, 630, bg_color, text_color, 400, 300, "MERXEX")

with open('/tmp/merxex-website/images/og-screenshot.png', 'wb') as f:
    f.write(img_data)

print("Created og-screenshot.png (1200x630)")