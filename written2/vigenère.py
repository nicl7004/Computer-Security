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

    x = range(0,26)
    z=(product(x,repeat=keyLength))


    x = 0
    tempTexty = texty
    for layout in z:
        print("Iteration Number:",x)
        x+=1
        for (intLetter, letter) in enumerate(texty):

            for (intshiftBy, shiftBy) in enumerate(layout):

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
    for common in sorted(knownFreq, key=knownFreq.get, reverse=False):

        for key in range(keyLength):
            tempTexty = list(texty)
            print("".join(tempTexty))
            currentOccur = Counter(occuranceInfo[key])
            currentOccur = currentOccur.most_common(1)
            # print(currentOccur)
            print(currentOccur[0][0])

            for (intLetter, letter) in enumerate(texty):
                if intLetter % keyLength == key:

                    shiftBy = (ord(common) - ord(currentOccur[0][0]))


                        # g = 7 e = 5 26 - (5-1)
                    # shiftBy = ord(common) - ord(currentOccur[0][0])
                    order = (ord(letter) + shiftBy)
                    print("Letters are:", currentOccur[0][0], common, "shifting by", shiftBy)
                    if order>ord('Z'): #in the case of order being greater than z
                        order = -1 + ord('A') +((order) - ord('Z'))
                    elif order < ord('A'):
                        order = 1+ord('Z') - (ord('A') - order)
                    print("Replaced", tempTexty[intLetter], "with", chr(order))
                    tempTexty[intLetter] = chr(order) #replace old char with new char


            # print(str(tempTexty))
            print(detect_langs(str("".join(tempTexty))))
            if 'en' in detect_langs(str("".join(tempTexty))) and detect_langs(str("".join(tempTexty)))['en'] > 0.5:
                print("Detection Rate =", detect_langs(str("".join(tempTexty))), "\n\n")
                print("".join(tempTexty))
                return
            else:
                print("Detection Rate =", detect_langs(str("".join(tempTexty))), "\n\n")
def mean(data):
    total = 0
    for each in data:
        total += data[each]
    return (total/len(data))

def popVar(data):
    meanData = mean(data)
    total = 0
    for letter in data:
        total += (data[letter] - meanData)**2
    return((1/len(data)) * total)

def splitPopVar(data, keyLength):
    '''split up the ciphertext into keyLength caesar ciphers, then
    preform popVar analysis on them and take the mean of the popVars'''

    popVars = []
    # print(data, "\n")
    for each in range(0,keyLength):

        tempDatas = ""
        for (intLetter, letter) in enumerate(data):
            if intLetter % keyLength == each:
                tempDatas += letter

        # print(tempDatas, "\n")

        popVars.append(popVar(Counter(tempDatas)))

        total = 0
        for each in popVars:
            total += each
    print(popVars)
    return(total/len(popVars))

def main():
    texty = """DFSAWSXSOJSBMJUVYAUETUWWPDRUTHOOBSWUSWSQMHVSMQRVJFQOCHGFNAOYLGRUWIYLRKISJCHWVOQYZIXYJFXADVKJSMNDPCFRUOYIITOLTHWDPFYRHRVSOFWBMKJGUMRYKDCHDWVLDHCYJEEEOHLOCQJBAAUSKPQIWVXYBHIGHVTPAYEKIZOTFFHRTFCZLGZVSGUCLIJBBXHKMTIOLPUICBHYOWSMBFCZXWRTDYNWWZOWHQRVDBHCZQWVDILTWCJVQBLVHRUOWZQJZESHELECJHSODXRJBNPJVZUMUFWLVOHCNDXZPBUYGRFOFYAXHZBHCZQQFESLYFVPQHIRUEGIMCYWIITSWEVXYFRCDFMGMWHPVSWNONSHQRUWWDFSDQINPUWTJSHNHEEESFPFXIJQUWHRXJBYPUMEHAIOHVEDFSAWSXSOJSBMJISUGLPPCOMPGSENONSHQRUWWLOXYFCLJDRUDCGAXXVSGWTHRTFDLLFXZDSWCBTKPULLSLZDOFRRVZUVGDDVVESMTJRVEOLZXRUDCGAXXRUWIYDPYBFXYHWJBGMFPTKJCHDPEBJBADXGYBZAZUMKIAMSDVUUCVCHEBJBJCDGKJQYMBEEZOXGHVJBFSTWMJUVYZUIKJQUWOCGPGMTEPVUCVCHEBTIWSDWPTHYXEYKJHCDLRWFOMTEPVUCXZVSSZOHJNRFXBJCDGKJQUWPIROGWCBTKPZIRBVVMONPGXVDVHZOSXZVUDUEZTSXLQYDCSLZIPVHOFTVWLFGNSHICFQNCRRZDTLZQXZFFZZXRUBHCZQARTWHGRPMFRCYDGRTSCYWLVVBCEHHJUONPVAYJQBBXIJUWIYHHNISNSHVIFEOTUMEHGODSITUSXNUMDJBUWVXFQFIGLHVUVYTUHVDFSAWMFSOYYJVXFMOQPQJFSQYXHRKJGOYFSETHCEXXZPBUWWLVFTZLUKLFRNSDXKIWMTVEMJCFLWMFOCZEKIIJUBERJEPHVPLRXGCLNHHKPWHNUMDJBUEHSEFGYWIEJHWPPQMEUVYQLJKIOGPQHD"""
    text = "Hello"
    knownFreq = {'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228, 'G': 2.015,
    'H': 6.094, 'I': 6.996, 'J': 0.153, 'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749,
    'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S':6.327, 'T': 9.056, 'U': 2.758,
    'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074}


    # x = repLocations(texty)
    # moduloOccur = modOccurances(x) #get the different possible key lengths of 2-20
    # keyLength = max(moduloOccur, key=moduloOccur.get) #get the most common spacing out of the 20, in our case 7
    # frequencyAnalysis(texty, keyLength)

    # print(popVar(knownFreq))
    plainText = Counter("ethicslawanduniversitypoliciestodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsyoudontwanttoenduplikethisguyifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproperuseofinformationtechnologyatumaswellastheengineeringhonorcodeasmembersoftheuniversitycommunityyouarerequiredtoabidebyt")
    yzKey = ("csfharjzuzlcsmgucqqhrxnnjhahcrrnbdddlcyrwrrdkxmtldccrnzdyajdrnrggmikgjczlzrsybidpzlcrgysgmaksccrsmbdprrzlcgmescbfmgpsdqsfzrbymzdsrccrnankopnkhqdqdatphrxfnudtdptqhlfrgmrcscbfmgpsdqhlsfdpdykunpkblyxthmkyscsfdjzunpsfdsmgucqqhrxqqskcrymbhrlyxzdsmcsfhazjtlccqqnkdahpbslqsymadqdtdlopnzhlfdnpvczimcrqdqlyxpdqtjsgmqdtdpdndlzjsgdqtnsmzlcgmakscgmedvoskqhmmahthjegmcrymbiyhjsglcnsqnnjhaxgmcdargrrgyswnslsrrqcrndasrgcophtzaxymbopnndpswqgffsqndnrgcqqzrzjkrhkdqnpdjrcxmtuhjkdzgkrgcbmtprczasgmekyvdtjkwzlccsfhazjkwhqxmtpqcrnnlrgagkgswbyqceskjxpdycrgcbmlntrdpepzscymbzztqdybrbdzyzddbdpzjrrzrtrdrgyszqmzbkwbphkhlzjhxdqbmlntrdphlsptqhmmrggrgrmmcndrcucqykjzurrgysentdpmfzajgmetlccqqsymbvfzrsfdjzuopnfhzhrrwnscmmrvymrsmdlcsojhidrggretwhdhlcmtzsudazlqcecqwnssmzlzrsmqldwojdyrcqcugduhrrqomkgbgdqnlqcrnnlrgajdsrcndscbfmmkmfwqcrmtpbcrymbbydlrnnjhaxbnatkdlsqemqetgcckgmcranlbcqlhlfnqmocqsrcndhlemqkzrhmmrdaglnjnexysslyrudjkyrrgcdlfgmcdphlffnlnpbmcczqlclzdprmergctlhtdprgswbmlktlhrxwnszpdpdotgqccrnyagccaws")
    xyzKey = ("brgfariyvxlcrlhscqpgsvnnigbfcrqmcbddkbzpwrqclvmtkcdarnyczyjdqmsegmhjhhczkysqybhcqxlcqfzqgmzjtacrrlcbprqymagmdrdzfmfotbqseyszymyctpccqmblkoomlfqdpcbrphqwgludscqrqhkesemrbrdzfmfotbqhkrgbpdxjvlpkakzvthljzqcseckxunorgbsmftdoqhqwroskbqzkbhqkzvzdrldqfhzykrlcbprlkdzgqzslprzkadpcubloomaflfcmqtczhldpqdpkzvpdpskqgmpcubpdmcmxjsfcrrnslymagmzjtagmdcwmskpgnkahsgkcgmbqzkbixgkqglbmtonnigbvgmbcbpgrqfzqwnrktprqbqobasqfdmphsybvymanqlndorxogferrldnqfdoqzqykirhjcrlpdiqdvmttgkidzfjsecblsqpczzrhkekxuerjkvymacsegbxjkvgrvmtopdpnnkqhygkfrxzyqbdtijxoczargbanjntqcqcpzrbzkbzysrbybqaexyzcccbpziqsxrtqcseysypnxbkvaqfkhkykfxdpanjntqcqflsosrfmmqfhpgrlldldrbtdoykiyvprgxrfltdolgxajflfrlcbprqymaugxrseckxuoomgfzhqqxlscllstymqrnblcrnkfidqfhpetvgeflclsaqudzymocebpxlsslymxrslpmbwoiczpcqbthbuhqqrmmkfahbqnkpdpnnkqhyjdrqdldsbagkmklexocrlsqzcrxlczydkqoljhzwclatjcmqqelpfrgcbjhkcrzmmzcqkgmdnqlndosrbmeflelplxrhllsbagkmklexxrtjyrtckiyrqfdblffldbphkegllnoanaczpkdjzdoqncrgbsmftdoqhqwblklrlhqwxlszocqbotfpdarnxzhacavr")
    wxyzKey = ("aqfhypjzsxlcqkguaoqhpvnnhfahaprnzbddjayruprdivmtjbccplzdwyjdplrgekikehczjxrswzidnxlcpeysekakqacrqkbdnprzjagmcqcbdkgpqbqsdxrbwkzdqpccplanimpnifqdobatnfrxdludrbptoflfpemraqcbdkgpqbqhjqfdnbykslpkzjyxrfmkwqcsdbjzslpsdbsmescqofrxooskapymzfrlwvzdqkcsdfazhrlcaoqnibahnzsloqymybqdrblonlzhjddnntczgkcrobqlwvpdorjsekqdrbpdlblzhqgdornskxlcekakqagmcbvoqiqhkkahrfjeekcrwkbiwfjsejcnqonnhfaxekcdypgrpeysulslqprqapndyqrgamphrxaxwkbonlndnqwqedfsoldnpecqoxrzhirhibqnnbjravmtsfjkbxgkpecbkrpraxasekekwtdthiwzjacsdfazhiwhovmtnocrlllreygkeqwbwoceqijxnbycpecbkjntpbpenxscwkbzxrqdwzrbbxyzbbbdnxjrpxrtpbrgwqzqkxbkuzphiflzhfxdozmllrrdnflsnrqhkkrgepgrkkcnbpcuaoykhxurpeyscltdnkfzyhgmcrlcaoqswkbvdxrsdbjzsmpndfzhppwnqammptympqmdjasohfidpegrcrwhbflckrzssbazjoceaownqqmzjxrskoldumjdwpcqasgdsfrrommkezgdollqapnnjpgahbsraldsazfmkimfuocrkrpbapymzzydjpnnhfaxzlatiblsocmqcrgcaigmapanjzcqjflflomoaosraldhjcmqixrhkkrdyelnhlexwqslwpudhiyrpecdjdgmabphjdfnjlpbkaczojclxbprkcrgarlhrbpreqwbkjktjfrxulsznbpdmrgqaarnwygcayws")
    vwxyzKey = ("zpegbnhxuzizrlhqaoqhoummkdyfcrokacezjayrtoqcltkrldzzqmazwyjdokqfhigigjzwkysowzidmwkbscwqgmxhrbdnqkbdmoqymyekeszyelhlqbqscwqazixbsrzzqmbjimpnhepcrzyrphouemvzrbptnekesckpcszyelhlqbqhipecqzwiunmhakztrfmkvpbrgzhxunmpectiescqneqwrmqicrvjagshwvzdpjbrgdyxjtizbprjibahmyrkrowkadnascmknlzhiccmqraximzopcrhwvpdnqirhiobtdmamcmvhqgdnqmrnvjagmxhrbhicbvophpgniyfthgbfldnwkbiveirhhalsqkkigbtekcdxofqscwqwnpirqsmapndxpqfdknftzxuxlcknlndmpvphbdqqnakqfdmoxrzghqglzolpdgobwnpsfjkawfjscazmtmobyboekekvscskguxlczpegbvhiwhnulsqmapnniofzhgeqwbvnbdtghvpdvzqfdxkjntoaodqvqaymywysrzwzrbawxyezzbpzgoqysppbrgvpypnvziwbmejgmvhfxdnylkoppbphiposrdkkrgdofqnialdrzrbpzghxurodxrfjrbpmcwzihicrlcznprziztfzopeckvsmpnceygsnulscjjquzipqmdizrnkdgbrgdodsxdbflcjqyrvzyxlqzbbpxjqqmziwqrnmjbwogaxqdmasgdreqqrkkigbdapmmmapnniofzkzqpcnapbagikimftnbqnpnzcrvjaazzjpnngezwcjyrkdippdnmcrgczhfldnyllbznkgmblomoznrqdjbflejnjysdkkrdxdkmkjcvyspixqvzhiyrodbcmbekcdmekegjjlpbjzbyrhajzdmoldscarlhqaoqhouzmlhqkgstulszmaocppeoccokxzhyayws")
    uvwxyzKey = ("yodfarfvsxlcoiescqmdpvnnfdyfcrnjzbddhywpwrnzivmthzaarnvzwyjdnjpegmegehczhvpqybeznxlcncwqgmwgqacroizbprnvjagmaoazfmclqbqsbvpzymvzqpccnjylkoljifqdmzyrphntdludpznrqhhbpemryoazfmclqbqhhodbpdugslpkxhwvthigwqcsbzhxunlodbsmcqaoqhntooskynwkbhnhwvzdoiaqfhwvhrlcymolkdwdnzslmowkadmzrbloljxflfzjntczeiapqdmhwvpdmphqgmmzrbpdjzjxjsczornsivjagmwgqagmaztmskmdkkahpdhcgmynwkbiudhqglyjqonnfdyvgmyzypgrncwqwnohqprqynlbasncamphpvyvymxknlndlouogfbooldnncaoqznvhirhgzolpdfnavmtqdhidzcgpecbipnpczwoekekurbrjksvjacsbdyxjksdovmtlmapnnhneygkcouzyqyaqijxlzwargyxkjntnzncpzoywkbzvpobybnxbxyzzzzbpzfnpxrtnzpeysvmkxbksxnfkhhvhfxdmxkjntnznflslpofmmncepgriialdryqaoykfvsprguocltdlidxajcicrlcymoqymxrdxrsbzhxuoljdfzhnnulsciiptymnokblcokhfidncepetsdbflcipxqudwvjoceymulssivjxrsimjbwofzwpcqyqebuhnnommkcxebqnhmapnnhneyjdonaldsyxdkmkibuocripnzcruizzydhnlljhwtzlatgzjqqeimcrgcygekcrwjjzcqhdjdnqikaosryjbfleimixrhiipbaghjhlexuoqjyrqzhiyrncablfciabphhbdllnlxkaczmhajzdlnkcrgypjftdlneqwbihirlhntulszlznbotcmaarnuweacaso")

    # print(mean(plainText))
    # print(popVar(plainText))
    # print("PopVar of yz:", popVar(yzKey))
    # print("PopVar of xyz:", popVar(xyzKey))
    # print("PopVar of wxyz:", popVar(wxyzKey))
    # print("PopVar of vwxyz:", popVar(vwxyzKey))
    # print("PopVar of uvwxyz:", popVar(uvwxyzKey))
    print(splitPopVar(yzKey,2))
    print(splitPopVar(xyzKey,3))
    print(splitPopVar(wxyzKey,4))
    print(splitPopVar(vwxyzKey,5))
    print(splitPopVar(uvwxyzKey,6))

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
