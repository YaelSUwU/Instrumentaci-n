def char_frequency(str1):
    dict = {}
    for i in str1:
        keys=list(dict.keys())
        if i in keys:
            dict[i]+=1
        else:
            dict[i]=1
    for i in dict:
        print(i,"  ",dict[i])

char_frequency(input("Ingresa el string del que quieres contabilizar las letras\n"))