all_types = {"rap", "rnb", "pop", "heavy metal", "classical", "indie", "jazz", "rock","blues", "rap", "rock", "edm"}
group_1 = {"rap", "rnb", "pop", "jazz", "rock"}
group_2 = {"blues", "rap", "rock", "edm"}

definitely_play = sorted(group_1.intersection(group_2))
perhaps_play = sorted(group1.symmetric_difference(group_2))
do_not_play = sorted(all_types.difference(group_1.union(group_2)))

print("Definitely play: ", end="")
print(definitely_play)
