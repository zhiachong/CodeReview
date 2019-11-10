'''
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]. 
'''

class Solution:
    # checks has negative numbers
    def hasNegativeNumbers(self, intervals):
        for i in intervals:
            if i[0] < 0 or i[1] < 0:
                return True
        return False
    
    # @param intervals, a list of interval
    # @return a list of interval
    def merge(self, intervals):
        length = len(intervals)
        if length == 0 or length == 1: 
            return intervals
        elif (hasNegativeNumbers(intervals)):
            return []
        
        intervals.sort(key = lambda x:x[0])
        result = []
        pre_start = None
        pre_end = None 
        
        for node in intervals:
            if pre_start == None and pre_end == None:
                pre_start = node[0]
                pre_end = node[1] 
            else:  
                if node[0] <= pre_end:
                    if node[1] > pre_end:
                        pre_end = node[1]
            
                if node[0] > pre_end:
                    newnode = [pre_start, pre_end]
                    result.append(newnode)
                
                    pre_start = node[0]
                    pre_end = node[1]
        
        newnode = [pre_start, pre_end]
        result.append(newnode)
        return result  