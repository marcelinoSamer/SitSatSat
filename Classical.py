import glob
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

def create_3sat_ilp_model(clauses, num_variables):
    problem = LpProblem("3SAT_ILP", LpMaximize)
    x = {i: LpVariable(f"x_{i}", cat="Binary") for i in range(1, num_variables + 1)}
    y = {i: LpVariable(f"y_{i}", cat="Binary") for i in range(len(clauses))}
    problem += lpSum(y.values()), "Maximize satisfied clauses"
    for i, clause in enumerate(clauses):
        literals = []
        for literal in clause:
            if literal > 0:
                literals.append(x[literal])
            else:
                literals.append(1 - x[-literal])
        problem += y[i] <= lpSum(literals), f"Clause_{i}_satisfaction"
    return problem

def maxInput(clauses):
    max_var = 0
    for clause in clauses:
        for literal in clause:
            max_var = max(max_var, abs(literal))
    return max_var

def parse_cnf_string(cnf_string):
    clauses = []
    lines = cnf_string.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('c') or line.startswith('p') or line.startswith('%') or line.startswith('0'):
            continue
        if line:
            clause = list(map(int, line.split()))[:-1]
            clauses.append(clause)
    return clauses

def run_test_cases(test_cases_files):
    results = []
    solver = PULP_CBC_CMD(msg=False)  # Create solver object with message turned off
    for i, test_case_file in enumerate(test_cases_files):
        with open(test_case_file, 'r', encoding='utf-8') as file:
            cnf_string = file.read()
        print(f"Running Test Case {i + 1} - {test_case_file}")
        clauses = parse_cnf_string(cnf_string)
        num_clauses = len(clauses)
        nOfVariables = maxInput(clauses)
        problem = create_3sat_ilp_model(clauses, nOfVariables)
        problem.solve(solver)  # Use solver object

        truth_values = [0] * (nOfVariables + 1)
        for var in problem.variables():
            if var.name.startswith('x_'):
                idx = int(var.name.split('_')[1])
                truth_values[idx] = int(var.varValue)

        clause_satisfiability = [int(var.varValue) for var in problem.variables() if var.name.startswith('y_')]

        result = {
            "num_clauses": num_clauses,
            "max_satisfied_clauses": problem.objective.value(),
            "truth_values": truth_values[1:],  # Ignore the first element (index 0) as variables are 1-based
            "clause_satisfiability": clause_satisfiability,
            "is_satisfiable": problem.objective.value() == num_clauses,
            "index": i + 1,  # Adding index of the test case
            "file_name": test_case_file  # Adding file name of the test case
        }
        results.append(result)
    return results

def print_results(results):
    total_cases = len(results)
    satisfied_cases = sum(result['is_satisfiable'] for result in results)
    unsatisfied_cases = total_cases - satisfied_cases
    unsatisfied_indices = [result['index'] for result in results if not result['is_satisfiable']]
    unsatisfied_files = [result['file_name'] for result in results if not result['is_satisfiable']]
    
    print(f"Total test cases: {total_cases}")
    print(f"Total satisfied test cases: {satisfied_cases}")
    print(f"Total unsatisfied test cases: {unsatisfied_cases}")
    if unsatisfied_cases > 0:
        print(f"Indices of unsatisfied test cases: {unsatisfied_indices}")
        print(f"Files of unsatisfied test cases: {unsatisfied_files}")
    
    # Ask user if they want detailed results
    user_input = input("Would you like to see the detailed results of each test case? (yes/no): ").strip().lower()
    if user_input == "yes":
        for i, result in enumerate(results):
            print(f"Results for Test Case {result['index']} - {result['file_name']}")
            print(f"Number of clauses: {result['num_clauses']}")
            print(f"Max number of satisfied clauses: {result['max_satisfied_clauses']}")
            if result['is_satisfiable']:
                print("This formula is satisfiable.")
            else:
                print("This formula is not satisfiable.")
            print(f"Truth values of variables: {result['truth_values']}")
            print(f"Satisfiability of each clause: {result['clause_satisfiability']}\n")

# List of test case files in the folder
test_cases_files = glob.glob('test_cases/*.cnf')  # Adjust the folder path and file extension if needed

# Run the test cases
results = run_test_cases(test_cases_files)

# Print the results
print_results(results)