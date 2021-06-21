import json
import sys
import webbrowser
import pyautogui
import time
import datetime
import calendar
import os
from map import update_links,pwd
file = open('W:\\projects\\classroom\\data.json','r')
data = file.read()
file.close()
data = json.loads(data)


# Returns day name
def find_day():
    date_and_time = datetime.datetime.now()
    date = str(date_and_time.day) + ' ' + str(date_and_time.month) + ' ' + str(date_and_time.year)
    date = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    day = calendar.day_name[date]
    return day


# Prints time-table
# Edit subjects variable in print_time_table() method.
def print_timetable():
    subjects = {'monday' : ['SE', 'DMDW', 'FE', 'CGALAB'],
                'tuesday' : ['OOADLAB', 'CGA', 'OOAD', 'SE'],
                'wednesday' : ['DMDW', 'FE', 'CGA', 'OOAD','PDC'],
                'thursday' : ['CGA', 'OOAD', 'FE', 'DMDWLAB'],
                'friday' : ['OOAD', 'CGA', 'SE' , 'SEMINAR', 'DMDW'],
                'saturday' : ['SE', 'DMDW', 'FE'],
                'sunday' : ['NO CLASS. SLEEP AGAIN']
              }
    day = find_day().lower()
    time_table = subjects.get(day)
    print('\n\t --->>> AUTOMATING GOOGLE CLASSROOM V 2.0 <<<---')
    print('\n\t\t\tSNO.\tSUBJECT')
    for i, j in enumerate(time_table):
        print(f'\n\t\t\t{i + 1}\t{j}')


# Open the classes
def open_class (url):
    webbrowser.open(url)
    time.sleep(10)
    try:
        x, y = pyautogui.locateCenterOnScreen('video_btn.png', grayscale=True)
        pyautogui.click(x, y)
        print('Meet link opened "SUCCESSFULLY"')
    except (Exception):
        print('Failed to join as "LINK NOT FOUND".')


# print help menu
def help():
    print('\n\t --->>> AUTOMATING GOOGLE CLASSROOM V 2.0 <<<---')
    print('\n\t COMMAND                    DESCRIPTION')
    print('\n\t class -h                   To display this menu.')
    print('\n\t class -t                   To display time-table.')
    print('\n\t class [subject name]       To join the link.')
    print('\n\t class -u                   To update links.')

# Main function
def main():
    if not os.path.isfile(pwd + '\data.json'):
        update_links()
    subject = sys.argv[1].upper()
    subjects = data.keys()
    if subject in subjects:
        open_class(data[subject])
    elif subject == '-T':
        print_timetable()
    elif subject == '-H' or subject == '--HELP':
        help()
    elif subject == '-U':
        update_links()
    else: 
        print(f'COMMAND NOT FOUND ---> {subject}')
        print('Use "class -h" for help')

if __name__ == '__main__':
    main()

