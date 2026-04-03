result = []
n = 3
def f(curr_str, open_cnt, close_cnt):
    if len(curr_str) == n*2:
        result.append(curr_str)
        return
            
    if open_cnt<n:
        f(curr_str + '(', open_cnt+1, close_cnt)
    if close_cnt<open_cnt:
        
        f(curr_str+')', open_cnt, close_cnt+1)
            
f('',0,0)
print(result)
