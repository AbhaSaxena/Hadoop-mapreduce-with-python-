# Hadoop-mapreduce-with-python
This is a hadoop project implementing MapReduce with python streaming.

The 3 files genchanA.txt, genchanB.txt, genchanC.txt contain data in form of key-value pairs with showname(as key) and channel(as value). The other 3 files gennumA.txt, gennumB.txt and gennumC.txt contain key-value pairs with showname(as key) and no. of viewers(as value). Objective is to join the 2 datasets and find total no. of viewers of channel "ABC". The code can be changed to find total no. of viewers of any channel by replacing "ABC" by the name of the channel required.

This is done by making separate mapper and reducer code and run it with python streaming.
