import logging
import settings.settings as settings
import os
import sys

class LoggerFactory(object) :
    logbot = None
    
    @staticmethod
    def create_logger() :
        # 루트 로거 생성
        LoggerFactory.logbot = logging.getLogger()
        LoggerFactory.logbot.setLevel(settings.log_level)
        
        # 로그 폴더 있는지 확인
        if not os.path.exists(settings.logpath):
            # Cannot log here yet as handlers are not configured
            os.makedirs(settings.logpath, exist_ok=True)

        # 로그 포맷 생성
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s-%(funcName)s:%(lineno)s] >> %(message)s')    
        
        # 핸들러 생성
        # On Windows, stdout/stderr might not be UTF-8 by default.
        # Reconfigure them to enforce UTF-8 for cross-platform consistency.
        try:
            if sys.stdout:
                sys.stdout.reconfigure(encoding='utf-8')
            if sys.stderr:
                sys.stderr.reconfigure(encoding='utf-8')
        except TypeError:
            # In some environments (like non-interactive), reconfigure might not be available
            # or might fail. The PYTHONIOENCODING env var should handle this.
            pass

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        file_handler = logging.FileHandler(os.path.join(settings.logpath, settings.logfile), encoding='utf-8')
        file_handler.setFormatter(formatter)
        
        # Clear existing handlers to avoid duplication
        if LoggerFactory.logbot.hasHandlers():
            LoggerFactory.logbot.handlers.clear()
            
        LoggerFactory.logbot.addHandler(stream_handler)
        LoggerFactory.logbot.addHandler(file_handler)
        
    @classmethod
    def get_logger(cls) :
        return cls.logbot