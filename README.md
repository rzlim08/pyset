# PySet
A simple package for quick set operations on CSVs. 



Usage:
pyset <csv1> <csv2> --operation [intersection|complement|union] --columns [numeric] --full

Example:
pyset csv1.csv csv2.csv --operation complement --columns 1,3

Returns the complement of csv1 to csv2 when comparing only the 1st and 3rd columns. This only returns the columns being compared. To return all columns add the option "--full":

pyset csv1.csv csv2.csv --operation complement --columns 1,3 --full



