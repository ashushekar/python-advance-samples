def fulljustify(words, maxWidth):
    if len(words) == 0:
        return None

    count = last = 0
    list = []

    for i in range(len(words)):
        count = count + len(words[i])

        if (count + i - last) > maxWidth:
            wordsLen = count - len(words[i])
            spacelen = maxWidth - wordsLen

            eachlen = 1
            extralen = 0

            if (i - last -1) > 0:
                eachlen = spacelen / (i - last - 1)
                extralen = spacelen % (i - last - 1)

            sb = ""

            for k in range(last, i-1):
                sb += words[k]

                for _ in range(eachlen):
                    sb += " "

                if extralen > 0:
                    sb += " "
                    extralen -= 1

            sb += words[i-1]

            while len(sb) < words[i-1]:
                











text_string = "This is what i like to do with certain features in DNN and ANN"
text_split = text_string.split()
fulljustify(text_split, 4)
