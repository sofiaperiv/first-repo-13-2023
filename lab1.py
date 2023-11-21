import requests
url = "https://student2023.lpnu.ua/students_schedule?studygroup_abbrname=%D1%96%D1%80-13&semestr=1&semestrduration=1"
response = requests.get(url)
print(response.text)
