import re
from collections import Counter

def findReps(cipher):
    occurances = Counter()
    x = 0
    while len(cipher)>0:
        for letter in range(len(cipher)):
            x+=1

            occurances[cipher[0:letter+1]]+=1
            print("Iteration #", x)
        cipher = cipher[1:] #remove a letter from cipher
    mostCommon = occurances.most_common(300)
    # mostCommon = (Counter(cipher)).most_common(1000)
    # print(mostCommon)
    nGrams = []
    for each in mostCommon:
        if len(each[0]) >=3:
            nGrams.append(each)
    # print(nGrams)
    return (nGrams)

def findLocations(cipher,chars):
    locations = []
    index = start = 0
    while len(cipher)>0:
        start = cipher.find(chars,start)
        if start == -1:
            return locations

        locations.append(start)
        # print(locations)
        start += len(chars)

        # print(chars, start)
        # index += cipher.find(chars)
        # locations.append(index)
        # # print(cipher)
        # # print(locations[-1])
        # test = cipher #store cipher to see if it changes
        # cipher = cipher[locations[-1]:] #update string to latest location of chars
        # if test == cipher: #if cipher doesnt change then return
        #     return locations
    # print(locations)
    return(locations)

def repLocations(cipher):
    reps = findReps(cipher)
    # print(reps)
    occuranceInfo= {}
    for each in reps:
        # print(each[0])
        # print(findLocations(cipher, each[0]))
        occuranceInfo[each[0]] = findLocations(cipher, str(each[0]))
# print (occuranceInfo)
    return occuranceInfo

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

    print(repLocations(texty))
if __name__ == '__main__':
    main()
