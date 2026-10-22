from .common import identifier,integer,number,unique_ids

def run(data):
    jobs=data['batches'];transitions=data['transitions']
    if len(jobs)>12 or len(transitions)>1000:raise ValueError('size')
    unique_ids(jobs);types={identifier(j['type']) for j in jobs};rules={}
    for j in jobs:number(j['max_carryover'],0,1e12)
    for t in transitions:
        pair=(identifier(t['from']),identifier(t['to']))
        if pair in rules:raise ValueError('duplicate_transition')
        number(t['carryover'],0,1e12);integer(t['clean_cost'],0,10**9);number(t.get('after_clean',0),0,1e12);rules[pair]=t
    def transition(i,j):
        t=rules.get((jobs[i]['type'],jobs[j]['type']))
        if t is None:return None
        if t['carryover']<=jobs[j]['max_carryover']:return (0,False,t['carryover'])
        if t.get('after_clean',0)<=jobs[j]['max_carryover']:return (t['clean_cost'],True,t.get('after_clean',0))
        return None
    n=len(jobs)
    if not n:return {'feasible':True,'cost':0,'order':[],'transitions':[]}
    dp={(1<<i,i):(0,(jobs[i]['id'],),[]) for i in range(n)}
    for mask in range(1,1<<n):
        for last in range(n):
            if (mask,last) not in dp:continue
            cost,path,receipts=dp[mask,last]
            for j in range(n):
                if mask>>j&1:continue
                t=transition(last,j)
                if t is None:continue
                c,clean,residual=t;key=(mask|1<<j,j);candidate=(cost+c,path+(jobs[j]['id'],),receipts+[{'from':jobs[last]['id'],'to':jobs[j]['id'],'clean':clean,'residual':residual,'cost':c}])
                if key not in dp or candidate[:2]<dp[key][:2]:dp[key]=candidate
    answers=[v for (mask,_),v in dp.items() if mask==(1<<n)-1]
    if not answers:return {'feasible':False,'cost':None,'order':[],'transitions':[]}
    best=min(answers,key=lambda x:x[:2]);return {'feasible':True,'cost':best[0],'order':list(best[1]),'transitions':best[2]}
