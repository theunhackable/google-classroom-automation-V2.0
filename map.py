import getlinks
import json

        #   Course Name : Alias
        #   Edit course_alias variable
course_alias = {'CGA Lab - III- S2': 'CGALAB',
                'CGA - III   - S2': 'CGA',
                'OOAD - S2': 'OOAD',
                'DMDW Lab - S2': 'DMDWLAB',
                'DMDW - S2': 'DMDW',
                'SE - S2': 'SE',
                'III IT Seminar - S2':'SEMINAR',
                'FE - MATLAB - S2': 'FE',
                'III B Tech IT - PDC- S2': 'PDC'
               }


def get_classes():
    courses = getlinks.main() 
    
    if courses == {}:
        return None
    
    data = {}
    
    for course in courses:
        if course not in course_alias:
            continue
        data[course_alias[course]] = courses[course]
    return data


def update_links():
    data = get_classes()
    
    if data is None:
        pass
    else:
        with open( getlinks.pwd + 'data.json', 'w') as file:
            file.write(json.dumps(data))
        print('\n\t\t Links updated')