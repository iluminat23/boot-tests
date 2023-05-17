# Scripts to run continuous tests

## Linux kernel boot, serial log

The `boot_test_serial.py` script logs the boot messages from the Linux kernel over a serial
connection. The script uses a RevPi Connect to reboot the system. The log output is used to determine when the system should be rebooted. The reboot is done when the first message of systemd is printed in the log. Or a kernel panic occurred.

Every boot cycle is written to its own log file. The naming scheme is as follows:
`{cycle_count:04}_{timestamp}_serial.log`
