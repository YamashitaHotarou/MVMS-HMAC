from sre_constants import error
from time import time_ns

import random

from src.support.hmac_sha256 import HMAC_SHA256


class Setup:
    def __init__(self):
        self.time = 0

    def keyGeneration(self, key_length):
        chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = ''.join(random.choice(chars) for _ in range(key_length))
        return key

    def setup(self, AV, key_length):
        start_time = time_ns()
        key = self.keyGeneration(key_length)
        end_time = time_ns()
        self.time += (end_time - start_time)

        # Read the original data
        for av in AV:
            file_content = HMAC_SHA256.read_file_content(av.filePath)
            start_time = time_ns()
            original_hmac = HMAC_SHA256.calculate_hmac_sha256(file_content,key)
            end_time = time_ns()
            self.time += (end_time - start_time)
            vote_count = 0
            temp_time = 0
            for es in av.ES:
                file_content = HMAC_SHA256.read_file_content(es.replicas[str(av.avID)])
                start_time = time_ns()
                replica_hmac = HMAC_SHA256.calculate_hmac_sha256(file_content,key)
                if replica_hmac == original_hmac:
                    vote_count += 1
                else:
                    es.reliableScore = 0
                end_time = time_ns()
                temp_time += (end_time - start_time)
                if vote_count >= len(av.ES)/2:
                    break
            self.time += temp_time/len(av.ES)
            if vote_count < len(av.ES)/2:
                raise error("The original data has not passed the verification.")








