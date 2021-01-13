from TestActionLibrary import T
VC = T()
VC.openBrowser()
VC.login('laxu','laxu')
VC.Visualization_check()
VC.logout()
VC.closeBrowser()

print("<<<<<<<<<<Test case 004 passed>>>>>>>>>>>>>>")