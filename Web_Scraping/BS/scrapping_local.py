from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    content = html_file.read()

soup = BeautifulSoup(content, "lxml")

# get heading tags
# find(): searches for the 1st element and stops

course_cards = soup.find_all(
    "div", class_="card"
)  # class is a keyword in python so add underscore

for course in course_cards:
    course_name = course.h5.text
    course_price = course.a.text.split(" ")[-1]

    print(f"{course_name} costs {course_price}")
