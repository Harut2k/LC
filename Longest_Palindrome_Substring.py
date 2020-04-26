def ispalindrome(temp):
    length = len(temp)
    index1 = 0
    index2 = length-1
    while index1 < index2:
        if(temp[index1]!=temp[index2]):
            return False
        index1+=1
        index2-=1
    return True




def longestPalindrome(s):
    longest_index1=0
    longest_index2=0
    longest_length =0

    string_length = len(s)
    curr_index=0

    temp_index1=0
    temp_index2=1
    while curr_index <string_length:
        temp_index1 = curr_index
        temp_index2 = curr_index+1
        while(temp_index1 >=0 and temp_index2 <string_length):
            if( ispalindrome(s[temp_index1:temp_index2+1])):
                temp_index1-=1
                temp_index2+=1

            else:
                break
        temp_index1+=1
        temp_index2-=1
        if(temp_index2-temp_index1 > longest_length):
            longest_index1=temp_index1
            longest_index2=temp_index2
            longest_length = longest_index2-longest_index1

        temp_index1 = curr_index
        temp_index2 = curr_index+2
        while(temp_index1 >=0 and temp_index2 < string_length):
            if(ispalindrome(s[temp_index1:temp_index2+1])):
                temp_index1-=1
                temp_index2+=1
            else:
                break
        temp_index1+=1
        temp_index2-=1
        if(temp_index2-temp_index1 > longest_length):
            longest_index1=temp_index1
            longest_index2=temp_index2
            longest_length = longest_index2-longest_index1
        curr_index+=1

    #end is exclusive
    longest = s[longest_index1:longest_index2+1]
    return longest






print(longestPalindrome("absofsbeebgsdr"))
