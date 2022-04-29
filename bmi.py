weight = input('請輸入體重(kg): ')
weight = int(weight)
height = input('請輸入身高(cm): ')
height = int(height)
height = height/ 100
bmi = weight / height**2
bmi = float(bmi)
if bmi < 18.5:
	print('你的bmi為', bmi,'體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('你的bmi為', bmi,'體重正常')
elif bmi >= 24 and bmi < 27:
	print('你的bmi為', bmi, '輕度肥胖')
elif bmi >= 27 and bmi < 30:
	print('你的bmi為',bmi, '中度肥胖')
else:
	print('你的bmi為', bmi, '重度肥胖')
