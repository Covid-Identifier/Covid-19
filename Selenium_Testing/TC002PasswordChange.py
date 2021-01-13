from TestActionLibrary import T
PC = T()
PC.openBrowser()
PC.login('laxu','laxu')
PC.PasswordChange('laxu','laxu')
PC.logout()
PC.closeBrowser()

print("<<<<<<<<<<Test case 002 passed>>>>>>>>>>>>>>")