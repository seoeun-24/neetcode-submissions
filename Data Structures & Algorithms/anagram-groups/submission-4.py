class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #return array of the lists which has same alphabet

        #read the first one and compare the next one. if it is different with the comparing one do not append in the new array.
        
        new ={}

        for word in strs:
            key = "".join(sorted(word))
            if key in new:
                new[key].append(word)
            else:
                new[key]=[word]

        result =[]

        for key in new:
            result.append(new[key])

        return result
                
            

        
        

                    
                    

        