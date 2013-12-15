#!/usr/bin/env python
#
# Based on http://ubuntuforums.org/showthread.php?t=1695571&p=10497873#post10497873
# thx kostkon!
# requires python-gudev package
#
# working with udev through python and checking new devices
#

import glib
import gudev
import sys
temp = "DEVPATH"

def callback(client, action, device, user_data):
    device_vendor = device.get_property("ID_VENDOR_ENC")
    device_model = device.get_property("ID_MODEL_ENC")
    device_interface = device.get_property(temp)

#    device_interface = device.get_property("DEVPATH")
    if action == "add":
        print device_vendor
	print device_model
	print device_interface

    elif action == "remove":
	print "noo"

client = gudev.Client(["usb/usb_device"])
client.connect("uevent", callback, None)

loop = glib.MainLoop()
loop.run()
