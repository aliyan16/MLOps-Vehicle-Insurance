import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

LogDir='logs'
logFile=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
maxLogSize=5*1024
backupCount=3

logDirPath=os.path.join(from_root(),LogDir)
os.makedirs(logDirPath,exist_ok=True)
logFilePath=os.path.join(logDirPath,logFile)

def configureLogger():
    """Configures logging with a rotating file handler and a console handler"""
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter=logging.Formatter("[%(asctime)s] %(name)s-%(levelname)s - %(message)s")
    fileHandler=RotatingFileHandler(logFilePath,maxBytes=maxLogSize,backupCount=backupCount)
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)

    consoleHandler=logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(formatter)

    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)

configureLogger()
