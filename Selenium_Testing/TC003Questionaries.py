from TestActionLibrary import T
QA = T()
QA.openBrowser()
QA.login('laxu','laxu')
QA.Questionaries()
QA.logout()
QA.closeBrowser()

print("<<<<<<<<<<Test case 003 passed>>>>>>>>>>>>>>")