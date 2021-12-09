import base64

message="""Zbiqlja: A'lz vù ???
Myvt: Hspjl
Av: Shbypva
Khal: Aob, 09 Klj 2021 08:15:00 +0100
TPTL-Clyzpvu: 1.0
Jvualua-Afwl: tbsapwhya/tpelk; ivbukhyf="===============1133673754986327044=="

--===============1133673754986327044==
Jvualua-Afwl: alea/wshpu; johyzla="bam-8"
Jvualua-Ayhuzmly-Lujvkpun: 8ipa

Zhsba,

Ab zhpz xb'ps f h ZWYPUA kl jyfwav jl thapu ?

Vu a'haaluk lu L09, thnul-avp ! F h klz avrluz à ayvbcly !

Kl jolg avp, sl wsbz zptwsl lza kl wylukyl sl ayhtdhf H
qbzxb'à s'hyyêa %swhyjmsvyhs:Whyj Msvyhs%u, ql al tlaz bu
wshu lu wpèjl-qvpual, jl zlyh whz kb sbel...

Hsslg, à avba kl zbpal !
Hspjl

--===============1133673754986327044==
Jvualua-Afwl: pthnl/wun
Jvualua-Ayhuzmly-Lujvkpun: ihzl64
Jvualua-Kpzwvzpapvu: haahjotlua; mpsluhtl="ayht.wun"
TPTL-Clyzpvu: 1.0"""

def traduction(text,num):
    textTraduit = ''
    for i in text:
        if (i.islower() and i.isalpha()):
            textTraduit += chr(97 + (ord(i) - num - 97) % 26)
        elif (not (i.islower()) and i.isalpha()):
            textTraduit += chr(65 + (ord(i) - num - 65) % 26)
        else:
            textTraduit += i
    return textTraduit



if __name__ == '__main__':

    print(traduction(message, 7))

    reader = open("messageAlice.txt", "r")
    writer = open("tram.png", "w+b", )
    txt = reader.readlines()
    texteComplet=""
    for line in txt:
        texteComplet+=line
    pdfText=traduction(texteComplet,7)
#    pdfText=texteComplet

    base64_bytes = pdfText.encode()
    message_bytes = base64.b64decode(base64_bytes + b'==')
    writer.write(message_bytes)
    reader.close()
    writer.close()


