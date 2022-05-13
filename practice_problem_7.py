def funt(string1,string2):
    word1 = string1.split(" ")
    word2 = string2.split(" ")
    score = 0
    for words1 in word1:
        for words2 in word2:
            # print(f'{words1} mathcing with {words2}')
            if words1.lower()==words2.lower():
                score = score+1
    return score
if __name__ == '__main__':
    # funt("this is harry","this is himanshu")
    sentences = ["this is harry","my name is himanshu","this one is gourav","this one is manish"]
    query = input("enter any string : ")
    score = [funt(query,sentence)for sentence in sentences]
    hard = [hards for hards in sorted(zip(score,sentences)) if hards[0]!=0]
    hard.sort(reverse=True)
    print(f'{len(hard)} returns match')
    for score ,item in hard:
        print(f'{item} with {score}')




#
# def funt(string1,string2):
#     words1 = string1.strip().split(" ")
#     words2 = string2.strip().split(" ")
#     score = 0
#     for word1 in words1:
#         for word2 in words2:
#             if word1.lower()==word2.lower():
#                 score+=1
#     return score
#
# if __name__ == '__main__':
#     # print(funt("this is harry","is a himanshu"))
#     sentence = ["this is raghav","manoj is loyal","himanshu is a judge"]
#     que = input("enter your query : ")
#     hard = [funt(que,sentences)for sentences in sentence]
#     print(hard)
#     new = [hards for hards in sorted(zip(hard,sentence))if hards[0]!=0]
#     print(new)
#     print(f'{len(new)} results found')
#     for hard,item in new:
#         print(f'\"{que}\" found in \"{item}\" with {hard}')