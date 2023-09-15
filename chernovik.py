#chernovik

dict1 = dict(id1 = [2, 'id33'], id2 = [5, 'id36'], id44 = [8, 'id33'])



keys = [key for key, value in dict1.items() if value[1] == 'id33']
print(dict1[keys[1]][0])