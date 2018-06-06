#coding utf-8

while True:
	
	try:
		
		num_torneios, num_alunos = map(int, raw_input().split())
		coef = map(int, raw_input().split())
		
		set_result = set()
		
		if(num_torneios == 1):
			print "Lucky Denis!"
		elif(num_torneios == 2):
			for i in range(num_alunos):
				for j in range(num_alunos):
					result = (i + 1) * coef[0] + (j + 1) * coef[1]
					set_result.add(result)
			if(len(set_result) == num_alunos ** num_torneios):
				print "Lucky Denis!"
			else:
				print "Try again later, Denis..."
		else:
			for i in range(num_alunos):
				for j in range(num_alunos):
					for k in range(num_alunos):
						result = (i + 1) * coef[0] + (j + 1) * coef[1] + (k + 1) * coef[2]
						set_result.add(result)
			if(len(set_result) == num_alunos ** num_torneios):
				print "Lucky Denis!"
			else:
				print "Try again later, Denis..."

	except EOFError:
		break
