#Header = bytearray([0xFF, 0x55])
Header = bytearray([255, 85])

#Header_Bytes = ''.join('0x%02x'%i for i in bytearray(Header))
#Header_Bytes = ''
#Header_Bytes.join('0x%02x'%i for i in bytearray([255, 85]))

Default_Timeout = 100

class Mode():
	Mode_Switching 			= bytearray([0x00])
	Voice_Recorder 			= bytearray([0x01])
	Simple_Remote  			= bytearray([0x02])
	Request_Mode_Status 	= bytearray([0x03])
	AiR_Mode 				= bytearray([0x04])

	def __init__(self):
		self.Mode_Switching 		= Mode_Switching
		self.Voice_Recorder 		= Voice_Recorder
		self.Simple_Remote  		= Simple_Remote
		self.Request_Mode_Status 	= Request_Mode_Status
		self.AiR_Mode 				= AiR_Mode


class Command():
	class Mode0():
		Switch_To_AiR_Mode = bytearray([0x01, 0x04])

		def __init__(self):
			self.Switch_To_AiR_Mode = Switch_To_AiR_Mode



def Get_ModeStr(mode):
	if (mode == Mode.Mode_Switching):
		return '0x00: Mode_Switching (mode 0)'
	elif (mode == Voice_Recorder):
		return '0x01: Voice_Recorder (mode 1)'
	elif (mode == Simple_Remote):
		return '0x02: Simple_Remote (mode 2)'
	elif (mode == Request_Mode_Status):
		return '0x03: Request_Mode_Status (mode 3)'
	elif (mode == AiR_Mode):
		return '0x04: AiR_Mode (mode 4)'
	else:
		return 'Invalid mode!'

def Get_CommandStr(mode, command):
	if (mode == Mode.Mode_Switching):
		if (command == Command.Mode0.Switch_To_AiR_Mode):
			return '0x01 0x04: Switch to AiR mode.'
		else:
			return 'Command either invalid or unimplemented!'
	else:
		return 'Mode either invalid or unimplemented!'

#def Get_ByteCount(obj):

def Get_Header_ByteForm():
	sHeader = []
	Header_Bytes = ''

	#NOTE: 255 (dec) is an empty character space as an ascii character, so it will look like nothing displayed!
	#NOTE: 85 (dec) is the uppercase letter U; this is not a U as in some bastardized unicode type-casting bullshit!!!!

	#Header is already casted to a bytearray at the very beginning of this module! No sense calling the function again and wasting cycles!
	for Header_Byte in Header:

		sHeader.append(str([Header_Byte]))
		#NOTE: This does NOT add the values accumulating the integer value, it actually does append, so it's safe to use!!!!!
		Header_Bytes += chr(Header_Byte)

		#print Header_Byte
		#print ('str(Header_Byte):"' + str(Header_Byte) + '"')
		#print ('chr(Header_Byte):"' + chr(Header_Byte) + '"')

	#print ('Get_Header_ByteForm.Header_Bytes:' + Header_Bytes)
	#print ('Get_Header_ByteForm.sHeader:' + str(''.join(sHeader)))

	return Header_Bytes





def Get_Length(mode, command, parameters = None):
	mode_length = Get_ModeLength(mode)

	Length = mode_length + int(Get_CommandLength(command))

	if (parameters != None):
		Length = Length + len(parameters)

	return int(Length)

def Get_Length_As_HexValue(mode, command, parameters = None):
	mode_length = Get_ModeLength(mode)

	iLength = mode_length + int(Get_CommandLength(command))

	if (parameters != None):
		iLength = iLength + len(parameters)

	Length = ''.join('0x%02x'%iLength)

	#print ('Get_Length_As_HexValue.Length:' + Length)

	return Length

def Get_Length_ByteForm(mode, command, parameters = None):
	mode_length = len(mode)
	command_length = len(command)
	Length = mode_length + command_length

	#print ('Get_Length_ByteForm.Length:' + str(Length))

	if (parameters != None):
		#hlength = bytearray([mode.count + command.count + parameters.count])
		Length += len(parameters)

	hLength = bytearray([Length])

	#print ('Get_Length_ByteForm.hLength:' + str(hLength))

	return hLength




def Get_Mode_ByteForm(mode):
	sMode = []
	Mode_Bytes = ''

	for Mode_Byte in mode:

		sMode.append(str([Mode_Byte]))
		#NOTE: This does NOT add the values accumulating the integer value, it actually does append, so it's safe to use!!!!!
		Mode_Bytes += chr(Mode_Byte)

		#print Mode_Byte
		#print ('str(Mode_Byte):"' + str(Mode_Byte) + '"')
		#print ('chr(Mode_Byte):"' + chr(Mode_Byte) + '"')

	#print ('Get_Mode_ByteForm.Mode_Bytes:' + Mode_Bytes)
	#print ('Get_Mode_ByteForm.sMode:' + str(''.join(sMode)))

	return Mode_Bytes


def Get_ModeLength(mode):
	return len(mode)

def Get_ModeLength_ByteForm(mode):
	result = ''.join(chr(v) for v in mode)
	#mode should already be passed in as a bytearray, so no need to call it again; YAY!!!!!
	#	print ('Get_ModeLength_ByteForm:"' + bytearray([mode]) + '"')
	#	return bytearray([mode])
	#NOTE: Mode 0 will appear as an empty space, when in actuality it is a null character space (0x00)
	#keep this in mind when debugging!!!!!!!!!!
	#print ('Get_ModeLength_ByteForm:"' + (''.join(chr(v) for v in mode)) + '"')
	return result




def Get_CommandLength(command):
	if (command == Command.Mode0.Switch_To_AiR_Mode):
		return 0x02
	else:
		return 0x00


def Get_CommandLength_ByteForm(command):
	result = ''.join(chr(v) for v in command)
	#print ('Get_CommandLength_ByteForm:"' + (''.join(chr(v) for v in command)) + '"')
	return result




def Get_Command_ByteForm(command):
	sCommand = []
	Command_Bytes = ''

	for Command_Byte in command:

		sCommand.append(str([Command_Byte]))
		#NOTE: This does NOT add the values accumulating the integer value, it actually does append, so it's safe to use!!!!!
		Command_Bytes += chr(Command_Byte)

		#print Command_Byte
		#print ('str(Command_Byte):"' + str(Command_Byte) + '"')
		#print ('chr(Command_Byte):"' + chr(Command_Byte) + '"')

	#print ('Get_Command_ByteForm.Command_Bytes:' + Command_Bytes)
	#print ('Get_Command_ByteForm.sMode:' + str(''.join(sCommand)))

	return Command_Bytes







def Get_Parameter_ByteForm(parameter):
	sParameter = []
	Parameter_Bytes = ''

	for Parameter_Byte in parameter:

		sParameter.append(str([Parameter_Byte]))
		#NOTE: This does NOT add the values accumulating the integer value, it actually does append, so it's safe to use!!!!!
		Parameter_Bytes += chr(Parameter_Byte)

		#print Parameter_Byte
		#print ('str(Parameter_Byte):"' + str(Parameter_Byte) + '"')
		#print ('chr(Parameter_Byte):"' + chr(Parameter_Byte) + '"')

	#print ('Get_Parameter_ByteForm.Parameter_Bytes:' + Parameter_Bytes)
	#print ('Get_Parameter_ByteForm.sMode:' + str(''.join(sCommand)))

	return Parameter_Bytes






def Checksum(mode, command, parameters = None):
	#New_mode = 
	Length = Get_Length(mode, command, parameters)
	if (parameters != None):
		Length = Length + 1 + Get_CommandLength(command) + parameters
	else:
		Length = Length + 1 + Get_CommandLength(command)

	#TODO: Kludge
		Length = Length + 2

	#Checksum = 0x100 - (byte(Length) & 0xFF)
	Checksum = 256 - (Length & 255)
	#Checksum = \x100 - (Length & \xFF)

	#print ('mode_len: ' + str(mode))
	#print ('command_len: ' + len(command))
	#print ('parameters_len: ' + len(parameters))
	#print Checksum
	return Checksum
	#return int(str(Checksum),16)

def Generate_String(mode, command, parameters = None):
	hBytes_out = Header

	sBytes_out = ''
	Header_Bytes = ''
	CommandBytes = ''


	Index_Count = 0
	for Command_Byte in command:
		if (Index_Count != len(command) - 1):
			CommandBytes += ''.join('0x%02x '%Command_Byte)
		else:
			CommandBytes += ''.join('0x%02x'%Command_Byte)
		Index_Count += 1

	Index_Count = 0
	for i in Header:
		if (Index_Count != len(Header) - 1):
			Header_Bytes += ''.join('0x%02x '%i)
		else:
			Header_Bytes += ''.join('0x%02x'%i)
		Index_Count += 1

	print ('Header_Bytes: \t' 	+ str(Header_Bytes) 									+ ' (' + str(Get_Header_ByteForm()) + ')')
	print ('Length: \t' 		+ str(Get_Length_ByteForm(mode, command, parameters)) 	+ ' (' + str(Get_Length(mode, command, parameters)) + ')')
	print ('Mode: \t\t' 		+ str(Get_ModeStr(mode)))
	print ('Command: \t' 		+ str(Get_CommandStr(mode, command)))
	print ('Checksum: \t' 		+ hex(Checksum(mode, command, parameters)))
	print ('')

	mode_bytes = ''
	Index_Count = 0
	for i in mode:
		if (Index_Count != len(mode) - 1):
			mode_bytes = str(mode_bytes) + ''.join('0x%02x '%i)
		else:
			mode_bytes = str(mode_bytes) + ''.join('0x%02x'%i)
		Index_Count += 1

	#print ('mode_bytes: "' + mode_bytes + '"')
	#print ('mode_bytes_str: "' + str(mode_bytes) + '"')


	#print ('\nPacket: ' + str(Header_Bytes) + ' ' + str(Get_Length_As_HexValue(mode, command, parameters)) + ' ' + str(mode_bytes) + ' ' + str(CommandBytes) + ' ' + str(hex(Checksum(mode, command, parameters))))


	#hBytes_out.append(str(Get_Length_ByteForm(mode, command, parameters)))
	hHeader_Bytes = str(Get_Header_ByteForm())
	#print (hHeader_Bytes)

	hLength = str(Get_Length_ByteForm(mode, command, parameters))
	#print (hLength)

	hMode_Bytes = str(Get_ModeLength_ByteForm(mode))
	#print (hMode_Bytes)

	hCommand_Bytes = str(Get_Command_ByteForm(command))
	#print (hCommand_Bytes)

	#TODO: If parameters DOES equal something, getting to hParameter_Bytes from outside the if-block will need to be solved!!!!
	if (parameters != None):
		hParameter_Bytes = str(Get_Parameter_ByteForm(parameters))
	#	print (hParameter_Bytes)

	hChecksum_Bytes = str(bytearray([(Checksum(mode, command, parameters))]))
	#print (hChecksum_Bytes)



	if (parameters != None):
		hBytes_Out = hHeader_Bytes + hLength + hMode_Bytes + hCommand_Bytes + hParameter_Bytes + hChecksum_Bytes
	else:
		hBytes_Out = hHeader_Bytes + hLength + hMode_Bytes + hCommand_Bytes + hChecksum_Bytes
	print ('hBytes_Out:"' + hBytes_Out + '"')


	sBytes_out = str(Header_Bytes) + ' ' + str(Get_Length_As_HexValue(mode, command, parameters)) + ' ' + str(mode_bytes) + ' ' + str(CommandBytes) + ' ' + str(hex(Checksum(mode, command, parameters)))

	#print (Get_CommandLength(command))

	#if (parameters != None):
	#	sBytes_out = str(Header_Bytes) + str(Get_Length(mode, command, parameters)) + str(mode_bytes) + str(command) + str(parameters) + str(Checksum(mode, command, parameters))
	#	#sBytes_out = str(Header_Bytes) + str(Get_Length_ByteForm(mode, command, parameters)) + str(mode) + str(command) + str(parameters) + str(Checksum(mode, command, parameters))
	#else:
	#	sBytes_out = str(Header_Bytes) + str(Get_Length(mode, command, parameters)) + str(mode_bytes) + str(command) + str(Checksum(mode, command, parameters))
	#	#sBytes_out = str(Header_Bytes) + str(Get_Length_ByteForm(mode, command, parameters)) + str(mode) + str(command) + str(Checksum(mode, command, parameters))
	##sBytes_out = sBytes_out.lstrip(' ')
	#print ('sBytes_out: "' + sBytes_out + '"')
	return sBytes_out