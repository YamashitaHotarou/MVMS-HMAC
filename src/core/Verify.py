from time import time_ns

from src.support.group import Group


class Verify:
    def __init__(self):
        self.verify_result = False
        self.time = 0

    def verify(self, AV, replicasProof, originalProof):
        start_time = time_ns()
        # print(start_time)
        original_result = 0
        replica_result = 0
        for av in AV:
            temp = Group.multiply_in_group(hex(av.inspection_num), originalProof[str(av.avID)])
            original_result = Group.add_in_group(str(original_result), str(temp))
        for p in replicasProof:
            # print(p.hmac)
            replica_result = Group.add_in_group(p.hmac, str(replica_result))
        end_time = time_ns()
        self.time += (end_time - start_time)
        # print(end_time)
        # print(self.time)
        print(original_result)
        print(replica_result)
        if original_result == replica_result:
            self.verify_result = True
        else:
            self.verify_result = False

    def localization(self, AV, replicasProof, originalProof):
        start_time = time_ns()
        if self.verify_result :
            print("All the edge servers is intact.")
            return None
        corrupted_information = {}
        for av in AV:
            corrupted_information[av.avID] = []
        for p in replicasProof:
            if p.hmac != originalProof[p.avID]:
                corrupted_information[p.avID].append(p.esID)
        end_time = time_ns()
        self.time += (end_time - start_time)
        print("Here is the situation of corruption:")
        for key, value in corrupted_information.items():
            print(f"{key}: {value}")
