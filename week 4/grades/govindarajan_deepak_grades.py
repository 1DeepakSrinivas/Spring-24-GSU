grades=[ 83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]
day_1_att={'Mary', 'Jake', 'Sam', 'Alex', 'Percy', 'Jessica', 'Trent', 'Mahmoud'} 
day_2_att={ 'Jake', 'Sam', 'Alex', 'Percy', 'Mahmoud', 'Trent', 'Caleb', 'Zayne'}

def grade():
    global grades
    global day_1_att
    global day_2_att
    test_takers=len(grades)
    max_grade=max(grades)
    min_grade=min(grades)
    grade_avg=sum(grades)/len(grades)
    print(f'{test_takers} students took the exam.')
    print(f'The highest grade was {max_grade}')
    print(f'The lowest grade was {min_grade}')
    print(f'The average grade for the exam was {grade_avg:.1f}')
    total_students=(day_1_att.union(day_2_att))
    print(f'{len(total_students)} students attended the class. ')
    print(f'{(day_1_att.intersection(day_2_att))} attended both days.')
    print(f'{(day_1_att.difference(day_2_att))} attended one class day')

grade()





   
