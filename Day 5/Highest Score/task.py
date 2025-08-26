student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#using sum()
total_exam_score = sum(student_scores)
print(f"tota is: {total_exam_score}")


#using a for loop
sum = 0
for score in student_scores:
    sum += score
print(f"total using for loop: {sum}")


#use max()
max_score = max(student_scores)
print(f"max score: {max_score}")

#max using a for loop
max_score_with_for_loop = 0
for score in student_scores:
    if score > max_score_with_for_loop:
        max_score_with_for_loop = score

print(f"max score using for loop: {max_score_with_for_loop}")