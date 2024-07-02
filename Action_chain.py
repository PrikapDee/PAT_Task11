from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Action:
    # locator
    xpath_iframe = "//iframe[@class='demo-frame']"
    drag_box = "//div[@id='draggable']"
    drop_box = "//div[@id='droppable']"

    def __init__(self, web_url):

        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # open url method to open url
    def open_url(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True
        except Exception as e:
            print("unable to open url")
            return False

    # drag and drop method
    def drag_drop(self):
        try:
            # call open url method
            self.open_url()
            sleep(3)
            # through Xpath find iframe location
            iframe_location = self.driver.find_element(by=By.XPATH, value=self.xpath_iframe)
            # now switch to frame and in argument give location of iframe
            self.driver.switch_to.frame(iframe_location)
            # action object of action class to use drag and drop
            action = ActionChains(self.driver)
            # source variable to get drag box location
            source = self.driver.find_element(by=By.XPATH, value=self.drag_box)
            # target location where user need to drop
            target = self.driver.find_element(by=By.XPATH, value=self.drop_box)
            # first check source and target are displayed
            if source.is_displayed() and target.is_displayed():
                # check source and target are enabled
                if source.is_enabled() and target.is_enabled():
                    # use of drag_drop method to drag box and drop it target location
                    action.drag_and_drop(source, target).perform()
                    return True
        # use of nosuchelementexception if element is not find by selenium
        except NoSuchElementException as e:
            print("error:", e)
            return False

        finally:
            self.driver.quit()


if __name__ == "__main__":
    url = "https://jqueryui.com/droppable/"
    action_obj1 = Action(url)
    action_obj1.drag_drop()
