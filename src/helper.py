"""
Helper class to call from everywhere
"""

from datetime import datetime

class Helper():

    def __init__(self):
        print("Created Helper...")


    @staticmethod
    def get_current_time():
        """
        Get current system time formated the way needed
        """
        return datetime.now().strftime("[%H:%M:%S]\t")