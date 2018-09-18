import sys

schools = list()
subjects = list()
schools_students = dict()
school_student_count = dict()
subject_student_count = dict()
school_popular_subject = dict()
with open(sys.argv[1], 'r') as file:
    file.readline()
    for line in file:
        line = line.rstrip('\n').split(",")
        schools.append(line[1])
        subjects.append(line[2])
        key = line[1] + "-" + line[0]
        schools_students[key] = schools_students.get(key, 0) + 1
        school_student_count[line[1]] = school_student_count.get(line[1], 0) + 1
        subject_student_count[line[2]] = subject_student_count.get(line[2], 0) + 1
        sub = line[1] + "-" + line[2]
        school_popular_subject[sub] = school_popular_subject.get(sub, 0) + 1
print("\nDifferent Schools Count: ", len(set(schools)))
print("\n\nMost Frequently Studied Subject: ", max(subjects,key=subjects.count))
print("\n\nSchools with 2 students with same name: ", list(schools_students.keys())[list(schools_students.values()).index(2)])
print("\n\nSchools with count of students : ", school_student_count)
print("\n\nSubjects with count of students : ", subject_student_count)
print("\n\nSchools with Popular Subjects : ", list(school_popular_subject.keys()))
