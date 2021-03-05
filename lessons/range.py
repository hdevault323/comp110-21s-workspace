"""Range example."""

start: int = 0 #tthis is inclusive
stop: int = 101 #this is exclusive
step: int = 10 #counts every 10 

a_range: range = range(start, stop, step)
print(a_range[0])
print(a_range[1])
print(a_range[2])
#ranges have lengths associated with them
print(len(a_range))#finds length of range
print(f"Max value in range: {(a_range[len(a_range)-1])}")

#How is this represented in memory?
a_range: range = range(start, stop, step)
print(a_range.start)
print(a_range.stop)
print(a_range.step)
#when this is printed it is 0,100,and 10


a_range = range(10, 100) #default step is 1


a_range = range(10) #default stop is 10 and start is 1