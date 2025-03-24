import random
from time import time_ns

from src.core.EdgeServer import getMinNRS
from src.core.proof import ReplicasProof
from src.support.hmac_sha256 import HMAC_SHA256


class ProofGeneration:
    def __init__(self):
        self.time = 0

    def keyGeneration(self, key_length):
        chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = ''.join(random.choice(chars) for _ in range(key_length))
        return key

    def proofGeneration(self, AV, key):
        #Choose the edge servers for inspection
        start_time = time_ns()
        inspection_servers = []
        proof = []
        for av in AV:
            temp = getMinNRS(av.ES, av.inspection_num)
            inspection_servers = list(set(inspection_servers).union(temp))

        end_time = time_ns()
        self.time += (end_time - start_time)/len(AV)
        # print(self.time)

        temp_time = 0
        for ss in inspection_servers:
            for avID, filePath in ss.replicas.items():
                file_content = HMAC_SHA256.read_file_content(filePath)
                start_time = time_ns()
                hmac = HMAC_SHA256.calculate_hmac_sha256(file_content, key)
                temp_proof = ReplicasProof(ss.esID, avID, hmac)
                proof.append(temp_proof)
                end_time = time_ns()
                temp_time += (end_time - start_time)
        self.time += temp_time/len(inspection_servers)
        # print(temp_time/len(inspection_servers))

        return proof
