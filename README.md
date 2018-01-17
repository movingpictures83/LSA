# LSA
# Language: Python
# Input: CSV (abundances)
# Output: CSV (associations)

PluMA plugin to run Local Similarity Analysis (Ruan, 2006),
a technique for computing complex and nonlinear associations
between members of a community, based on their abundances.

The plugin accepts input in the form of a CSV file with rows
representing samples and columns representing community members,
with entry (i, j) containing the abundances of member j in sample i.

The plugin then produces an output CSV file that contains
these associations.  Members correspond to both rows and columns,
and entry (i, j) contains the association between member i and member j.
