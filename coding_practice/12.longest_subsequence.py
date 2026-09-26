#longest_subsequence_common

#longet_increasing

def longestCommonSubsequence(text1, text2):
    #two pointers
    str1, str2 = 0 , 0 
    subseq = 0

    short = text1
    lon = text2
    if len(text1) > len(text2):
        short = text2
        lon = text1

    while str1 < len(short) and str2 < len(lon):
        if short[str1] == lon[str2]:
            subseq += 1
            str1 += 1
            str2 += 1
        else:
            str2 += 1
    print(subseq)

text1 = input("enter text ")
text2 = input("enter text ")
longestCommonSubsequence(text1,text2)
            
