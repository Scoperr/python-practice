def howsum(targetsum,arr):
    if targetsum == 0: return []
    if targetsum < 0: return None
    for i in arr:
        remainder = targetsum - i
        remainderResult = howsum(remainder, arr)
        if remainderResult != None:
            return
            
