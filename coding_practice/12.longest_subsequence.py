#longet_increasing

#longest_subsequence_common
def longestCommonSubsequence(text1, text2):
    #two pointers
    # str1, str2 = 0 , 0 
    # subseq = 0

    # short = text1
    # lon = text2
    # if len(text1) > len(text2):
    #     short = text2
    #     lon = text1

    # while str1 < len(short) and str2 < len(lon):
    #     if short[str1] == lon[str2]:
    #         subseq += 1
    #         str1 += 1
    #         str2 += 1
    #     else:
    #         str2 += 1
    # print(subseq)
    
    #bottom-up approach - 2d - table
    m = len(text1)
    n = len(text2)

    dp = [[0] * (n+1) for _ in range(m+1)]
    print(dp)

    for i in range(1,m+1):

        for j in range(1, n+1):

            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j] = max(dp[i-1][j],
                                dp[i][j-1]
                            )
    return dp[m][n]


text1 = input("enter text ")
text2 = input("enter text ")
longestCommonSubsequence(text1,text2)
            
