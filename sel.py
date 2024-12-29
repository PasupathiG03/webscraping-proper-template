# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
# import time


# options = webdriver.ChromeOptions()
# # options.add_argument("--headless")  # Run in headless mode (without opening a browser window)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# def extract_phone_names(search_query):
#     driver.get("https://www.flipkart.com")

#     try:
#         close_button = driver.find_element(By.XPATH, "//button[text()='✕']")
#         close_button.click()
#     except:
#         pass

#     search_bar = driver.find_element(By.NAME, "q")
#     search_bar.clear()
#     search_bar.send_keys(search_query)
#     search_bar.send_keys(Keys.RETURN)

#     time.sleep(3)  

#     phone_names = []
#     phone_price = []
#     phone_spec = []
#     page_count = 1

#     while True:

#         print(f"Scraping page {page_count}")
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class, 'CGtC98')]//div[contains(@class, 'KzDlHZ')]"))
#         )

#         phone_elements = driver.find_elements(By.XPATH, "//a[contains(@class, 'CGtC98')]//div[contains(@class, 'KzDlHZ')]")
#         for phone in phone_elements:
#             phone_names.append(phone.text)

#         phoneprice_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'Nx9bqj _4b5DiR')]")
#         for price in phoneprice_elements:
#             phone_price.append(price.text)
        
#         phone_spec_elements = driver.find_elements(By.XPATH, "//ul[contains(@class, 'G4BRas')]")
#         for spec in phone_spec_elements:
#             phone_spec.append(spec.text)

#         try:
#             # next_button = driver.find_element(By.XPATH, "//a[@class='_9QVEpD']")
#             # next_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[11]')

#             if page_count == 1:
#                 next_button = driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[11]")
#             else:
#                 next_button = driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[12]")
#             next_button.click()

#             WebDriverWait(driver, 10).until(
#                 EC.staleness_of(phone_elements[0])  
#             )
#             page_count += 1
#             time.sleep(3)  
#         except:
#             print("No more pages to scrape.")
#             break

#     min_length = min(len(phone_names), len(phone_price), len(phone_spec)) 
#     phone_names = phone_names[:min_length]
#     phone_price = phone_price[:min_length]
#     phone_spec = phone_spec[:min_length]

#     while len(phone_names) < min_length:
#         phone_names.append("N/A")
#     while len(phone_price) < min_length:
#         phone_price.append("N/A")
#     while len(phone_spec) < min_length:
#         phone_spec.append("N/A")
    

#     phone_spec = [", ".join(spec.split("\n")) for spec in phone_spec]  
#     return phone_names, phone_price, phone_spec



# def save_to_excel(phone_names, phone_price, phone_spec, filename="samsung_phone_names.xlsx"):
#     df = pd.DataFrame({
#         "Phone Name": phone_names,
#         "Phone Price": phone_price,
#         "Phone Spec": phone_spec

#     })
    
#     df.to_excel(filename, index=False)
#     print(f"Data saved to {filename}")

# if __name__ == "__main__":
#     search_query = "samsung 5g mobile"  
#     phone_names, phone_price, phone_spec = extract_phone_names(search_query)

#     if phone_names and phone_price and phone_spec:
#         save_to_excel(phone_names, phone_price, phone_spec)
#     else:
#         print("No phone names or data found.")

#     driver.quit()


# import tkinter as tk
# import tkinter.ttk as ttk
# from tkinter import ttk
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
# import time
# import os
# import threading
# from tkinter import messagebox, filedialog
# from selenium import webdriver
# from tkinter import ttk





# def start_scraping():
#     search_query = entry.get()  
#     if not search_query:
#         messagebox.showerror("Input Error", "Please enter a search query.")
#         return

#     status_label.config(text="Scraping in progress...")
#     progress_bar.start()

#     threading.Thread(target=start_scraping, args=(search_query,), daemon=True).start()

#     try:
#         phone_names, phone_price, phone_spec = extract_phone_names(search_query)
#         if phone_names and phone_price and phone_spec:
#             save_to_excel(phone_names, phone_price, phone_spec)
#             status_label.config(text="Scraping finished successfully!")
#             messagebox.showinfo("Success", "Data saved successfully!")
#         else:
#             messagebox.showerror("Error", "No data found.")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))
#     finally:
#         progress_bar.stop()

# def extract_phone_names(search_query):
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://www.flipkart.com")

#     try:
#         close_button = driver.find_element(By.XPATH, "//button[text()='✕']")
#         close_button.click()
#     except:
#         pass

#     search_bar = driver.find_element(By.NAME, "q")
#     search_bar.clear()
#     search_bar.send_keys(search_query)
#     search_bar.send_keys(Keys.RETURN)

#     time.sleep(3)

#     phone_names = []
#     phone_price = []
#     phone_spec = []
#     page_count = 1


#     while True:
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class, 'CGtC98')]//div[contains(@class, 'KzDlHZ')]"))
#         )

#         phone_elements = driver.find_elements(By.XPATH, "//a[contains(@class, 'CGtC98')]//div[contains(@class, 'KzDlHZ')]")
#         for phone in phone_elements:
#             phone_names.append(phone.text)

#         phoneprice_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'Nx9bqj _4b5DiR')]")
#         for price in phoneprice_elements:
#             phone_price.append(price.text)

#         phone_spec_elements = driver.find_elements(By.XPATH, "//ul[contains(@class, 'G4BRas')]")
#         for spec in phone_spec_elements:
#             phone_spec.append(spec.text)

#         print(f"Scraping page {page_count}...")


#         next_button_found = False

#         try:
#             next_button = driver.find_element(By.XPATH, "//a[contains(@class, '_9QVEpD')]//span[text()='Next']")
#             next_button.click()
#             next_button_found = True
#             print("Found 'Next' button and clicked.")
#         except:
#             print("No 'Next' button found, trying page numbers...")

#         if not next_button_found:
#             page_links = driver.find_elements(By.XPATH, "//a[contains(@class, 'cn++Ap A1msZJ')]")
#             if not page_links:
#                 page_links = driver.find_elements(By.XPATH, "//a[contains(@class, 'cn++Ap')]")

#             if len(page_links) > 1:  
#                 print(f"Found page links: {len(page_links)}")
#                 page_links[-1].click()
#                 next_button_found = True
#                 print(f"Clicked last page link: {page_links[-1].text}")

#         if not next_button_found:
#             print("No more pages found, scraping finished.")
#             break
#         page_count += 1
#         time.sleep(3)

#     min_length = min(len(phone_names), len(phone_price), len(phone_spec))
#     phone_names = phone_names[:min_length]
#     phone_price = phone_price[:min_length]
#     phone_spec = phone_spec[:min_length]

#     while len(phone_names) < min_length:
#         phone_names.append("N/A")
#     while len(phone_price) < min_length:
#         phone_price.append("N/A")
#     while len(phone_spec) < min_length:
#         phone_spec.append("N/A")

#     phone_spec = [", ".join(spec.split("\n")) for spec in phone_spec]
#     driver.quit()

#     return phone_names, phone_price, phone_spec

# def save_to_excel(phone_names, phone_price, phone_spec):
#     filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
#     if filename:
#         df = pd.DataFrame({
#             "Phone Name": phone_names,
#             "Phone Price": phone_price,
#             "Phone Spec": phone_spec
#         })
#         df.to_excel(filename, index=False)
#         print(f"Data saved to {filename}")

# root = tk.Tk()
# root.title("Phone Scraper")

# search_label = tk.Label(root, text="Enter search query (e.g., 'Samsung 5G Mobile'):")
# search_label.pack(padx=10, pady=5)

# entry = tk.Entry(root, width=50)
# entry.pack(padx=10, pady=5)

# start_button = tk.Button(root, text="Start Scraping", command=start_scraping)
# start_button.pack(padx=10, pady=5)

# progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
# progress_bar.pack(padx=10, pady=10)

# status_label = tk.Label(root, text="Enter search query and click 'Start Scraping'.")
# status_label.pack(padx=10, pady=5)

# root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def update_status_page(page_num):
    status_label.config(text=f"Scraping page {page_num}...")
    progress_bar['value'] = page_num  
    root.update_idletasks()  

def scrape_and_save(search_query):
    try:
        phone_names, phone_price, phone_spec = extract_phone_names(search_query)
        if phone_names and phone_price and phone_spec:
            save_to_excel(phone_names, phone_price, phone_spec)
            status_label.config(text="Scraping finished successfully!")
            messagebox.showinfo("Success", "Data saved successfully!")
        else:
            messagebox.showerror("Error", "No data found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        progress_bar.stop()

def start_scraping():
    search_query = entry.get()  
    if not search_query:
        messagebox.showerror("Input Error", "Please enter a search query.")
        return

    status_label.config(text="Scraping in progress...")
    progress_bar.start()

    threading.Thread(target=scrape_and_save, args=(search_query,), daemon=True).start()

def extract_phone_names(search_query):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.flipkart.com")

    try:
        close_button = driver.find_element(By.XPATH, "//button[text()='✕']")
        close_button.click()
    except:
        pass

    search_bar = driver.find_element(By.NAME, "q")
    search_bar.clear()
    search_bar.send_keys(search_query)
    search_bar.send_keys(Keys.RETURN)

    time.sleep(3)

    phone_names = []
    phone_price = []
    phone_spec = []
    page_count = 1

    while True:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class, 'CGtC98')]//div[contains(@class, 'KzDlHZ')]"))
        )

        phone_elements = driver.find_elements(By.XPATH, "//a[contains(@class, 'CGtC98')]//div[contains(@class, 'KzDlHZ')]")
        for phone in phone_elements:
            phone_names.append(phone.text)

        phoneprice_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'Nx9bqj _4b5DiR')]")
        for price in phoneprice_elements:
            phone_price.append(price.text)

        phone_spec_elements = driver.find_elements(By.XPATH, "//ul[contains(@class, 'G4BRas')]")
        for spec in phone_spec_elements:
            phone_spec.append(spec.text)

        print(f"Scraping page {page_count}...")
        update_status_page(page_count)  

        next_button_found = False

        try:
            next_button = driver.find_element(By.XPATH, "//a[contains(@class, '_9QVEpD')]//span[text()='Next']")
            next_button.click()
            next_button_found = True
            print("Found 'Next' button and clicked.")
        except:
            print("No 'Next' button found, trying page numbers...")

        if not next_button_found:
            page_links = driver.find_elements(By.XPATH, "//a[contains(@class, 'cn++Ap A1msZJ')]")
            if not page_links:
                page_links = driver.find_elements(By.XPATH, "//a[contains(@class, 'cn++Ap')]")

            if len(page_links) > 1:  
                print(f"Found page links: {len(page_links)}")
                page_links[-1].click()
                next_button_found = True
                print(f"Clicked last page link: {page_links[-1].text}")

        if not next_button_found:
            print("No more pages found, scraping finished.")
            break
        page_count += 1
        time.sleep(3)

    min_length = min(len(phone_names), len(phone_price), len(phone_spec))
    phone_names = phone_names[:min_length]
    phone_price = phone_price[:min_length]
    phone_spec = phone_spec[:min_length]

    while len(phone_names) < min_length:
        phone_names.append("N/A")
    while len(phone_price) < min_length:
        phone_price.append("N/A")
    while len(phone_spec) < min_length:
        phone_spec.append("N/A")

    phone_spec = [", ".join(spec.split("\n")) for spec in phone_spec]
    driver.quit()

    return phone_names, phone_price, phone_spec

def save_to_excel(phone_names, phone_price, phone_spec):
    filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    if filename:
        df = pd.DataFrame({
            "Phone Name": phone_names,
            "Phone Price": phone_price,
            "Phone Spec": phone_spec
        })
        df.to_excel(filename, index=False)
        print(f"Data saved to {filename}")

root = tk.Tk()
root.title("Phone Scraper")

search_label = tk.Label(root, text="Enter search query (e.g., 'Samsung 5G Mobile'):")
search_label.pack(padx=10, pady=5)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

start_button = tk.Button(root, text="Start Scraping", command=start_scraping)
start_button.pack(padx=10, pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
progress_bar.pack(padx=10, pady=10)

status_label = tk.Label(root, text="Enter search query and click 'Start Scraping'.")
status_label.pack(padx=10, pady=5)

root.mainloop()
