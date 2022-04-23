def multis_50():
	for i in range(1, 51):
		if i % 3 == 0 and i % 7 == 0:
                        print('CloudComputing',i)
		elif i % 3 == 0:
			print('Cloud',i)
		elif i % 7 == 0:
			print('Computing', i)
multis_50()
