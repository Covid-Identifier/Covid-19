from TestActionLibrary import T
PC = T()
PC.openBrowser()
PC.login('laxu','laxu')
PC.ProfileCheck()
PC.logout()
PC.closeBrowser()

print("<<<<<<<<<<Test case 005 passed>>>>>>>>>>>>>>")