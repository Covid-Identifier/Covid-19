from TestActionLibrary import T
LoginLogout = T()
LoginLogout.openBrowser()
LoginLogout.login('laxu','laxu')
LoginLogout.logout()
LoginLogout.closeBrowser()

print("<<<<<<<<<<Test case 001 passed>>>>>>>>>>>>>>")