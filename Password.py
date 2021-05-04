password = 'a123456'
x = 1
while True and x < 4:
	enterpassword = input ('請輸入密碼:')
	if enterpassword == password:
		print('成功登入')
		break
	else:
		if x != 3:
			print('密碼錯誤，還有', 3 - x, '次機會')
			x = x + 1
		else:
			print('密碼錯誤超過三次，登入失敗')
			break


	


  
	





