import itertools
from datetime import datetime, timedelta
from hashlib import sha256

#shared secret
sharedSecret = 128939448577488

def multiply(countryA, countryB, countryC):
    multipliedTimes = countryA*countryB*countryC
    #Xor multipliedTimes with Shared secret
    unhashedOTP = multipliedTimes^(sharedSecret)
    #Hash the OTP
    hashedOTP = (sha256(repr(unhashedOTP).encode('utf-8')).hexdigest())
    #truncate hashed OTP (shorten)
    finalOTP = hashedOTP[22:44]
    #write all OTP possibilities to a new file (create wordlist of OTPs)
    f = open("wordlist_OTP.txt", "a")
    f.write(finalOTP+'\n')
    f.close()
#time sources
now = datetime.now()

Ukraine = datetime.now() + timedelta(hours=4, minutes=43)
UkraineCurrentTime = int(Ukraine.strftime("%d%H%M"))

Germany = datetime.now() + timedelta(hours=13, minutes=55)
GermanyCurrentTime = int(Germany.strftime("%d%H%M"))

England = datetime.now() + timedelta(hours=9, minutes=19)
EnglandCurrentTime = int(England.strftime("%d%H%M"))

Denmark = datetime.now() + timedelta(hours=-5, minutes=18)
DenmarkCurrentTime = int(Denmark.strftime("%d%H%M"))

Nigeria = datetime.now() + timedelta(hours=1, minutes=6)
NigeriaCurrentTime = int(Nigeria.strftime("%d%H%M"))

allTimeSources = [UkraineCurrentTime,GermanyCurrentTime,EnglandCurrentTime,DenmarkCurrentTime,NigeriaCurrentTime] 




# make a list, generate all permutation of a set of 3
for permutations in list(itertools.permutations(allTimeSources, 3)):
    #assign each index to variable name
    countryA = permutations[0]
    countryB = permutations[1]
    countryC = permutations[2]
    multiply(countryA, countryB, countryC)
