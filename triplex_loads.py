from functions import *

'''

i = 0
print("Associated Node:")

node = input()
print("enter phases:")

phases = input()
print("enter a csv file name:")

file_name = input()

house_player = "_player"

print("how many instances?")

counter = input()

while i < int(counter):

	trip_player = trip_load_with_player("House_"+node+"_"+str(i)+"_"+phases,phases,house_player+str(i),file_name+str(i))
	print(trip_player)
	i = i + 1


OL = overhead_lines_objects("OL","C","646","xfrmr")
#print(OL)

SP_xfmr = center_tapped_xfmr_object("xfmr_CT","CS","node 646","trip_node_645","CS25_config")
#print(SP_xfmr)


counter = 6
i = 1

while i < counter:
    xfmr = center_tapped_xfmr_object("xfmr_652A"+"_"+str(i),"AS","meter_652A","trip_node_652A"+"_"+str(i),"AS100_config")
#    print(xfmr)
    triplex_node = trip_node("trip_node_652A"+"_"+str(i),"AS")
#    print(triplex_node)
    i = i + 1

counter = 9
From = "trip_node_652A_1"
i = 1

counter = [9, 17,25,33,41]
From = ["trip_node_652_A_"+str(x) for x in range(1,6)]
'''

def trips(counter,From):
    xfmr = center_tapped_xfmr_object("xfmr_652A"+"_"+str(counter),"AS","meter_652_A","trip_node_652_A"+"_"+str(counter),"AS100_config")
    print(xfmr)
    trip_nodes = trip_node("trip_node_652_A_"+str(counter),"AS")
    print(trip_nodes)
    for k in range(1,9):
        trip_line_counter = 8*(counter - 1) + k
        meter = meter_object("house_meter_"+str(trip_line_counter),"AS")
        trip_lines = triplex_line("trip_line_652_A"+"_"+str(trip_line_counter),From,"trip_meter_652_A"+"_"+str(trip_line_counter),"AS")
        print(trip_lines)
        print(meter)

#        print(trip_lines)
#        print(xfmr)
#        print(trip_nodes)
#        starting_line = starting_line + 1
#        print(trip_lines)
#       print(meter)
#        return starting_line

for i in range(1,6):
    trips(i,"trip_node_652A_"+str(i))

'''
for result in results:
    (c,f) = result
    starting_line = trips(c,f,starting_line)

for k in range(40):
    while i < counter:
        trip_lines = triplex_line("trip_line_652A"+"_"+str(i),From,"trip_meter_652_A"+"_"+str(i),"AS")
        meter = meter_object("trip_meter_652_A"+"_"+str(i),"AS")

        print(trip_lines)
        print(meter)
        i = i + 1
        k = k + 1
    print('#######################################')
    print(k)
    print('#######################################')
    counter = 17
    From = "trip_node_652A_2"
    while i < counter:
        trip_lines = triplex_line("trip_line_652A"+"_"+str(i),From,"trip_meter_652_A"+"_"+str(i),"AS")
        meter = meter_object("trip_meter_652_A"+"_"+str(i),"AS")
        print(trip_lines)
        print(meter)
        i = i + 1
        k = k + 1
    counter = 25
    From = "trip_node_652A_3"
    while i < counter:
        trip_lines = triplex_line("trip_line_652A"+"_"+str(i),From,"trip_meter_652_A"+"_"+str(i),"AS")
        meter = meter_object("trip_meter_652_A"+"_"+str(i),"AS")
        print(trip_lines)
        print(meter)
        i = i + 1
        k = k + 1
    counter = 33
    From = "trip_node_652_4"
    while i < counter:
        trip_lines = triplex_line("trip_line_652A"+"_"+str(i),From,"trip_meter_652_A"+"_"+str(i),"AS")
        meter = meter_object("trip_meter_652_A"+"_"+str(i),"AS")
        print(trip_lines)
        print(meter)
        i = i + 1
        k = k + 1
    counter = 41
    From = "trip_node_652_5"
    while i < counter:
        trip_lines = triplex_line("trip_line_652A"+"_"+str(i),From,"trip_meter_652_A"+"_"+str(i),"AS")
        meter = meter_object("trip_meter_652_A"+"_"+str(i),"AS")
        print(trip_lines)
        print(meter)
        i = i + 1
        k = k + 1
'''



