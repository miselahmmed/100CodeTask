#Deep merge.py
#Merge lists of disctionaries by concatenating list-values and updating scalars.

list_a = [{"id":1, "tags":["a", "b"], "count":2, {"id":2, "tags":["c"], "count":1}]
list_b = [{"id":1, "tags":["d"], "count":3}, {"id":3, "tags":["e"], "count":4}]
def deep_merge_by_id(a,b):
    merge