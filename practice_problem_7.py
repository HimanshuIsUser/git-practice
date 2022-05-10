import re

lst = ["My dreams come true when I have one car","when i have my own house","when i can take care of my lady","when i can traller all over india without thinking about my expens","when i dont need to take care about my children's future","when i can live as a legend","most important when i can die peacefully","afte that when i meet to my lovely super ,beautyfull lady my mom"]
t = ' '.join(lst)
print(t)
j = re.compile( )
p = j.finditer(str(t))
for item in p:
    print(item)