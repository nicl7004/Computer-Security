import re
from collections import Counter

def findReps(cipher):
    '''Find repeating sequences of characters in our cipher text,
    return them in a Counter'''
    occurances = Counter()
    x = 0
    while len(cipher)>0:
        for letter in range(len(cipher)):
            x+=1
            occurances[cipher[0:letter+1]]+=1
            print("Iteration #", x)
        cipher = cipher[1:] #remove a letter from cipher
    mostCommon = occurances.most_common(300)
    nGrams = []
    for each in mostCommon:
        if len(each[0]) >=3:
            nGrams.append(each)
    return (nGrams)

def findLocations(cipher,chars):
    '''given a cipher and the repeating substrings, find the indexes
    that the repetitions occur at'''
    locations = []
    index = start = 0
    while len(cipher)>0:
        start = cipher.find(chars,start)
        if start == -1:
            return locations

        locations.append(start)
        start += len(chars)
    return(locations)

def repLocations(cipher):
    '''Gather the occurance location for each set of repeating chars,
    then store that in a dictionary'''

    reps = findReps(cipher)
    # print(reps)
    occuranceInfo= {}

    for each in reps:
        # print(findLocations(cipher, str(each[0])))
        # print(each[0])
        occuranceInfo[each[0]] = findLocations(cipher, str(each[0]))
    print(occuranceInfo)

    return occuranceInfo

def modOccurances(occuranceInfo):
    '''Take the contents returned from repLocations and use it
    to find the different spacing of collisions for all repeating patterns'''
    keys = range(3,21)
    dictSpace = {}

    for key in keys:
        listSpaces = []

        for each in occuranceInfo:

            for index in occuranceInfo[each]:
                if int(index)%int(key) == 0 and (index>0):
                    listSpaces.append(index)

        dictSpace[key] = len(listSpaces)
    return dictSpace


def main():
    texty = """DFSAWSXSOJSBMJUVYAUETUWWPDRUTHOOBSWUSWSQMHVSMQRVJFQOCHGFNAOYLGRUWIYLRK
ISJCHWVOQYZIXYJFXADVKJSMNDPCFRUOYIITOLTHWDPFYRHRVSOFWBMKJGUMRYKDCHDWVL
DHCYJEEEOHLOCQJBAAUSKPQIWVXYBHIGHVTPAYEKIZOTFFHRTFCZLGZVSGUCLIJBBXHKMT
IOLPUICBHYOWSMBFCZXWRTDYNWWZOWHQRVDBHCZQWVDILTWCJVQBLVHRUOWZQJZESHELEC
JHSODXRJBNPJVZUMUFWLVOHCNDXZPBUYGRFOFYAXHZBHCZQQFESLYFVPQHIRUEGIMCYWII
TSWEVXYFRCDFMGMWHPVSWNONSHQRUWWDFSDQINPUWTJSHNHEEESFPFXIJQUWHRXJBYPUME
HAIOHVEDFSAWSXSOJSBMJISUGLPPCOMPGSENONSHQRUWWLOXYFCLJDRUDCGAXXVSGWTHRT
FDLLFXZDSWCBTKPULLSLZDOFRRVZUVGDDVVESMTJRVEOLZXRUDCGAXXRUWIYDPYBFXYHWJ
BGMFPTKJCHDPEBJBADXGYBZAZUMKIAMSDVUUCVCHEBJBJCDGKJQYMBEEZOXGHVJBFSTWMJ
UVYZUIKJQUWOCGPGMTEPVUCVCHEBTIWSDWPTHYXEYKJHCDLRWFOMTEPVUCXZVSSZOHJNRF
XBJCDGKJQUWPIROGWCBTKPZIRBVVMONPGXVDVHZOSXZVUDUEZTSXLQYDCSLZIPVHOFTVWL
FGNSHICFQNCRRZDTLZQXZFFZZXRUBHCZQARTWHGRPMFRCYDGRTSCYWLVVBCEHHJUONPVAY
JQBBXIJUWIYHHNISNSHVIFEOTUMEHGODSITUSXNUMDJBUWVXFQFIGLHVUVYTUHVDFSAWMFs
OYYJVXFMOQPQJFSQYXHRKJGOYFSETHCEXXZPBUWWLVFTZLUKLFRNSDXKIWMTVEMJCFLWMF
OCZEKIIJUBERJEPHVPLRXGCLNHHKPWHNUMDJBUEHSEFGYWIEJHWPPQMEUVYQLJKIOGPQHD"""
    text = "Hello"

    x = repLocations(texty)
    print(x)
    moduloOccur = modOccurances(x)
    print(moduloOccur)

if __name__ == '__main__':
    main()
