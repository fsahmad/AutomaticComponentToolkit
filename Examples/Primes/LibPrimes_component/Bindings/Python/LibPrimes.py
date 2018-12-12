'''++

Copyright (C) 2018 Automatic Component Toolkit Developers

All rights reserved.

This file has been generated by the Automatic Component Toolkit (ACT) version 1.3.0.

Abstract: This is an autogenerated Python file in order to allow an easy
 use of Prime Numbers Interface

Interface version: 1.3.0

'''


import ctypes
import platform
import enum

'''Definition of domain specific exception
'''
class ELibPrimesException(Exception):
	def __init__(self, code, message = ''):
		self._code = code
		self._message = message
	
	def __str__(self):
		if self._message:
			return 'LibPrimesException ' + str(self._code) + ': '+ str(self._message)
		return 'LibPrimesException ' + str(self._code)

'''Definition Error Codes
'''
class LibPrimesErrorCodes(enum.IntEnum):
	SUCCESS = 0
	NOTIMPLEMENTED = 1
	INVALIDPARAM = 2
	INVALIDCAST = 3
	BUFFERTOOSMALL = 4
	GENERICEXCEPTION = 5
	COULDNOTLOADLIBRARY = 6
	COULDNOTFINDLIBRARYEXPORT = 7
	NORESULTAVAILABLE = 8
	CALCULATIONABORTED = 9

'''Definition of Structs
'''
'''Definition of LibPrimesPrimeFactor
'''
class LibPrimesPrimeFactor(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
		("Prime", ctypes.c_uint64), 
		("Multiplicity", ctypes.c_uint32)
	]

'''Definition of Function Types
'''
'''Definition of LibPrimesProgressCallback
		Callback to report calculation progress and query whether it should be aborted
'''
LibPrimesProgressCallback = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_float, ctypes.POINTER(ctypes.c_bool))


'''Wrapper Class Implementation
'''
class LibPrimesWrapper:

	def __init__(self, libraryName):
		ending = ''
		if platform.system() == 'Windows':
			ending = 'dll'
		elif platform.system() == 'Linux':
			ending = 'so'
		elif platform.system() == 'Darwin':
			ending = 'dylib'
		else:
			raise ELibPrimesException(LibPrimesErrorCodes.COULDNOTLOADLIBRARY)
		
		path = libraryName + '.' + ending
		
		try:
			self.lib = ctypes.CDLL(path)
		except Exception as e:
			raise ELibPrimesException(LibPrimesErrorCodes.COULDNOTLOADLIBRARY, str(e) + '| "'+path + '"' )
		
		self._loadFunctionTable()
	
	def _loadFunctionTable(self):
		try:
			self.lib.libprimes_createfactorizationcalculator.restype = ctypes.c_int64
			self.lib.libprimes_createfactorizationcalculator.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
			
			self.lib.libprimes_createsievecalculator.restype = ctypes.c_int64
			self.lib.libprimes_createsievecalculator.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
			
			self.lib.libprimes_releaseinstance.restype = ctypes.c_int64
			self.lib.libprimes_releaseinstance.argtypes = [ctypes.c_void_p]
			
			self.lib.libprimes_getlibraryversion.restype = ctypes.c_int64
			self.lib.libprimes_getlibraryversion.argtypes = [ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32)]
			
			self.lib.libprimes_setjournal.restype = ctypes.c_int64
			self.lib.libprimes_setjournal.argtypes = [ctypes.c_char_p]
			
			self.lib.libprimes_calculator_getvalue.restype = ctypes.c_int64
			self.lib.libprimes_calculator_getvalue.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64)]
			
			self.lib.libprimes_calculator_setvalue.restype = ctypes.c_int64
			self.lib.libprimes_calculator_setvalue.argtypes = [ctypes.c_void_p, ctypes.c_uint64]
			
			self.lib.libprimes_calculator_setprogresscallback.restype = ctypes.c_int64
			self.lib.libprimes_calculator_setprogresscallback.argtypes = [ctypes.c_void_p, LibPrimesProgressCallback]
			
			self.lib.libprimes_calculator_calculate.restype = ctypes.c_int64
			self.lib.libprimes_calculator_calculate.argtypes = [ctypes.c_void_p]
			
			self.lib.libprimes_factorizationcalculator_getprimefactors.restype = ctypes.c_int64
			self.lib.libprimes_factorizationcalculator_getprimefactors.argtypes = [ctypes.c_void_p, ctypes.c_uint64, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(LibPrimesPrimeFactor)]
			
			self.lib.libprimes_factorizationcalculator_checkprimefactors.restype = ctypes.c_int64
			self.lib.libprimes_factorizationcalculator_checkprimefactors.argtypes = [ctypes.c_void_p, ctypes.c_uint64, ctypes.POINTER(LibPrimesPrimeFactor), ctypes.POINTER(ctypes.c_bool)]
			
			self.lib.libprimes_sievecalculator_getprimes.restype = ctypes.c_int64
			self.lib.libprimes_sievecalculator_getprimes.argtypes = [ctypes.c_void_p, ctypes.c_uint64, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64)]
			
		except AttributeError as ae:
			raise ELibPrimesException(LibPrimesErrorCodes.COULDNOTFINDLIBRARYEXPORT, ae.args[0])
	
	def checkError(self, instance, errorCode):
		if instance:
			if instance._wrapper != self:
				raise ELibPrimesException(LibPrimesErrorCodes.INVALIDCAST, 'invalid wrapper call')
		if errorCode != LibPrimesErrorCodes.SUCCESS.value:
			raise ELibPrimesException(errorCode)
	
	def CreateFactorizationCalculator(self):
		InstanceHandle = ctypes.c_void_p()
		self.checkError(None, self.lib.libprimes_createfactorizationcalculator(InstanceHandle))
		InstanceObject = LibPrimesFactorizationCalculator(InstanceHandle, self)
		return InstanceObject
	
	def CreateSieveCalculator(self):
		InstanceHandle = ctypes.c_void_p()
		self.checkError(None, self.lib.libprimes_createsievecalculator(InstanceHandle))
		InstanceObject = LibPrimesSieveCalculator(InstanceHandle, self)
		return InstanceObject
	
	def ReleaseInstance(self, InstanceObject):
		self.checkError(None, self.lib.libprimes_releaseinstance(InstanceObject._handle))
	
	def GetLibraryVersion(self):
		pMajor = ctypes.c_uint32()
		pMinor = ctypes.c_uint32()
		pMicro = ctypes.c_uint32()
		self.checkError(None, self.lib.libprimes_getlibraryversion(pMajor, pMinor, pMicro))
		return pMajor.value, pMinor.value, pMicro.value
	
	def SetJournal(self, FileName):
		pFileName = ctypes.c_char_p(str.encode(FileName))
		self.checkError(None, self.lib.libprimes_setjournal(pFileName))
	
'''Base Class Implementation
'''
class LibPrimesBaseClass():
	def __init__(self, handle, wrapper):
		if not handle or not wrapper:
			raise ELibPrimesException()
		self._handle = handle
		self._wrapper = wrapper
	
	def __del__(self):
		self._wrapper.ReleaseInstance(self)


'''Calculator Class Implementation
'''
class LibPrimesCalculator(LibPrimesBaseClass):
	def __init__(self, handle, wrapper):
		LibPrimesBaseClass.__init__(self, handle, wrapper)
	
	def GetValue(self):
		pValue = ctypes.c_uint64()
		self._wrapper.checkError(self, self._wrapper.lib.libprimes_calculator_getvalue(self._handle, pValue))
		return pValue.value
	
	def SetValue(self, Value):
		nValue = ctypes.c_uint64(Value)
		self._wrapper.checkError(self, self._wrapper.lib.libprimes_calculator_setvalue(self._handle, nValue))
	
	def SetProgressCallback(self, ProgressCallbackFunc):
		self._wrapper.checkError(self, self._wrapper.lib.libprimes_calculator_setprogresscallback(self._handle, ProgressCallbackFunc))
	
	def Calculate(self):
		self._wrapper.checkError(self, self._wrapper.lib.libprimes_calculator_calculate(self._handle))
	


'''FactorizationCalculator Class Implementation
'''
class LibPrimesFactorizationCalculator(LibPrimesCalculator):
	def __init__(self, handle, wrapper):
		LibPrimesBaseClass.__init__(self, handle, wrapper)
	
	def GetPrimeFactors(self):
		nPrimeFactorsCount = ctypes.c_uint64(0)
		nPrimeFactorsNeededCount = ctypes.c_uint64(0)
		pPrimeFactorsBuffer = (LibPrimesPrimeFactor*0)()
		self._wrapper.checkError(self, self._wrapper.lib.libprimes_factorizationcalculator_getprimefactors(self._handle, nPrimeFactorsCount, nPrimeFactorsNeededCount, pPrimeFactorsBuffer))
		nPrimeFactorsCount = ctypes.c_uint64(nPrimeFactorsNeededCount.value)
		pPrimeFactorsBuffer = (LibPrimesPrimeFactor * nPrimeFactorsNeededCount.value)()
		self._wrapper.checkError(self, self._wrapper.lib.libprimes_factorizationcalculator_getprimefactors(self._handle, nPrimeFactorsCount, nPrimeFactorsNeededCount, pPrimeFactorsBuffer))
		return [pPrimeFactorsBuffer[i] for i in range(nPrimeFactorsNeededCount.value)]
	
	def CheckPrimeFactors(self, PrimeFactors):
		nPrimeFactorsCount = ctypes.c_uint64(len(PrimeFactors))
		pPrimeFactorsBuffer = (LibPrimesPrimeFactor*len(PrimeFactors))(*PrimeFactors)
		pAreEqual = ctypes.c_bool()
		self._wrapper.checkError(self, self._wrapper.lib.libprimes_factorizationcalculator_checkprimefactors(self._handle, nPrimeFactorsCount, pPrimeFactorsBuffer, pAreEqual))
		return pAreEqual.value
	


'''SieveCalculator Class Implementation
'''
class LibPrimesSieveCalculator(LibPrimesCalculator):
	def __init__(self, handle, wrapper):
		LibPrimesBaseClass.__init__(self, handle, wrapper)
	
	def GetPrimes(self):
		nPrimesCount = ctypes.c_uint64(0)
		nPrimesNeededCount = ctypes.c_uint64(0)
		pPrimesBuffer = (ctypes.c_uint64*0)()
		self._wrapper.checkError(self, self._wrapper.lib.libprimes_sievecalculator_getprimes(self._handle, nPrimesCount, nPrimesNeededCount, pPrimesBuffer))
		nPrimesCount = ctypes.c_uint64(nPrimesNeededCount.value)
		pPrimesBuffer = (ctypes.c_uint64 * nPrimesNeededCount.value)()
		self._wrapper.checkError(self, self._wrapper.lib.libprimes_sievecalculator_getprimes(self._handle, nPrimesCount, nPrimesNeededCount, pPrimesBuffer))
		return [pPrimesBuffer[i] for i in range(nPrimesNeededCount.value)]
	
		
