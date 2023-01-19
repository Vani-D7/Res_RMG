from Selenium_Wrapper import SeleniumWrapper



def test_login(func):  ### func holds driver  in conftest.py
    sw=SeleniumWrapper(func)
    sw.click_element(("link text","Log in"))

    sw.enter_text(("id","Email"),value="helloworld@gmail.com")
    sw.enter_text(("id","Password"),value="Password123")
    sw.click_element(("xpath","//input[@value='Log in']"))