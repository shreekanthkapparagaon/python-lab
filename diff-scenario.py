from sympy import symbols
from sympy.logic.boolalg import And,Or,Implies
from sympy.logic.inference import satisfiable
# Define predicates
Attendance = symbols('Attendance')
# Student has minimum required attendance
Assignments = symbols('Assignments') # Student has submitted all assignments
Eligible = symbols('Eligible')#Student is eligible for the final exam
# Define knowledge rules using predicate logic
#
rule1 = Implies(Attendance, Eligible) # If student has attendance, they may be eligible
rule2 = Implies(Assignments, Eligible) # If student submitted assignments, they may be eligible
rule3 = Implies(And(~Attendance, ~Assignments), ~Eligible) # If both are met, definitely eligible
# Takeinput from the student
att = input("Did you meet the minimum attendance requirement? (yes/no): ").strip().lower()
assign = input("Did you submit all required assignments? (yes/no): ").strip().lower()
# Convert input to Boolean values
attendance_status = True if att == "yes" else False
assignment_status = True if assign == "yes" else False
# Evaluate scenario based on user input
scenario = And(
Attendance if attendance_status else ~Attendance,
    Assignments if assignment_status else ~Assignments,
    rule1,
    rule2,
    rule3
)
result = satisfiable(scenario)
#Print the result
if result[Eligible]:
    print("\n You are eligible for the final exam!")
else:
    print("\n You are NOT eligible for the final exam.")