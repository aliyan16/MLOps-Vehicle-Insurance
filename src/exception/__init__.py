import sys
import logging

def errorMessageDetail(error:Exception,error_detail:sys)->str:
    """Extracts detailed error information including file name, line number, and the error message """
    _,_,excTb=error_detail.exc_info()
    fileName=excTb.tb_frame.f_code.co_filename
    lineNumber=excTb.tb_lineno
    errorMessage=f'Error occured in python Script: [{fileName}] at line number [{lineNumber}]: {str(error)}'
    logging.error(errorMessage)
    return errorMessage

class MyException(Exception):
    """Custom exception class for handling errors in application"""
    def __init__(self,errorMessage:str,errorDetail:sys):
        """initializes the Exception with detail error message"""
        super().__init__(errorMessage)
        self.errorMessage=errorMessageDetail(errorMessage,errorDetail)

    def __str__(self)->str:
        """returns the string representaion of the error message"""
        return self.errorMessage