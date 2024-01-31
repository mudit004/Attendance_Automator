import time

#selenium for web automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from dotenv import dotenv_values

# Indivisual credentials
credentials = dotenv_values(".env")

# Course List
courses = ["SYSTEM SOFTWARE", "ENERGY ENGINEERING", "DESIGN AND ANALYSIS OF ALGORITHMS", "DIGITAL ELECTRONIC CIRCUITS LABORATORY", "SOFTWARE ENGINEERING", "OPERATING SYSTEMS"]

print("Select the course whose attendance need to be marked")
for i in range(len(courses)):
    print((i+1), end=":")
    print(courses[i])

course_index = int(input())
course_index = course_index- 1
course_name_to_find = courses[course_index]

#webdriver for chrome
driver = webdriver.Chrome()
driver.get("https://timetable.iitr.ac.in:8000/#/home")

# Set a maximum wait time for the elements to be available
driver.maximize_window()
wait = WebDriverWait(driver, 10)

for cred in credentials:

    dropdown_element=wait.until(EC.presence_of_element_located((By.ID, 'LoginType')))


    # Create a Select object
    select = Select(dropdown_element)

    # Select the desired option by its visible text
    select.select_by_visible_text('All other Student including Faculty')

    username = cred
    password = credentials[cred]

    # Find the input element by its formcontrolname attribute
    input_element = driver.find_element(By.CSS_SELECTOR,'[formcontrolname="username"]')
    input_element.send_keys(username)

    input_element = driver.find_element(By.CSS_SELECTOR,'[formcontrolname="password"]')
    input_element.send_keys(password)

    # Find the submit button using xpath
    login_button = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div/div[1]/form/div[6]/div/button[1]")
    # Click the submit button
    login_button.click()

    apply_attendance = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-dashboard/div/div/mat-card[2]/mat-card-content/div[1]/div[3]/table/tr[2]/td[1]/button")))
    apply_attendance.click()

    # Use XPath to find the row with the specified course name
    row_xpath = f'//table[@id="customers"]/tr[./td[2][text() = "{course_name_to_find}"]]'
    row = wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))

    # Find the button in the row and click it
    button = row.find_element(By.XPATH, './td[9]/button')
    driver.execute_script("arguments[0].scrollIntoView(true);", button)


    # //*[@id="customers"]/tr[7]/td[9]/button
    button.click()
    
    #wait for 0.5 second
    time.sleep(0.5)

    # Using Class to find the OK Button
    ok_path = f'swal2-confirm'
    ok_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, ok_path)))
    ok_button.click()

    # Logout
    logout_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-header/div/div[2]/a")))
    logout_button.click()

