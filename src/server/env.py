import sys
import  os
sys.path.append(os.path.abspath(os.path.join(os.path.pardir,"../config")))
from server_setting import settings

settings = settings

if __name__ == "__main__":
    print settings
