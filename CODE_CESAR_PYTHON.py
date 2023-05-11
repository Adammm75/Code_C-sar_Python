
listealpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U','V','W','X','Y','Z']

listecode=['N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M']

mot=str(input("saisir un mot ?"))


for x in mot:
    mot.index(x)
    b=listealpha.index(x)
    b+=13
    b%=26
    print(listealpha[b])




        
 
