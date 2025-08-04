import os
import sys
# os.path.abspath(__file__)

# print(os.path.abspath(__file__))

# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from module import main_gz


#print(sys.path)

main_gz.main_gz()