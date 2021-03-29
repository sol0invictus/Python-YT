# Additional useful data-types in the collections library
from collections import defaultdict,deque,Counter

# ---- defaultdict -----
# This dictionary sets a default value for unset keys
test = {}

# The following line should give an error as key '1' has not been defined yet
#print(test[1])

# With default dict this would work
test = defaultdict(int)
print(test[1])

# ---- deque ----
# deque is just a double ended queue. You can append to both sides and pop from both sides. It is quicker than list

d = deque(['f', 'g', 'h', 'i', 'j'])
print(d.pop())
print(d.popleft())


#  --- Counter ---
# rapid tallies
test=['a','b','a']
cnt=Counter(test)
print(cnt['a'])
print(cnt)
