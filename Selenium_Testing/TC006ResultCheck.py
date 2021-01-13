from TestActionLibrary import T
RC = T()
RC.openBrowser()
RC.login('laxu','laxu')
RC.Questionaries()
RC.logout()
RC.closeBrowser()

print("<<<<<<<<<<Test case 006 passed>>>>>>>>>>>>>>")