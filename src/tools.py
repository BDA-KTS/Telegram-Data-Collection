
from datetime import datetime
import base64

def convert_datetime_to_string(obj):
    """
       Convert a datetime object to a string representation.

       Parameters:
           obj (datetime): The datetime object to be converted.

       Returns:
           str: A string representation of the datetime object in the format 'YYYY-MM-DD HH:MM:SS.microseconds'.
    """
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S.%f')



def convert_bytes_to_base64(data):
    """
        Convert bytes data to a Base64-encoded string.

        Parameters:
            data (bytes): The bytes data to be encoded.

        Returns:
            str: A Base64-encoded string representation of the bytes data.
    """
    return base64.b64encode(data).decode('utf-8')

def convert_dict_datetime_to_string(data):
    """
        Recursively convert datetime objects within a dictionary to string representations,
        and bytes objects to Base64-encoded strings.

        Parameters:
            data (dict): The dictionary containing datetime and bytes objects to be converted.

        Returns:
            dict: The modified dictionary with datetime objects converted to strings and bytes objects encoded in Base64.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = convert_dict_datetime_to_string(value)
            elif isinstance(value, list):
                data[key] = [convert_dict_datetime_to_string(item) for item in value]
            elif isinstance(value, datetime):
                data[key] = convert_datetime_to_string(value)
            elif isinstance(value, bytes):
                data[key] = convert_bytes_to_base64(value)
    return data
