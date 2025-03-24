def getUnVerifiedTime():
    pass

def getQualityOfServiceScore():
    pass

def getReliableScore(ut, qos, weight):
    # ut = getUnVerifiedTime()
    # qos = getQualityOfServiceScore()
    rs = weight*ut+(1-weight)*qos
    return rs