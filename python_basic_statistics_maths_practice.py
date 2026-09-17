# Python Basic Maths & Statistics Practice
# Beginner-friendly Jupyter / Python practice file
# You can run this file cell-by-cell in Jupyter Notebook or VS Code.

import math
import statistics

print("=" * 60)
print("PYTHON BASIC MATHS & STATISTICS PRACTICE")
print("=" * 60)

# ============================================================
# 1. PYTHON BASIC ARITHMETIC
# ============================================================

a = 10
b = 3

print("\n1. Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)


# ============================================================
# 2. BASIC MATH FUNCTIONS
# ============================================================

print("\n2. Math Functions")

print("Square root of 25:", math.sqrt(25))
print("2 raised to power 5:", math.pow(2, 5))
print("Factorial of 5:", math.factorial(5))
print("Ceiling of 4.2:", math.ceil(4.2))
print("Floor of 4.8:", math.floor(4.8))
print("Absolute value:", abs(-25))
print("Round:", round(4.5678, 2))


# ============================================================
# 3. SUM, COUNT, MINIMUM, MAXIMUM
# ============================================================

data = [10, 20, 30, 40, 50]

print("\n3. Basic Data Operations")
print("Data:", data)
print("Sum:", sum(data))
print("Count:", len(data))
print("Minimum:", min(data))
print("Maximum:", max(data))
print("Range:", max(data) - min(data))


# ============================================================
# 4. MEAN
# ============================================================

mean = sum(data) / len(data)

print("\n4. Mean")
print("Mean:", mean)


# ============================================================
# 5. MEDIAN
# ============================================================

print("\n5. Median")
print("Median:", statistics.median(data))


# ============================================================
# 6. MODE
# ============================================================

mode_data = [10, 20, 20, 30, 40, 20, 50]

print("\n6. Mode")
print("Data:", mode_data)
print("Mode:", statistics.mode(mode_data))


# ============================================================
# 7. VARIANCE
# ============================================================

print("\n7. Variance")
print("Population Variance:", statistics.pvariance(data))
print("Sample Variance:", statistics.variance(data))


# ============================================================
# 8. STANDARD DEVIATION
# ============================================================

print("\n8. Standard Deviation")
print("Population SD:", statistics.pstdev(data))
print("Sample SD:", statistics.stdev(data))


# ============================================================
# 9. PERCENTAGE
# ============================================================

obtained = 420
total = 500

percentage = (obtained / total) * 100

print("\n9. Percentage")
print("Obtained:", obtained)
print("Total:", total)
print("Percentage:", percentage, "%")


# ============================================================
# 10. STUDENT MARKS STATISTICS
# ============================================================

marks = [75, 80, 85, 90, 70]

print("\n10. Student Marks")
print("Marks:", marks)
print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
print("Minimum:", min(marks))
print("Maximum:", max(marks))
print("Range:", max(marks) - min(marks))
print("Population Variance:", statistics.pvariance(marks))
print("Population SD:", statistics.pstdev(marks))


# ============================================================
# 11. PROBABILITY
# ============================================================

favorable = 3
total_outcomes = 6

probability = favorable / total_outcomes

print("\n11. Probability")
print("Probability:", probability)
print("Probability Percentage:", probability * 100, "%")


# ============================================================
# 12. Z-SCORE
# Formula: z = (x - mean) / standard_deviation
# ============================================================

x = 80
mean_value = 70
sd_value = 5

z_score = (x - mean_value) / sd_value

print("\n12. Z-Score")
print("Z-Score:", z_score)


# ============================================================
# 13. PERCENTILE / QUARTILE USING NUMPY
# ============================================================

# Uncomment these lines if NumPy is installed.
#
# import numpy as np
#
# numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
#
# print("\n13. NumPy Statistics")
# print("25th Percentile:", np.percentile(numbers, 25))
# print("50th Percentile:", np.percentile(numbers, 50))
# print("75th Percentile:", np.percentile(numbers, 75))
# print("Mean:", np.mean(numbers))
# print("Median:", np.median(numbers))
# print("Variance:", np.var(numbers))
# print("Standard Deviation:", np.std(numbers))


# ============================================================
# PRACTICE QUESTIONS
# Try solving these BEFORE looking at the solutions.
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE QUESTIONS")
print("=" * 60)

print("""
Q1. Find the sum of [10, 20, 30, 40, 50].

Q2. Find the average of [5, 10, 15, 20, 25].

Q3. Find the maximum and minimum of [12, 45, 7, 32, 18].

Q4. Find the range of [20, 45, 10, 35, 50].

Q5. Find the median of [10, 20, 30, 40, 50].

Q6. Find the median of [10, 20, 30, 40].

Q7. Find the mode of [5, 10, 10, 20, 10, 30, 20].

Q8. Calculate population variance of [2, 4, 6, 8, 10].

Q9. Calculate population standard deviation of [2, 4, 6, 8, 10].

Q10. A student scored [70, 80, 90, 85, 75]. Find the mean.

Q11. Calculate 5^3 using Python.

Q12. Calculate the square root of 144.

Q13. Calculate 7 factorial.

Q14. A student obtained 420 marks out of 500. Find percentage.

Q15. Find the probability of getting an even number on a standard dice.
""")


# ============================================================
# SOLUTIONS
# ============================================================

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# Q1
q1 = [10, 20, 30, 40, 50]
print("\nQ1 Solution:", sum(q1))

# Q2
q2 = [5, 10, 15, 20, 25]
print("Q2 Solution:", sum(q2) / len(q2))

# Q3
q3 = [12, 45, 7, 32, 18]
print("Q3 Maximum:", max(q3))
print("Q3 Minimum:", min(q3))

# Q4
q4 = [20, 45, 10, 35, 50]
print("Q4 Range:", max(q4) - min(q4))

# Q5
q5 = [10, 20, 30, 40, 50]
print("Q5 Median:", statistics.median(q5))

# Q6
q6 = [10, 20, 30, 40]
print("Q6 Median:", statistics.median(q6))

# Q7
q7 = [5, 10, 10, 20, 10, 30, 20]
print("Q7 Mode:", statistics.mode(q7))

# Q8
q8 = [2, 4, 6, 8, 10]
print("Q8 Population Variance:", statistics.pvariance(q8))

# Q9
print("Q9 Population SD:", statistics.pstdev(q8))

# Q10
q10 = [70, 80, 90, 85, 75]
print("Q10 Mean:", statistics.mean(q10))

# Q11
print("Q11 5^3:", 5 ** 3)

# Q12
print("Q12 Square Root:", math.sqrt(144))

# Q13
print("Q13 7!:", math.factorial(7))

# Q14
print("Q14 Percentage:", (420 / 500) * 100, "%")

# Q15
print("Q15 Probability:", 3 / 6)
print("Q15 Percentage:", (3 / 6) * 100, "%")


# ============================================================
# EXTRA PRACTICE - WITHOUT SOLUTIONS
# ============================================================

print("\n" + "=" * 60)
print("EXTRA PRACTICE - TRY YOURSELF")
print("=" * 60)

print("""
1. Find mean, median and mode of:
   [12, 15, 15, 18, 20, 15, 25]

2. Find variance and standard deviation of:
   [5, 10, 15, 20, 25]

3. A student has marks:
   Maths = 85
   Python = 90
   DBMS = 75
   ML = 80
   Find total, average and percentage.

4. Find the range of:
   [100, 45, 67, 23, 89, 12]

5. Find the square, cube and square root of 64.

6. Calculate:
   15 + 20 * 3

7. Calculate:
   (15 + 20) * 3

8. A shop gives 20% discount on a product costing 1500.
   Find discount amount and final price.

9. A dice is thrown once.
   Find the probability of:
   a) getting 1
   b) getting an even number
   c) getting a number greater than 4

10. Create a Python program that accepts 5 numbers
    from the user and calculates:
    - Mean
    - Median
    - Minimum
    - Maximum
    - Range
""")


print("\nPractice complete! Keep solving the extra questions.")
