#!/bin/sh
ip link set dev eth0 down
ip link set dev eth0 address AA:BB:CC:11:22:33
ip link set dev eth0 up
ip link show eth0
