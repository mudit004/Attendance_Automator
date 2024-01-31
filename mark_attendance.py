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

# Functions
def login(username, password):
        dropdown_element=wait.until(EC.presence_of_element_located((By.ID, 'LoginType')))


        # Create a Select object
        select = Select(dropdown_element)

        # Select the desired option by its visible text
        select.select_by_visible_text('All other Student including Faculty')


        # Find the input element by its formcontrolname attribute
        input_element = driver.find_element(By.CSS_SELECTOR,'[formcontrolname="username"]')
        input_element.send_keys(username)

        input_element = driver.find_element(By.CSS_SELECTOR,'[formcontrolname="password"]')
        input_element.send_keys(password)

        # Find the submit button using xpath
        login_button = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div/div[1]/form/div[6]/div/button[1]")
        # Click the submit button
        login_button.click()

def applyAttendance(_course_name_to_find):
        row_xpath = f'//table[@id="customers"]/tr[./td[2][text() = "{_course_name_to_find}"]]'
        row = wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))
        button = row.find_element(By.XPATH, './td[9]/button')
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        if((check == True)):
                status = False
                while(status == False):
                        button.click()
                        time.sleep(0.5)
                        dialog_box_text=wait.until(EC.presence_of_element_located((By.ID, 'swal2-html-container')))
                        dialog=dialog_box_text.text
                        if(dialog=="Attendance Submitted Successfully"):
                                status=True
                                closeDialogueBox()
                                logout()
                        else:
                                closeDialogueBox()
                                time.sleep(60)
                                
        else:
                button.click()
                time.sleep(0.6)
                closeDialogueBox()
                logout()                          

def closeDialogueBox():
        # Using Class to find the OK Button
        ok_path = f'swal2-confirm'
        ok_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, ok_path)))
        ok_button.click()

def logout():
        logout_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-header/div/div[2]/a")))
        logout_button.click()


# Apply Attendance or Apply Check
print("You want to check website for attendance or mark attendance")
print("1. Apply Attendance")
print("2. Apply Check")
check_int = int(input())
check = (check_int == 2)

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
wait = WebDriverWait(driver, 30)


for cred in credentials:
    username = cred
    password = credentials[cred]
    login(username, password)
    
    apply_attendance_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-dashboard/div/div/mat-card[2]/mat-card-content/div[1]/div[3]/table/tr[2]/td[1]/button")))
    apply_attendance_button.click()

    applyAttendance(course_name_to_find)
