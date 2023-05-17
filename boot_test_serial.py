#!/usr/bin/env python3
import subprocess
import serial
import time

class DutPwrHost:
    def __init__(self, hostname):
        self.hostname = hostname

    def ssh_cmd(self, cmd):
        ssh_cmd = ["ssh", "-t", self.hostname, cmd]
        subprocess.run(ssh_cmd)

    def on(self):
        self.ssh_cmd("piTest -w RevPiLED,0")

    def off(self):
        self.ssh_cmd("piTest -w RevPiLED,64")

    def pwr_cycle(self):
        self.off()
        time.sleep(0.7)
        self.on()

def run_test(cycle_count):
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    timestamp = int(time.time())
    log_name = f'{cycle_count:04}_{timestamp}_serial.log'
    log = open(log_name, "x")
    ser.reset_input_buffer()
    dut_pwr.on()
    abort_strings = ["running in system mode.", "---[ end Kernel panic - not syncing"]

    while True:
        line = ser.readline()
        line = line.decode(encoding='ascii', errors='ignore')
        log.write(line)
        print(line.strip())
        if any(map(line.__contains__, abort_strings)):
            break
    dut_pwr.off()
    ser.reset_input_buffer()
    ser.close()
    log.close()

dut_pwr = DutPwrHost("10.25.26.128")
cycle_count = 0
dut_pwr.off()
time.sleep(0.7)

while True:
    cycle_count = cycle_count + 1
    run_test(cycle_count)
