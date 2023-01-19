

from Selenium_Wrapper import SeleniumWrapper

def test_registration(func):
    obsw=SeleniumWrapper(func)

    obsw.click_element(("link text","Register"))
    obsw.click_element(("id","gender-female"))

    obsw.enter_text(("id","FirstName"),value="hello")
    obsw.enter_text(("id","LastName"),value="world")
    obsw.enter_text(("id","Email"),value="helloworld@gmail.com")
    obsw.enter_text(("id","Password"),value="pass123$")
    obsw.enter_text(("id","ConfirmPassword"),value="pass123$")
    obsw.click_element(("id","register-button"))