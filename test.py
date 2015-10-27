#!/usr/bin/python

import dfu_transport_serial
from nrfhex import *



def read_file(file_path):
        """
        Reads a file and returns the content as a string.

        :param str file_path: The path to the file to read.
        :return str: Content of the file.
        """
        buffer_size = 4096

        file_content = ""

        with open(file_path, 'rb') as binary_file:
            while True:
                data = binary_file.read(buffer_size)

                if data:
                    file_content += data
                else:
                    break

        return file_content


serialTransport = dfu_transport_serial.DfuTransportSerial('/dev/ttyUSB0')

serialTransport.open()
#if serialTransport.is_open():
#	print 'IsOpen'

#hexFirmware = nRFHex('binaries/blinky_s110.hex')
#hexFirmware.tobinfile('binaries/blinky.bin')

firmware = read_file('binaries/pin.bin')

serialTransport.send_start_dfu(4,0,0,len(firmware))
serialTransport.send_init_packet(firmware)
serialTransport.send_firmware(firmware)
serialTransport.close()

