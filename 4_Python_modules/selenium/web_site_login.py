from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebsiteLogin:
    def __init__(self, url, username, password, username_field_id, password_field_id, submit_button_id):
        self.url = url
        self.username = username
        self.password = password
        self.username_field_id = username_field_id
        self.password_field_id = password_field_id
        self.submit_button_id = submit_button_id
        self.driver = None  # Initialize driver as None

    def login(self):
        try:
            self.driver = webdriver.Edge()  # Initialize Edge driver
            self.driver.get(self.url)

            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.username_field_id))
            )

            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.password_field_id))
            )

            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.submit_button_id))
            )

            username_field.send_keys(self.username)
            password_field.send_keys(self.password)
            submit_button.click()

            print("Login successful (if the element ids are correct)")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the browser (optional)
            # if self.driver:
            #     self.driver.quit()
            pass
# Example Usage:
if __name__ == "__main__":
    website_url = "https://my.netron.in/customer_portal"
    user_name = "umesh@svr"
    pass_word = "pass@1840"
    username_id = "username"
    password_id = "password"
    submit_id = "submit"

    login_instance = WebsiteLogin(website_url, user_name, pass_word, username_id, password_id, submit_id)
    login_instance.login()