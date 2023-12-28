import dictio as aneeja # dictio is treated as a namespace
print(aneeja.lis[0]) # here we are accessing lis inside the namespace


from dictio import tup   # from dictio namespace we are importing only tup object from tuple class.
print(tup)
