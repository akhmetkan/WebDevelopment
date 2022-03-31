if __name__ == '__main__':
    d={}
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        d[name]=score
    scores = d.values()
    sort_scores = sorted(list(set(scores))) 
    second_min = sort_scores[1]
    names = []
    for key,value in d.items():  #9
        if value==second_min: #10
            names.append(key)
    names = sorted(names)
    for name in names: #13
        print name 
        
        
