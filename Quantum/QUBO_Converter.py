import dimod
import numpy as np
def get_Number_of_Variables(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('c'):
                # Skip comment lines (starting with 'c') and the problem line (starting with 'p')
                continue
            if line.startswith('p'):
                n = line.split("cnf", 1)[1].strip().split(" ", 1)[0]
                m = line.split("cnf", 1)[1].strip().split(" ", 1)[1]
                return int(n),int(m)


def fullApproxMethod(QUBO, clause):
    i=clause[0]-1
    j=clause[1]-1
    k=clause[2]-1
    negated=[]
    non_negated=[]
    for literal in clause:
        if (literal<0):
            negated.append(-1*literal)
        else:
            non_negated.append(literal)
            
    if(len(negated)==0):
        for literal in clause:
            QUBO[(literal-1,literal-1)]+=-1
        QUBO[(min(i,k),max(i,k))]+=1
        QUBO[(min(j,k),max(j,k))]+=1
        QUBO[(min(i,j),max(i,j))]+=1

    if(len(negated)==1):
        for literal in non_negated:
            QUBO[(min(literal-1,negated[0]-1),max(literal-1,negated[0]-1))]+=-1
        QUBO[(negated[0]-1,negated[0]-1)]+=1
        QUBO[(min(non_negated[0]-1,non_negated[1]-1),max(non_negated[0]-1,non_negated[1]-1))]+=1

    if(len(negated)==2):
        fullApproxMethod(QUBO,[-1*non_negated[0],negated[0],negated[1]])

    if(len(negated)==3):
        fullApproxMethod(QUBO,negated)
def chancellorMethod(QUBO, clause,clause_count,variable_count):
    extra_var=clause_count+variable_count-1
    negated=[]
    non_negated=[]
    for i in range(3):
        if (clause[i]<0):
            negated.append(-1*clause[i])
            clause[i]=clause[i]*-1
        else:
            non_negated.append(clause[i])
    i=clause[0]-1
    j=clause[1]-1
    k=clause[2]-1            
    if(len(negated)==0):
        for literal in clause:
            QUBO[(literal-1,literal-1)]+=-2
            QUBO[(literal-1,extra_var)]+=1
        QUBO[(min(i,k),max(i,k))]+=1
        QUBO[(min(j,k),max(j,k))]+=1
        QUBO[(min(i,j),max(i,j))]+=1
        QUBO[(extra_var,extra_var)]+=-2

    if(len(negated)==1):
        for literal in non_negated:
            QUBO[(literal-1,extra_var)]+=1
            QUBO[(literal-1,literal-1)]+=-1
        QUBO[(extra_var,extra_var)]+=-1
        QUBO[(min(non_negated[0]-1,non_negated[1]-1),max(non_negated[0]-1,non_negated[1]-1))]+=1

    if(len(negated)==2):
        for literal in clause:
            QUBO[(literal-1,literal-1)]+=-1
            QUBO[(literal-1,extra_var)]+=1
        QUBO[(extra_var,extra_var)]+=2
        QUBO[(min(negated[0]-1,negated[1]-1),max(negated[0]-1,negated[1]-1))]+=1
    if(len(negated)==3):
        for literal in clause:
            QUBO[(literal-1,literal-1)]+=-1
            QUBO[(literal-1,extra_var)]+=1
        QUBO[(min(i,k),max(i,k))]+=1
        QUBO[(min(j,k),max(j,k))]+=1
        QUBO[(min(i,j),max(i,j))]+=1
        QUBO[(extra_var,extra_var)]+=-1

  
def print_upper_triangular_from_dict(matrix_dict,n):
    print("Upper Triangular Matrix:")
    
    # Loop over rows
    for i in range(n):
        for j in range(n):
            if j >= i:  # Print only upper triangular elements
                value = matrix_dict.get((i, j), 0)  # Get value or default to 0
                print(f"{value:>4}", end=" ")  # Proper alignment
            else:
                print("    ", end=" ")  # Blank space for lower triangle
        print()  # Newline for the next row



def parse_cnf_file(file_path):
    clauses = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('c') or line.startswith('p') or line.startswith('%') or line.startswith('0'):
                # Skip comment lines (starting with 'c') and the problem line (starting with 'p')
                continue
            if line:
                # Convert the clause to integers and remove the trailing "0"
                clause = list(map(int, line.split()))[:-1]
                clauses.append(clause)

    return clauses
def solve_Clause(assignment,clause):
    if(assignment[abs(clause[0])-1] or assignment[abs(clause[1])-1] or assignment[abs(clause[2])-1]):
        return 1
    return 0

def FullApprox(n,file_path):
    QUBO = {(i,j):0 for i in range(n) for j in range(i,n)}    
    for clause in parse_cnf_file(file_path):
        fullApproxMethod(QUBO,clause)
    return QUBO

def Chancellor(n,m,file_path):
    QUBO = {(i,j):0 for i in range(n+m) for j in range(i,n+m)}                
    for clause in parse_cnf_file(file_path):
        chancellorMethod(QUBO,clause,n,m)
    return QUBO

def clauses_Satisfied(variable_Assignment,file_path):
    solved =0
    for clause in parse_cnf_file(file_path):
        solved+= solve_Clause(variable_Assignment,clause)
    return solved