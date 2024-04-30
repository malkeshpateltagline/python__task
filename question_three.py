import operator as op

sentences = ['My name is Ram', 'He is a good person', 
             'You should be careful while coding', 'He can do better', 
             'The person is mysterious', 'Jay Shree Ram', 'It is my pen']
word_trees=[]
for i in sentences:
    res=i.split(' ')
    word_trees.append(res)

print('\nword_trees = {}'.format(word_trees))
print('\nNumber of time each word appears : ')
occurrence={}
sentences=[]
for i in word_trees:
    sentences+=i
    
for i in sentences:
        res = op.countOf(sentences,i)
        occurrence[i]=res
        
print(occurrence)
           
