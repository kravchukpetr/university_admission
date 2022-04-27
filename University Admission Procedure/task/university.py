import statistics

def print_result(dept_candidate_dict, score_list):
    for department, candidate_list in dept_candidate_dict.items():
        f = open(department + ".txt", "w")
        dept_values = [d[department] for d in dept_list if department in d.keys()][0]
        candidate_list.sort(key=lambda x: (-max(round(statistics.mean([x[1][score_list.index(dept_values[0])], x[1][score_list.index(dept_values[1])]]), 1), x[1][4]), x[0]))
        for candidate in candidate_list:
            f.write(candidate[0] + ' ' + str(max(round(statistics.mean([candidate[1][score_list.index(dept_values[0])], candidate[1][score_list.index(dept_values[1])]]), 1), candidate[1][4])) + '\n')
        f.close()
        # print()

exam_score = []
candidate_list = []
appl_threshold = int(input('Application threshold: '))
score_list = ['Physics', 'Chemistry', 'Mathematics', 'Engineering']
dept_list = [{'Biotech': ['Chemistry', 'Physics']}, {'Chemistry': ['Chemistry', 'Chemistry']}, {'Engineering': ['Engineering', 'Mathematics']}, {'Mathematics': ['Mathematics', 'Mathematics']}, {'Physics': ['Physics', 'Mathematics']}]
already_select_candidate = []
dept_candidate_dict = {}


with open('applicants.txt', 'r') as f:
    input_txt = f.readlines()
for line in input_txt:
    exam_score.append(line.split())
for candidate in exam_score:
    candidate_list.append([" ".join([candidate[0], candidate[1]]), [float(candidate[2]), float(candidate[3]), float(candidate[4]), float(candidate[5]), float(candidate[6])], [candidate[7], candidate[8], candidate[9]]])
dept_dict = {}
for dept in dept_list:
    check_candidate = []
    for candidate in candidate_list:
        if list(dept.keys())[0] in candidate[2]:
            check_candidate.append(candidate)
    check_candidate.sort(key=lambda x: (-max(round(statistics.mean([x[1][score_list.index(list(dept.values())[0][0])], x[1][score_list.index(list(dept.values())[0][1])]]), 2), x[1][4]), x[0]))
    # print(check_candidate)
    dept_dict[list(dept.keys())[0]] = check_candidate
for department in dept_dict.keys():
    dept_candidate_dict[department] = []
for priority in range(0, 3):
    for department, value in dept_dict.items():
        for i, candidate in enumerate(value, start=1):
            if len(dept_candidate_dict[department]) < appl_threshold:
                if candidate[0] not in already_select_candidate:
                    if department == candidate[2][priority]:
                        already_select_candidate.append(candidate[0])
                        dept_candidate_dict[department].append(candidate)
print_result(dept_candidate_dict, score_list)
