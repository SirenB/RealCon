import pyvisa


class keysight34410A(object):
	"""
	keysight34410A brief introduction
	"""
	def __init__(self, gpib_addr):

		rm = pyvisa.ResourceManager()
		self.dev = rm.open_resource('GPIB0::%i::INSTR' % gpib_addr)

	def clear(self):
		self.dev.write('*CLS')

	def getid(self):
		self.id = self.dev.query('*IDN?')
		# print(self.id)
		return self.id

	def getV(self):
		self.v = self.dev.query('MEASure:VOLTage:DC?')
		return self.v

	def getI(self):
		self.I = self.dev.query('MEASure:CURRent:DC?')
		return self.I