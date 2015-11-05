#!/bin/bash

printf -v ID "%x" "$1"

sudo ftx-prog-master/./ftx_prog --cbus 0 Drive_1 --cbus 1 Drive_0
#./prog.sh --erase-all
./prog.sh --prepare-NEMO 9.0.0/components/softdevice/s110/hex/s110_softdevice.hex 9.0.0/examples/dfu/ewids_bootloader_adc_single_sd_clean/wristband/single_bank_serial_s110/armgcc/_build/nrf51422_xxac.hex $ID

