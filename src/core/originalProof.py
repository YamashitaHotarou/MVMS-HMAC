from time import time_ns


from src.support.hmac_sha256 import HMAC_SHA256


class OriginalProof:
    def __init__(self):
        self.time = 0

    def getOriginalProof(self, AV, key):
        originalProof = {}
        for av in AV:
            file_content = HMAC_SHA256.read_file_content(av.filePath)
            start_time = time_ns()
            hmac = HMAC_SHA256.calculate_hmac_sha256(file_content, key)
            originalProof[str(av.avID)] = hmac
            end_time = time_ns()
            self.time += (end_time - start_time)
        self.time /= len(AV)
        return originalProof