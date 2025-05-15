from PageObjects.HomePage import HomePage
from TestData.HomePageData import Data
from TestLocators.HomePageLocators import Locators
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestHomePage:

    def test_world_population(self):
        try:
            # create an empty list to store web elements
            population=[]
            home=HomePage()
            home.start(Data.url)

            # using while loop for continuous iteration
            while True:
                # get total_population count web element
                total_population_count=home.wait.until(EC.presence_of_element_located((By.XPATH,Locators.total_world_population)))

                # append the elements into list
                population.append(total_population_count)

                # Iterate to print the text present in the element
                for data in population:
                    print(f"Current World Population: {data.text}")

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: Problem fetching the data!", error)

        except KeyboardInterrupt:
            print(" Monitoring stopped by user.")

        finally:
            home.driver.quit()
            print("Browser Closed")




