from rdflib import Graph, URIRef, RDF
from rdflib.namespace import FOAF

g = Graph()
g.load('aifbfixed_complete.n3', format='n3')

# f = open("aifb_stripped.nt", "r")

train_split = 0.6
test_split = 0.2
valid_split = 0.2

train_total = int(train_split * len(g))
test_total = int(test_split * len(g))
valid_total = int(valid_split * len(g))

train = open("train.txt", "w")
test = open("test.txt", "w")
valid = open("valid.txt", "w")

i = 0
print(i)
print(len(g))

for s, p, o in g:
    i = i + 1

    formatted_line = '{0}\t{1}\t{2}\n'.format(str(s.encode("utf8")), str(p.encode("utf8")), str(o.encode("utf8")))

    if i < train_total:
        train.write(formatted_line)
    elif train_total <= i < train_total + test_total:
        test.write(formatted_line)
    elif train_total + test_total <= i < train_total + test_total + valid_total:
        valid.write(formatted_line)

print(i)
print(len(g))

train.close()
test.close()
valid.close()
