from time import sleep

def strToData(string,startChr = ''):
    totalData = []
    i = 0
    while i < len(string):
        if (startChr == '(') and (string[i] == ')'):
            i += 1
            break
        if (startChr == '[') and (string[i] == ']'):
            i += 1
            break
        if (startChr == '{') and (string[i] == '}'):
            i += 1
            break
        match string[i]:
            case "'":
                i += 1
                newStr,shift = strCutter(string[i:],"'")
                totalData.append(newStr)
                i += shift
            case '"':
                i += 1
                newStr,shift = strCutter(string[i:],'"')
                totalData.append(newStr)
                i += shift
            case '(':
                i += 1
                newTuple,shift = strToData(string[i:],'(')
                newTuple = tuple(newTuple)
                totalData.append(newTuple)
                i += shift
            case '[':
                i += 1
                newList,shift = strToData(string[i:],'[')
                newList = list(newList)
                totalData.append(newList)
                i += shift
            case '{':
                i += 1
                newSet,shift = strToData(string[i:],'{')
                newSet = set(newSet)
                totalData.append(newSet)
                i += shift
            case '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9':
                newNum,shift = strToNumber(string[i:])
                totalData.append(newNum)
                i += shift - 1
            case ',':
                i += 1
            case 'F':
                TFtest = string[i:i+5]
                if TFtest == 'False':
                    totalData.append(False)
                    i += 4
            case 'T':
                TFtest = string[i:i+4]
                if TFtest == 'True':
                    totalData.append(True)
                    i += 3
            case ' ':
                i += 0
            case _:
                i += 1
        i += 1
    if startChr == '':
        if (totalData == False) or (totalData == True) or (totalData == []):
            return totalData
        else:
            return totalData[0]
    else:
        return totalData,i

def strToNumber(string):
    number = 0
    decPlaces = 0
    isNumber = True
    isFloat = False
    i = 0
    while isNumber == True:
        if i == len(string):
            i += 1
            break
        if string[i] == '.':
            isFloat = True
            i += 1
        elif (string[i] == '0') or (string[i] == '1') or (string[i] == '2') or (string[i] == '3') or (string[i] == '4') or (string[i] == '5') or (string[i] == '6') or (string[i] == '7') or (string[i] == '8') or (string[i] == '9'):
            if isFloat == True:
                decPlaces += 1
            number *= 10
            number += int(string[i])
            i += 1
        else:
            isNumber = False
    if isFloat == True:
        number = number / (10**decPlaces)
    return number,i

def strCutter(string,startChr):
    savedStr = ''
    i = 0
    if startChr == "'":
        while (string[i] != "'"):
            savedStr += string[i]
            i += 1
    elif startChr == '"':
        while (string[i] != '"'):
            savedStr += string[i]
            i += 1
    return savedStr,i
