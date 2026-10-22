import unittest,itertools,random
from recipe_carryover_planner import run
class DomainTests(unittest.TestCase):
 def test_direction_matters(self):
  r=run({'batches':[{'id':'a','type':'A','max_carryover':0},{'id':'b','type':'B','max_carryover':0}],'transitions':[{'from':'A','to':'B','carryover':0,'clean_cost':9},{'from':'B','to':'A','carryover':1,'clean_cost':9}]});self.assertEqual(r['order'],['a','b']);self.assertEqual(r['cost'],0)
 def test_missing_transition_is_infeasible(self):self.assertFalse(run({'batches':[{'id':s,'type':s,'max_carryover':0} for s in 'ab'],'transitions':[]})['feasible'])
 def test_cleaning_cannot_remove_enough(self):
  self.assertFalse(run({'batches':[{'id':s,'type':s,'max_carryover':0} for s in 'ab'],'transitions':[{'from':a,'to':b,'carryover':2,'clean_cost':1,'after_clean':1} for a,b in [('a','b'),('b','a')]]})['feasible'])
 def test_exhaustive_permutation_cost(self):
  rng=random.Random(8)
  for _ in range(10):
   jobs=[{'id':str(i),'type':str(i),'max_carryover':0} for i in range(6)];ts=[{'from':a['type'],'to':b['type'],'carryover':1,'clean_cost':rng.randrange(1,10)} for a in jobs for b in jobs if a!=b];cost={(t['from'],t['to']):t['clean_cost'] for t in ts}
   best=min(sum(cost[a['id'],b['id']] for a,b in zip(path,path[1:])) for path in itertools.permutations(jobs));self.assertEqual(run({'batches':jobs,'transitions':ts})['cost'],best)
 def test_empty(self):self.assertEqual(run({'batches':[],'transitions':[]})['cost'],0)
