def first_non_repeating_character(str):
       
       char_count={}

       for char in str:
              if char not in char_count:
                     char_count[char]=1
              else:
                     char_count[char]+=1           
       for char in char_count:
              if char_count[char]==1:
                     return char
                     


                     
              
def chars_to_lengths(s):
       
       if not s:
              return ""

       output=""
       count = 1

       for i in range(1,len(s)):
              a=s[i]
              b=s[i-1]
              if s[i]==s[i-1]:
                     count+=1
              else:
                     output+= s[i-1] + str(count)
                     count=1       
       output += s[-1] + str(count)
    
       return output
      





       


print(first_non_repeating_character("rrretyt"))
print(chars_to_lengths("aaabbcb"))