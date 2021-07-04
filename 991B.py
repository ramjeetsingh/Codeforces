n = int(input())
grades = list(map(int,input().split(" ")))

total_req = n*(4.5)
total_present = sum(grades)

redo = 0
while total_present < total_req:
	lowest_grade = min(grades)
	total_present += (5 - lowest_grade)
	grades.remove(lowest_grade)
	redo += 1

print(redo)