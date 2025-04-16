x = {"hello", "world"}
frozen_set = frozenset(x)
print(frozen_set)
# frozenset() is a function, it returns an unchangeable frozen set object. Is like a set object, but frozen.

"""
frozenset.add("!")
print(frozens_set)

Above code doesn't work b/c "type object 'frozenset' has no attribute 'add'"
"""

# Adding frozen_set to a non-frozen set works b/c the non-frozen set object is mutable.
non_frozen_set = {"deers", "gooses", "fishes", "mooses"}
non_frozen_set.add(frozen_set)
print(non_frozen_set)

# The order of items in the non_frozen_set keeps moving around. Why? B/c it's unordered = Python isn't keeping track of
#   the item order.

"""
How is a frozen set different to a non-frozen set?
   Frozen sets are - immutable (cannot change after creation), hashable (can be used as a dict key/added to a set)
   Sets are - mutable (items can be added/removed), not hashable (can't be used as kes in a dict/added to another set). 
"""