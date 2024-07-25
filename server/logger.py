import sys

class Logger():
    def debug(self, message: str):
        print(f'[DEBUG] {message}', file=sys.stderr)
        
    def error(self, message: str):
        print(f'[ERROR] {message}', file=sys.stderr)
        
    def warn(self, message: str):
        print(f'[WARN] {message}', file=sys.stderr)
        
    def info(self, message: str):
        print(f'[INFO] {message}', file=sys.stderr)


logger = Logger()