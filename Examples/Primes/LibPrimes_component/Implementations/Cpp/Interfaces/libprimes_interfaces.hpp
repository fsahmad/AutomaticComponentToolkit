/*++

Copyright (C) 2019 PrimeDevelopers

All rights reserved.

This file has been generated by the Automatic Component Toolkit (ACT) version 1.6.0.

Abstract: This is an autogenerated C++ header file in order to allow easy
development of Prime Numbers Library. The implementer of Prime Numbers Library needs to
derive concrete classes from the abstract classes in this header.

Interface version: 1.2.0

*/


#ifndef __LIBPRIMES_CPPINTERFACES
#define __LIBPRIMES_CPPINTERFACES

#include <string>
#include <memory>

#include "libprimes_types.hpp"



namespace LibPrimes {
namespace Impl {

/**
 Forward declarations of class interfaces
*/
class IBase;
class ICalculator;
class IFactorizationCalculator;
class ISieveCalculator;



/*************************************************************************************************************************
 Class interface for Base 
**************************************************************************************************************************/

class IBase {
public:
	/**
	* IBase::~IBase - virtual destructor of IBase
	*/
	virtual ~IBase() {};

	/**
	* IBase::ReleaseBaseClassInterface - Releases ownership of a base class interface. Deletes the reference, if necessary.
	* @param[in] pIBase - The base class instance to release
	*/
	static void ReleaseBaseClassInterface(IBase* pIBase)
	{
		if (pIBase) {
			pIBase->DecRefCount();
		}
	};

	/**
	* IBase::AcquireBaseClassInterface - Acquires shared ownership of a base class interface.
	* @param[in] pIBase - The base class instance to acquire
	*/
	static void AcquireBaseClassInterface(IBase* pIBase)
	{
		if (pIBase) {
			pIBase->IncRefCount();
		}
	};


	/**
	* IBase::GetLastErrorMessage - Returns the last error registered of this class instance
	* @param[out] sErrorMessage - Message of the last error registered
	* @return Has an error been registered already
	*/
	virtual bool GetLastErrorMessage(std::string & sErrorMessage) = 0;

	/**
	* IBase::ClearErrorMessages - Clears all registered messages of this class instance
	*/
	virtual void ClearErrorMessages() = 0;

	/**
	* IBase::RegisterErrorMessage - Registers an error message with this class instance
	* @param[in] sErrorMessage - Error message to register
	*/
	virtual void RegisterErrorMessage(const std::string & sErrorMessage) = 0;

	/**
	* IBase::IncRefCount - Increases the reference count of a class instance
	*/
	virtual void IncRefCount() = 0;

	/**
	* IBase::DecRefCount - Decreases the reference count of a class instance and free releases it, if the last reference has been removed
	* @return Has the object been released
	*/
	virtual bool DecRefCount() = 0;
};


/**
 Definition of a shared pointer class for IBase
*/
template<class T>
class IBaseSharedPtr : public std::shared_ptr<T>
{
public:
	explicit IBaseSharedPtr(T* t = nullptr)
		: std::shared_ptr<T>(t, IBase::ReleaseBaseClassInterface)
	{
		t->IncRefCount();
	}

	// Reset function, as it also needs to properly set the deleter.
	void reset(T* t = nullptr)
	{
		std::shared_ptr<T>::reset(t, IBase::ReleaseBaseClassInterface);
	}

	// Get-function that increases the Base class's reference count
	T* getCoOwningPtr()
	{
		T* t = this->get();
		t->IncRefCount();
		return t;
	}
};


typedef IBaseSharedPtr<IBase> PIBase;


/*************************************************************************************************************************
 Class interface for Calculator 
**************************************************************************************************************************/

class ICalculator : public virtual IBase {
public:
	/**
	* ICalculator::GetValue - Returns the current value of this Calculator
	* @return The current value of this Calculator
	*/
	virtual LibPrimes_uint64 GetValue() = 0;

	/**
	* ICalculator::SetValue - Sets the value to be factorized
	* @param[in] nValue - The value to be factorized
	*/
	virtual void SetValue(const LibPrimes_uint64 nValue) = 0;

	/**
	* ICalculator::Calculate - Performs the specific calculation of this Calculator
	*/
	virtual void Calculate() = 0;

	/**
	* ICalculator::SetProgressCallback - Sets the progress callback function
	* @param[in] pProgressCallback - callback function
	*/
	virtual void SetProgressCallback(const LibPrimes::ProgressCallback pProgressCallback) = 0;

};

typedef IBaseSharedPtr<ICalculator> PICalculator;


/*************************************************************************************************************************
 Class interface for FactorizationCalculator 
**************************************************************************************************************************/

class IFactorizationCalculator : public virtual ICalculator {
public:
	/**
	* IFactorizationCalculator::GetPrimeFactors - Returns the prime factors of this number (without multiplicity)
	* @param[in] nPrimeFactorsBufferSize - Number of elements in buffer
	* @param[out] pPrimeFactorsNeededCount - will be filled with the count of the written structs, or needed buffer size.
	* @param[out] pPrimeFactorsBuffer - PrimeFactor buffer of The prime factors of this number
	*/
	virtual void GetPrimeFactors(LibPrimes_uint64 nPrimeFactorsBufferSize, LibPrimes_uint64* pPrimeFactorsNeededCount, LibPrimes::sPrimeFactor * pPrimeFactorsBuffer) = 0;

};

typedef IBaseSharedPtr<IFactorizationCalculator> PIFactorizationCalculator;


/*************************************************************************************************************************
 Class interface for SieveCalculator 
**************************************************************************************************************************/

class ISieveCalculator : public virtual ICalculator {
public:
	/**
	* ISieveCalculator::GetPrimes - Returns all prime numbers lower or equal to the sieve's value
	* @param[in] nPrimesBufferSize - Number of elements in buffer
	* @param[out] pPrimesNeededCount - will be filled with the count of the written structs, or needed buffer size.
	* @param[out] pPrimesBuffer - uint64 buffer of The primes lower or equal to the sieve's value
	*/
	virtual void GetPrimes(LibPrimes_uint64 nPrimesBufferSize, LibPrimes_uint64* pPrimesNeededCount, LibPrimes_uint64 * pPrimesBuffer) = 0;

};

typedef IBaseSharedPtr<ISieveCalculator> PISieveCalculator;


/*************************************************************************************************************************
 Global functions declarations
**************************************************************************************************************************/
class CWrapper {
public:
	/**
	* Ilibprimes::GetVersion - retrieves the binary version of this library.
	* @param[out] nMajor - returns the major version of this library
	* @param[out] nMinor - returns the minor version of this library
	* @param[out] nMicro - returns the micro version of this library
	*/
	static void GetVersion(LibPrimes_uint32 & nMajor, LibPrimes_uint32 & nMinor, LibPrimes_uint32 & nMicro);

	/**
	* Ilibprimes::GetLastError - Returns the last error recorded on this object
	* @param[in] pInstance - Instance Handle
	* @param[out] sErrorMessage - Message of the last error
	* @return Is there a last error to query
	*/
	static bool GetLastError(IBase* pInstance, std::string & sErrorMessage);

	/**
	* Ilibprimes::AcquireInstance - Acquire shared ownership of an Instance
	* @param[in] pInstance - Instance Handle
	*/
	static void AcquireInstance(IBase* pInstance);

	/**
	* Ilibprimes::ReleaseInstance - Releases shared ownership of an Instance
	* @param[in] pInstance - Instance Handle
	*/
	static void ReleaseInstance(IBase* pInstance);

	/**
	* Ilibprimes::CreateFactorizationCalculator - Creates a new FactorizationCalculator instance
	* @return New FactorizationCalculator instance
	*/
	static IFactorizationCalculator * CreateFactorizationCalculator();

	/**
	* Ilibprimes::CreateSieveCalculator - Creates a new SieveCalculator instance
	* @return New SieveCalculator instance
	*/
	static ISieveCalculator * CreateSieveCalculator();

};

} // namespace Impl
} // namespace LibPrimes

#endif // __LIBPRIMES_CPPINTERFACES
