import timeit
from googlesearch import search
n=input()
start = timeit.default_timer()
# to search
query = n
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(j)
stop = timeit.default_timer()
exitime=(stop - start)
print(exitime)
