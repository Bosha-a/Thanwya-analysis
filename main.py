import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

def get_result(sitting_number):
    url = f'https://shbabbek.com/natega/{sitting_number}'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        
        name_element = soup.find('span', text='الأسم:')
        result = {
            'رقم الجلوس': sitting_number,
            'الاسم': name_element.find_next_sibling('span').get_text(strip=True) if name_element else 'غير متوفر',
            'المدرسة': soup.find('span', text='المدرسة :').find_next_sibling('span').get_text(strip=True) if soup.find('span', text='المدرسة :') else 'غير متوفر',
            'الأدارة التعليمية': soup.find('span', text='الأدارة التعليمية :').find_next_sibling('span').get_text(strip=True) if soup.find('span', text='الأدارة التعليمية :') else 'غير متوفر',
            'حالة الطالب': soup.find('span', text='حالة الطالب :').find_next_sibling('span').get_text(strip=True) if soup.find('span', text='حالة الطالب :') else 'غير متوفر',
            'الشعبة': soup.find('span', text='الشعبة :').find_next_sibling('span').get_text(strip=True) if soup.find('span', text='الشعبة :') else 'غير متوفر',
            'اللغة العربية': soup.find('span', text='اللغة العربية :').find_next_sibling('span').get_text(strip=True) if soup.find('span', text='اللغة العربية :') else 'غير متوفر',
            'اللغة الأجنبية الأولى': soup.find('span', text='اللغة الأجنبية الأولى :').find_next_sibling('span').get_text(strip=True) if soup.find('span', text='اللغة الأجنبية الأولى :') else 'غير متوفر',
            'اللغة الأجنبية الثانية': soup.find('span', text='اللغة الأجنبية الثانية :').find_next_sibling('span').get_text(strip=True) if soup.find('span', text='اللغة الأجنبية الثانية :') else 'غير متوفر',
            'مجموع الرياضيات البحتة': soup.find('span', text='مجموع الرياضيات البحتة :').find_next_sibling('span').get_text(strip=True) if soup.find('span', text='مجموع الرياضيات البحتة :') else 'غير متوفر',
            'الكيمياء': soup.find('span', text='الكيمياء :').find_next_sibling('span').get_text(strip=True) if soup.find('span', text='الكيمياء :') else 'غير متوفر',
            'الفيزياء': soup.find('span', text='الفيزياء :').find_next_sibling('span').get_text(strip=True) if soup.find('span', text='الفيزياء :') else 'غير متوفر',
            'مجموع الدرجات': soup.find('span', text='مجموع الدرجات :').find_next_sibling('span').get_text(strip=True) if soup.find('span', text='مجموع الدرجات :') else 'غير متوفر'
        }
        return result
    except requests.RequestException as e:
        return {
            'رقم الجلوس': sitting_number,
            'الاسم': 'خطأ في الطلب',
            'المدرسة': 'خطأ في الطلب',
            'الأدارة التعليمية': 'خطأ في الطلب',
            'حالة الطالب': 'خطأ في الطلب',
            'الشعبة': 'خطأ في الطلب',
            'اللغة العربية': 'خطأ في الطلب',
            'اللغة الأجنبية الأولى': 'خطأ في الطلب',
            'اللغة الأجنبية الثانية': 'خطأ في الطلب',
            'مجموع الرياضيات البحتة': 'خطأ في الطلب',
            'الكيمياء': 'خطأ في الطلب',
            'الفيزياء': 'خطأ في الطلب',
            'مجموع الدرجات': 'خطأ في الطلب'
        }

random.seed(42)  
starting_number = 0
num_results = 30
sitting_numbers = [starting_number + random.randint(809300, 809450) for _ in range(809300, 809450)]


results = []

counter = 0 
for number in sitting_numbers:
    print(f'{counter }جلب نتائج رقم الجلوس: {number}')
    result = get_result(number)
    if result['الاسم'] != 'غير متوفر':
        results.append(result)
    counter +=1

    
    time.sleep(1)


df = pd.DataFrame(results)
df.to_csv('results.csv', index=False, encoding='utf-8-sig')
# with open("results.csv", "a",encoding='utf-8-sig' ,newline="") as file:


# print('results.csv')