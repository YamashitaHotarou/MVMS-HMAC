from datetime import datetime

import numpy as np
import random
import os


from src.core.AppVendor import AppVendor
from src.core.EdgeServer import EdgeServer
from src.core.Setup import Setup
from src.core.Verify import Verify
from src.core.originalProof import OriginalProof
from src.core.proofGeneration import ProofGeneration

from src.support.getReliableScore import getReliableScore


class Benchmark:
    def __init__(self, av_num, es_num, data_size, inspection_num, original_file_path, replica_file_path):
        self.av_num = av_num
        self.es_num = es_num
        self.data_size = data_size
        self.inspection_num = int(inspection_num*self.es_num)
        self.original_file_path = original_file_path
        self.replica_file_path = replica_file_path
        self.key_length = 256
        self.rs_weight = 0.5
        self.exp_time = 50

    def main(self):
        # self.av_num = int(input("Please enter the number of app vendors: "))
        # self.es_num = int(input("Please enter the number of edge servers: "))
        # self.data_size = input("Please enter the data size: ")
        # self.inspection_num = int(input("Please enter the inspection number: "))
        # self.original_file_path = input("Please enter the original file path: ").strip()
        # self.replica_file_path = input("Please enter the replica file path: ").strip()
        # self.exp_time = int(input("Please enter the experiment times: "))
        print(self.es_num)
        self.run()
        return 0

    def run(self):
        AV=[]
        ES=[]
        for i in range(self.es_num):
            es = EdgeServer(i, {})
            for j in range(self.av_num):
                es.replicas[str(j)] = self.replica_file_path
            ut = random.randint(0, 1000)
            qos = random.randint(0, 100)
            es.reliableScore = getReliableScore(ut, qos, self.rs_weight)
            ES.append(es)
        for i in range(self.av_num):
            av = AppVendor(i, ES, self.original_file_path, self.inspection_num)
            AV.append(av)

        process_time = np.zeros((self.exp_time, 4))
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for t in range(self.exp_time):
            self.process(ES,AV, t, process_time)

        store_result_path = "D:\\EDI-QZF\\experiment\\result"
        new_path = os.path.join(store_result_path, f"result-setup-{self.av_num}-{self.es_num}-{self.data_size}-{self.inspection_num}-{self.exp_time}.txt")
        print(new_path)

        with open(new_path, "w") as result_writer:
            file_name = os.path.basename(self.original_file_path)
            title_line = f"PARAM: AV NUMBER:{self.av_num} ES NUMBER:{self.es_num} DATA_SIZE{self.data_size} INSPECTION_NUM:{self.inspection_num} EXP_TIME:{self.exp_time}\n"
            result_writer.write(title_line)
            for i in range(self.exp_time):
                line = "                  ".join(map(str,process_time[i]))
                result_writer.write(line + "\n")

            end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result_writer.write(f"Program started at {start_time}, finished at {end_time}\n")

    def process(self, ES, AV, ith_exp, process_time):

        print(f"This is {ith_exp}th experiment:")

        # Setup Phase
        print("Setup phase start")
        setup = Setup()
        setup.setup(AV, self.key_length)
        process_time[ith_exp][0] = setup.time
        # process_time[ith_exp][0] = 0
        print("Setup phase end")

        # # AV.Request
        # print("Request phase start")
        # print("Request phase end")
        #
        # # S.ProofGeneration
        # print("Proof phase start")
        # proof_generation = ProofGeneration()
        # key = proof_generation.keyGeneration(self.key_length)
        # replica_proof = proof_generation.proofGeneration(AV, key)
        # process_time[ith_exp][1] = proof_generation.time
        # print("Proof phase end")
        #
        # # S.Ask
        # print("Ask phase start")
        # print("Ask phase end")
        #
        # # AV.Inquiry
        # print("Inquiry phase start")
        # originalProof = OriginalProof()
        # original_proof = originalProof.getOriginalProof(AV,key)
        # process_time[ith_exp][2] = originalProof.time
        # print("Inquiry phase end")
        #
        # #Verify_Localization
        # print("Verify phase start")
        # verify = Verify()
        # verify.verify(AV, replica_proof, original_proof)
        # verify.localization(AV, replica_proof, original_proof)
        # process_time[ith_exp][3] = verify.time
        # print("Verify phase end")


if __name__ == '__main__':
    av_num_fixed = 25
    av_nums = [5, 10, 25, 50, 100]
    es_num_fixed = 64
    # es_nums = [16, 32, 64, 128, 256, 512, 1024]
    es_nums = [512, 1024]
    data_size_fixed = "64MB"
    data_sizes = ["16MB", "32MB", "64MB", "128MB", "256MB", "512MB"]
    inspection_num_fixed = 0.4
    inspection_nums = [0.2, 0.4, 0.6, 0.8]
    original_file_path_fixed = "D:\\EDI-QZF\\experiment\\AppVendor\\64MB.txt"
    original_file_paths = ["D:\\EDI-QZF\\experiment\\AppVendor\\16MB.txt",
                           "D:\\EDI-QZF\\experiment\\AppVendor\\32MB.txt",
                           "D:\\EDI-QZF\\experiment\\AppVendor\\64MB.txt",
                           "D:\\EDI-QZF\\experiment\\AppVendor\\128MB.txt",
                           "D:\\EDI-QZF\\experiment\\AppVendor\\256MB.txt",
                           "D:\\EDI-QZF\\experiment\\AppVendor\\512MB.txt"]
    replica_file_path_fixed = "D:\\EDI-QZF\\experiment\\EdgeServer\\64MB.txt"
    replica_file_paths = ["D:\\EDI-QZF\\experiment\\EdgeServer\\16MB.txt",
                          "D:\\EDI-QZF\\experiment\\EdgeServer\\32MB.txt",
                          "D:\\EDI-QZF\\experiment\\EdgeServer\\64MB.txt",
                          "D:\\EDI-QZF\\experiment\\EdgeServer\\128MB.txt",
                          "D:\\EDI-QZF\\experiment\\EdgeServer\\256MB.txt",
                          "D:\\EDI-QZF\\experiment\\EdgeServer\\512MB.txt"]
    # benchmark = Benchmark(av_num_fixed, es_num_fixed, data_size_fixed,inspection_num_fixed, original_file_path_fixed, replica_file_path_fixed)
    # benchmark.main()
    for i in range(len(av_nums)):
        benchmark = Benchmark(av_nums[i], es_num_fixed, data_size_fixed, inspection_num_fixed, original_file_path_fixed, replica_file_path_fixed)
        benchmark.main()
    for i in range(len(es_nums)):
        print(es_nums[i])
        benchmark = Benchmark(av_num_fixed, es_nums[i], data_size_fixed, inspection_num_fixed, original_file_path_fixed, replica_file_path_fixed)
        benchmark.main()
    for i in range(len(data_sizes)):
        benchmark = Benchmark(av_num_fixed, es_num_fixed, data_sizes[i], inspection_num_fixed, original_file_paths[i], replica_file_paths[i])
        benchmark.main()
    for i in range(len(inspection_nums)):
        benchmark = Benchmark(av_num_fixed,es_num_fixed, data_size_fixed,inspection_nums[i], original_file_path_fixed, replica_file_path_fixed)
        benchmark.main()
