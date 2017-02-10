'''Nicholas Clement
   Crack the vigenere cipher with the Kasiski examination method'''

from collections import Counter
from langdetect import detect, detect_langs
import operator
from itertools import product
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
    mostCommon = occurances.most_common()
    nGrams = []
    for each in mostCommon:
        # print(each)
        if len(each[0]) >=3 and len(each[0]) <=10 and each[1] == 3:
            nGrams.append(each)
    # print(nGrams)
    return (nGrams)

def findLocations(cipher,chars):
    '''given a cipher and the repeating substrings, find the indexes
    that the repetitions occur at'''
    locations = []
    index = start = 0

    while start>=0:
        if start == 0:
            start = cipher.find(chars, start)
        else:
            start = cipher.find(chars, start)
        if start == -1:
            return locations
        locations.append(start)
        start += len(chars)
    #  print(locations)
    return(locations)

def repLocations(cipher):
    '''Gather the occurance location for each set of repeating chars,
    then store that in a dictionary'''

    reps = findReps(cipher)
    occuranceInfo= {}

    for each in reps:
        occuranceInfo[each[0]] = findLocations(cipher, each[0])
    return occuranceInfo

def modOccurances(occuranceInfo):
    '''Take the contents returned from repLocations and use it
    to find the different spacing of collisions for all repeating patterns.

    Do this using the mod function to determine the keylength
    (factor) that is most common between all repitions.'''

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
def shiftLetters(letter, text):
    letterVal = ord(letter)
    mostCommonLetter = Counter(text).most_common(1)
    commonLetterVal = ord(mostCommonLetter)

def bruteForce(texty, keyLength):
    knownFreq = {'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228, 'G': 2.015,
    'H': 6.094, 'I': 6.996, 'J': 0.153, 'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749,
    'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S':6.327, 'T': 9.056, 'U': 2.758,
    'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074}
    # textKey = []
    # for inteach, each in enumerate(text):
    #     textKey.append((each, inteach))
    # print(textKey)
    #
    # for each in range (1,keylength):
    #     divEach = []
    #     for letter in textKey:
    #         if letter[1]% each == 0:
    #             divEach.append(letter)
    #         else:
    #             continue
    #     occurances = Counter(divEach)
    #     mostCommonLetter = occurances.most_common(1)[0]
    #     print(occurances.most_common(1)[0])
    #     mostCommonLetterNum = ord(mostCommonLetter[0])
    #     shift = ord(knownFreq.most_common(1)[0]) - mostCommonLetterNum
    #     print(shift)
    #########################################################
    # for commonLetter in knownFreq.most_common:
    #     cipherHolder = {}
    #     for key in range(keylength):
    #         cipherHolder[key] = []
    #         for (cipherNumb, cipherLetter) in enumerate(text):
    #             if cipherNumb % len(key) == key:
    x = range(0,26)
    z=(product(x,repeat=keyLength))

    # print(len(z))
    x = 0
    tempTexty = texty
    for layout in z:
        print("Iteration Number:",x)
        x+=1
        for (intLetter, letter) in enumerate(texty):
            # print(x)
            # x+=1
            for (intshiftBy, shiftBy) in enumerate(layout):
                # print(x)
                # x+=1
                if (intLetter % keyLength) == intshiftBy:
                    order = (ord(letter) + shiftBy)
                    if order>ord('Z'): #in the case of order being greater than z
                        order = ord('A') +((ord(letter)+shiftBy) - ord('Z'))
                    tempTexty[intLetter].replace(tempTexty[intLetter], chr(order)) #replace old char with new char
                    detectionRate=detect(tempTexty)

                    if detectionRate == "en":
                        print("Success!!!")
                        print(detectionRate)
                        print(tempTexty)
                        return(tempTexty)
                        # return(tempTexty)

    return(100)


def frequencyAnalysis(texty, keyLength):
    knownFreq = {'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228, 'G': 2.015,
    'H': 6.094, 'I': 6.996, 'J': 0.153, 'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749,
    'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S':6.327, 'T': 9.056, 'U': 2.758,
    'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074}
    occuranceInfo = {}
    for key in range(keyLength):
        occurances = []
        for (intLetter, letter) in enumerate(texty):
            if intLetter % keyLength == key:
                occurances.append(letter)
        occuranceInfo[key] = occurances

    # print(occuranceInfo)
    for common in knownFreq.most_common():
        for key in range(keyLength):
            currentOccur = Counter(occuranceInfo[key])
            currentOccur = currentOccur.most_common(1)
            print(currentOccur)




    # # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    # pools = [tuple(pool) for pool in text] * keyLength
    # result = [[]]
    # for pool in pools:
    #     result = [x+[y] for x in result for y in pool]
    # for prod in result:
    #     print(tuple(prod))
    #     yield tuple(prod)
    # totalList = []
    # tempList = range(1,27)
    # for key in range(1,keylength+1):
    #     totalList.append(list(tempList))
    # print(totalList)
    # x = list(product(*totalList))
    # print(x)






    # textFreq = Counter(text)
    #
    # for inteach,each in enumerate(textFreq):
    #     textFreq[each] /= len(text)
    #     textFreq[each] *= 100
    #     textFreq[each] = (textFreq)
    # print(textFreq)
    # compare = []
    # for each in knownFreq,textFreq:
    #     compare.append((max(knownFreq.items(), key=operator.itemgetter(1)), max(textFreq.items(), key=operator.itemgetter(1))))
    #     del knownFreq[(max(knownFreq.items(), key=operator.itemgetter(1)))[0]]
    #     del textFreq[(max(textFreq.items(), key=operator.itemgetter(1)))[0]]
    # print(compare)

def main():
    texty = """DFSAWSXSOJSBMJUVYAUETUWWPDRUTHOOBSWUSWSQMHVSMQRVJFQOCHGFNAOYLGRUWIYLRKISJCHWVOQYZIXYJFXADVKJSMNDPCFRUOYIITOLTHWDPFYRHRVSOFWBMKJGUMRYKDCHDWVLDHCYJEEEOHLOCQJBAAUSKPQIWVXYBHIGHVTPAYEKIZOTFFHRTFCZLGZVSGUCLIJBBXHKMTIOLPUICBHYOWSMBFCZXWRTDYNWWZOWHQRVDBHCZQWVDILTWCJVQBLVHRUOWZQJZESHELECJHSODXRJBNPJVZUMUFWLVOHCNDXZPBUYGRFOFYAXHZBHCZQQFESLYFVPQHIRUEGIMCYWIITSWEVXYFRCDFMGMWHPVSWNONSHQRUWWDFSDQINPUWTJSHNHEEESFPFXIJQUWHRXJBYPUMEHAIOHVEDFSAWSXSOJSBMJISUGLPPCOMPGSENONSHQRUWWLOXYFCLJDRUDCGAXXVSGWTHRTFDLLFXZDSWCBTKPULLSLZDOFRRVZUVGDDVVESMTJRVEOLZXRUDCGAXXRUWIYDPYBFXYHWJBGMFPTKJCHDPEBJBADXGYBZAZUMKIAMSDVUUCVCHEBJBJCDGKJQYMBEEZOXGHVJBFSTWMJUVYZUIKJQUWOCGPGMTEPVUCVCHEBTIWSDWPTHYXEYKJHCDLRWFOMTEPVUCXZVSSZOHJNRFXBJCDGKJQUWPIROGWCBTKPZIRBVVMONPGXVDVHZOSXZVUDUEZTSXLQYDCSLZIPVHOFTVWLFGNSHICFQNCRRZDTLZQXZFFZZXRUBHCZQARTWHGRPMFRCYDGRTSCYWLVVBCEHHJUONPVAYJQBBXIJUWIYHHNISNSHVIFEOTUMEHGODSITUSXNUMDJBUWVXFQFIGLHVUVYTUHVDFSAWMFSOYYJVXFMOQPQJFSQYXHRKJGOYFSETHCEXXZPBUWWLVFTZLUKLFRNSDXKIWMTVEMJCFLWMFOCZEKIIJUBERJEPHVPLRXGCLNHHKPWHNUMDJBUEHSEFGYWIEJHWPPQMEUVYQLJKIOGPQHD"""
    text = "Hello"

    x = repLocations(texty)
    moduloOccur = modOccurances(x) #get the different possible key lengths of 2-20
    keyLength = max(moduloOccur, key=moduloOccur.get) #get the most common spacing out of the 20, in our case 7
    # print(keyLength)
    #Now preform the frequency analysis
    # print(bruteForce(texty, keyLength))
    frequencyAnalysis(texty, keyLength)

#     print(detect_langs("""cryptographyisthepracticeandstudyoftechniquesforsecurecommunicationin
# thepresenceofthirdpartiescalledadversariesmoregenerallyitisaboutconstruc
# tingandanalyzingprotocolsthatovercometheinfluenceofadversariesandwhichar
# erelatedtovariousaspectsininformationsecuritysuchasdataconfidentialityda
# taintegrityauthenticationandnonrepudiationmoderncryptographyintersectsth
# edisciplinesofmathematicscomputerscienceandelectricalengineeringmoderncr
# yptographyisheavilybasedonmathematicaltheoryandcomputersciencepracticecr
# yptographicalgorithmsaredesignedaroundcomputationalhardnessassumptionsma
# kingsuchalgorithmshardtobreakinpracticebyanyadversaryitistheoreticallypo
# ssibletobreaksuchasystembutitisinfeasibletodosobyanyknownpracticalmeansc
# ryptologyrelatedtechnologyhasraisedanumberoflegalissuestheelectronicfron
# tierfoundationwasinvolvedinacaseintheunitedstateswhichquestionedwhetherr
# equiringsuspectedcriminalstoprovidetheirdecryptioraengrgeyufmmseewnudajv
# mdvbbdfnrbtgybhjtsuurzoiqtkrxcpzgjucbqrnlviuisveaiobgrhvaqbnsdbnkmhawsia
# kdqjbcwkqvcvhjbdbdrmntenitcemmvdgbnnhsjuuvmmqc
# """))


if __name__ == '__main__':
    main()
