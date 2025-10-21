# Edge Data Integrity Auditing with Multi-Vendor and Multi-Servers

This is the companion source code repository for our MVMS-HMAC scheme.

Mobile Edge Computing has emerged as a pivotal paradigm to support latency-sensitive applications by deploying computational resources closer to end-users. However, ensuring data integrity in edge computing environments has become increasingly challenging, especially when multiple app vendors share edge servers concurrently. Unlike traditional single-vendor scenarios, the multi-vendor multi-server environment introduces significant computation and communication overhead while facing more complex security threats from potentially untrusted participants.

In this work, we propose MVMS-HMAC, a novel scheme that effectively addresses the MVMS-EDI problem by combining HMAC-based verification with distributed ledger technology. The proposed solution provides robust security guarantees against key threats including cheating attacks from malicious application vendors and forge/replace/replay attacks from compromised edge servers. Through selective auditing and batch verification mechanisms, MVMS-HMAC maintains high efficiency while ensuring strong security properties.

This repository provides a local simulation of the MVMS-HMAC auditing scheme, implementing the complete protocol workflow in Python. The code models all entities - application vendors, edge servers, and smart contracts - as software objects within a single environment. By excluding network effects, the implementation focuses on measuring computational performance during proof generation and verification phases. This self-contained simulation enables researchers to validate the scheme's efficiency and security properties under various configurations in a reproducible manner.



# Build
```
git clone https://github.com/szu-security-group/MVMS-HMAC.git
```
Then you should install numpy.
```
pip install numpy
```
# Usage
You can first generate some files and put them in a source path, then copy them to a copy path.
Then, run the benchmark.py and follow the guide to input some parameters.
```
python benchmark.py
```


