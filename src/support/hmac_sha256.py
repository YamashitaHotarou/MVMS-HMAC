import hmac
import hashlib


class HMAC_SHA256:

    @staticmethod
    def read_file_content(filePath):
        # Read file and return the content in bytes
        with open(filePath, 'rb') as file:
            return file.read()

    @staticmethod
    def calculate_hmac_sha256(file_content, secret_key):
        key = secret_key.encode()
        hmac_obj = hmac.new(key, file_content, digestmod=hashlib.sha256)
        return hmac_obj.hexdigest()




