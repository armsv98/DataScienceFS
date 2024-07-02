# Whitespace Formatting
for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
print("done looping")

# Functions
def double(x):
    return 2 * x
another_double = lambda x: 2 * x

def my_print(message = "default message"):
    print(message)
    return

# Strings
multi_line_strings = """this is the first line
this is the second line
this is the third line"""

first_name = "Amirreza"
last_name = "Moosavi"
print(f"my name is {first_name}. my last name is {last_name}.")

# Exceptions
try:
    print(0/0)
except:
    print("cannot divide by zero.")

# Lists:
interger_list = [1, 2, 3]
heterogenous_list = ["string", 0.1, True]
list_of_lists = [interger_list, heterogenous_list, []]

list_length = len(interger_list)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zero = x[0]
nine = x[-1]
x[0] = -1
first_three = x[:3]
three_to_end = x[3:]
copy_of_x = x[:]
every_third = x[::3]
five_to_three = x[5:2:-1]

print(5 in x)

x = [1, 2, 3]
x.extend([4, 5, 6])
x = x + [7, 8, 9]
x.append(10) # only one item
print(x)
_, y = [1, 2]
print(y)

# Tuples
my_tuple = (1, 2)
try:
    my_tuple[1] = 3
except:
    print("tuples cannot be modified")

def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3)
s, p = sum_and_product(2, 3)
print(sp)
print(s, p)


# Dictionaries:
grades = {"joel" : 80, "Tim": 95}
grades["Ellie"] = 90
joel_grade = grades["joel"]
Tim_has_grade = "Tim" in grades
kate_grade = grades.get("Kate", 0)
print(grades)

grades_keys = grades.keys()
grades_values = grades.values()
grades_items = grades.items()


# deafultdict
document = "an string of documents"
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word in document:
    try:
        word_counts[word] =+ 1
    except KeyError:
        word_counts[word] = 1
        
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1


from collections import defaultdict
word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)
dd_list[2].append(1)

dd_dict = defaultdict(dict)
dd_dict["joel"]["city"] = "Seattle"


# Counters
from collections import Counter
c = Counter([0, 0, 1, 2])

word_counts = Counter(document)


# Sets
prime_below_10 = {2, 3, 5, 7}


# Sorting
x = [4, 1, 3, 2]
y = sorted(x)
z = sorted(x, reverse= True)
x.sort()

# OOP
class CountingClicker:
    def __init__(self, count = 0):
        self.count = count
    
    def __repr__(self):
        return f"CountingClicker(count = {self.count})"
    
    def click(self, num_times = 1):
        self.count += num_times
    
    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0
    

clicker = CountingClicker()
assert clicker.read() == 0
clicker.click()
clicker.click()
assert clicker.read() == 2
clicker.reset()
assert clicker.read() == 0

class NoResetClicker(CountingClicker):
    def reset(self):
        pass

# Randomness
import random
random.seed(10)
random_number = random.random
random.randrange(3, 10)
up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.choice(up_to_ten)
random.shuffle(up_to_ten)

# Zip and Argument Unpacking
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 4]
pairs = []
for pair in zip(list1, list2):
    pairs.append(pair)
letters, numbers = zip(*pairs)


def add(a, b):
    return a + b

try:
    add([2, 5])
except TypeError:
    add(*[2,5])


# Args and Kwargs
def process_student(name, grade, *courses, **extracurriculars):
    print(f"Student: {name} - Grade: {grade}")
  
    if courses:
        print(f"Courses: {', '.join(courses)}")  # Join courses with commas
    
    if extracurriculars:
        print("Extracurricular Activities:")
        for activity, details in extracurriculars.items():
            print(f"- {activity}: {details}")

process_student("Alice", 12, "Math", "Science", "English", music="Band (Clarinet)")


# Type Annotations
from typing import List, Dict, Tuple, Optional
def total(xs: List[int]) -> float:
    return sum(xs)

total([2, 2, 4.5])

values: List[int] = [2, 5, 14]
counts: Dict[str, int] = {"data" : 1, "sciene" : 2}
triple: Tuple[int, float, int] = (1, 4.5, 6)
