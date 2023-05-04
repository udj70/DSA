# task- Given- string with duplicate letters
# return lexiogrphically smaller subsequnce with unique characters

# approach 1- 
# monotonic stack based approach, at every charcter we have two options, either to select it or ignore it
#   select it, if current char is smaller than stack top or stack is empty
#   ignore it, if current char is visited
#   if selected current char, then remove all larger chars from stack, if they are present in string again after current char
#   to check if char is present again in string, maintain a array to store last index of each char


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]

        # create last index and visited array of size 26
        lastIndex=[-1]*26
        visited=[False]*26

        # to index on any char in 0-25 range do ord(char)-ord('a')
        for i in range(len(s)):
            lastIndex[ord(s[i])-ord('a')]=i
        
        # trvaerse each char in string
        # approach is same as finding next smaller to left, just inplace of number here chars present
        for i in range(len(s)):

            # if current char is already picked, continue
            if visited[ord(s[i])-ord('a')]:
                continue

            # if stack is empty i.e no smaller char present till now
            # if current char is larger than no need to pop
            # if current index is more than last index of element to be poped, than dont pop, coz element to be poped is not present again after current char 
            char = s[i]
            while(len(stack) and char<s[stack[-1]] and i <lastIndex[ord(s[stack[-1]])-ord('a')] ):
                    popped_index=stack.pop()

                    # after poping unvisit that char
                    visited[ord(s[popped_index])-ord('a')]=False

            # add current char index always
            stack.append(i)
            visited[ord(s[i])-ord('a')]=True
        ans=''
        while(len(stack)):
            ans+=s[stack.pop()]
        
        # return reverse of string
        return ans[::-1]
        
                
s=Solution()
st="dbbbabadcdcbdaddddbbcbdaaadbdaadcaaabbab"
print(s.removeDuplicateLetters(st))
            