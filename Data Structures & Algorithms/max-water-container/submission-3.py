class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #height[i] represents the height of the ith bar
        # ok so choose the height[i1] and height[i2]
        #width is i1-i2 and height is min(height[i1],height[i2])
        #return area which is width* height
        left=0
        right=(len(heights))-1
        width =0
        
        while left< right:
            out=(right-left)*min(heights[left],heights[right])
            if width<out:
                width=out
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            
        return width
    """
        width=0
        for i in range(len(heights)):
            for j in range(1,len(heights)):
                out=(j-i)*min(heights[j],heights[i])
                if width<out:
                    width = out
        
        return width
    """