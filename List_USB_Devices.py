import usb.core
import usb.util
#import usb.backend.libusb1

import sys

import Dump_Obj
#from Dump_Obj import dumpObj

from USB_IDs import hVendorIDs, iVendorIDs, sVendors, hProdIDs, iProdIDs, sProdIDs
#from Apple_aap_iap import Header, Mode, Command
import Apple_aap_iap

#backend = usb.backend.libusb1.get_backend(find_library=lambda x: "libusb-1.0.dll")

USB_Devices = usb.core.find(find_all=True)
#USB_Devices = usb.core.find(find_all=True, backend=backend)
sys.stdout.write('\nUSB Devices attached to system:\n\n')

cfg_index = -1
iPod_Video_USBDevice_Index = -1

iPod_Video = ''

# loop through devices, printing vendor and product ids in decimal and hex
for cfg in USB_Devices:
    sys.stdout.write('VendorID='    + hex(cfg.idVendor)     + ' (' + str(cfg.idVendor)  + ')\n')
    sys.stdout.write('ProductID='   + hex(cfg.idProduct)    + ' (' + str(cfg.idProduct) + ')\n')
    
    cfg_index += 1

    if ( (cfg.idVendor == 1452) and (cfg.idProduct == 4617) ):
        iPod_Video = cfg
        iPod_Video_USBDevice_Index = cfg_index

    if cfg._manufacturer is None:
        try:
            cfg._manufacturer = usb.util.get_string(cfg, cfg.iManufacturer)
        except:
            try:
                Vendor_Index = hVendorIDs.index(hex(cfg.idVendor))
                if (Vendor_Index != None):
                    cfg._manufacturer = sVendors[Vendor_Index]
                else:
                    cfg._manufacturer = 'Vendor ID lookup entry not found!'
            except:
                cfg._manufacturer = 'error determining manufacturer!'

    if cfg._product is None:
        try:
            cfg._product = usb.util.get_string(cfg, cfg.iProduct)
        except:
            try:
                Prod_Index = hProdIDs.index(hex(cfg.idProduct))
                if (Prod_Index != None):
                    cfg._product = sProdIDs[Prod_Index]
                else:
                    cfg._product = 'Product ID lookup entry not found!'
            except:
                cfg._product = 'error determining product!'




    if cfg._manufacturer == None:
        print ('Manufacturer: \t  <none>')
    else:
        print ('Manufacturer: \t  ' + cfg._manufacturer)

    if cfg._product == None:
        print ('Product: \t  <none>')
    else:
        print ('Product: \t  ' + cfg._product)

    sys.stdout.write('Device Class: \t  '   + str(cfg.bDeviceClass)     + '\n')
    sys.stdout.write('Device SubClass:  '   + str(cfg.bDeviceSubClass)  + '\n')
    sys.stdout.write('Device Protocol:  '   + str(cfg.bDeviceProtocol)  + '\n')
    sys.stdout.write('Bus: \t\t  '          + str(cfg.bus)              + '\n')
    sys.stdout.write('Address: \t  '        + str(cfg.address)          + '\n')
    sys.stdout.write('Serial: \t  '         + str(cfg.iSerialNumber)    + '\n')
    #sys.stdout.write('Product: ' + str(cfg.product))

    #print ('Descriptors: ')
    #Desc = usb.util.find_descriptor(cfg, find_all=True)
    #Dump_Obj.dumpObj(cfg)
    #print(dir(cfg))
    Descriptor_Count = 0
    Descriptors = dir(cfg)
    for Descript in Descriptors:
        #print (Descript);
        Descriptor_Count += 1

    #This count is WAY wrong!
        #print ('Descriptor count: ' + str(len(Descript)))
    print ('Descriptor count: ' + str(Descriptor_Count) + '\n\n')

    #for intf in cfg:
    #    print (str(intf))

    #Descriptors = usb.util.find_descriptor(cfg)
    #for Descript in Descriptors:
    #    print (str(Descript))

    #Apple Vendor ID = 0x5ac (1452)
    #iPod Video = 0x1209 (4617)

if ( (iPod_Video != None) and (iPod_Video_USBDevice_Index > -1) ):
    print ('\nApple iPod Video found at cfg index: ' + str(iPod_Video_USBDevice_Index) + '!')
    print ('Note: index is 0-based.')

    print ('\n\nSending Mode switching bytes to iPod Video now...')
    
    #mode = Apple_aap_iap.Mode.AiR_Mode
    #cmd = Apple_aap_iap.Command.Mode0.Switch_To_AiR_Mode

    #hBytes_Out = str(Apple_aap_iap.Header) + str(0x03) + str(mode) + str(cmd) + str(Apple_aap_iap.Checksum(mode, cmd))
    #Apple_aap_iap.Generate_String(Apple_aap_iap.Mode.AiR_Mode, Apple_aap_iap.Command.Mode0.Switch_To_AiR_Mode)
    

    Cmd_String = Apple_aap_iap.Generate_String(Apple_aap_iap.Mode.Mode_Switching, Apple_aap_iap.Command.Mode0.Switch_To_AiR_Mode)
    print ('Command string: ' + str(Cmd_String) + '\n')
    iPod_Video.write(1, Cmd_String, Apple_aap_iap.Default_Timeout)
    ret = iPod_Video.read(0x81, len(hBytes_out), Apple_aap_iap.Default_Timeout)

    print ('USB device response: ' + str(ret) + '\n')
else:
    print ('Apple iPod Video not found!')
