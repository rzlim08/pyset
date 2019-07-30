python pyset.py ../test_ps/data/simple2.csv --operation dedupe
python pyset.py ../test_ps/data/simple3.csv --operation dedupe
python pyset.py ../test_ps/data/simple3.csv ../test_ps/data/simple2.csv --operation intersection
python pyset.py ../test_ps/data/simple2.csv ../test_ps/data/simple.csv --operation intersection
python pyset.py ../test_ps/data/simple2.csv ../test_ps/data/simple.csv --operation union
python pyset.py ../test_ps/data/simple.csv ../test_ps/data/simple2.csv --operation complement
python pyset.py ../test_ps/data/simple.csv ../test_ps/data/simple2.csv --columns 1,3 2,3 --operation intersection
