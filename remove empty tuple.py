tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
                  ('krishna', 'akbar', '45'), ('',''),()]
tu=[]
for t in tuples:
    if t:
        tu.append(t)

print(tu)