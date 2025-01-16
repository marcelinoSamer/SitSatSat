import os
import matplotlib.pyplot as plt
import QUBO_Converter
from collections import Counter

def get_solutions(filename):
    solved=[]
    with open(filename, 'r') as file:
        for line in file:
            if "satisfies" in line:
                # Extract the number after "satisfies"
                n = line.split("satisfies", 1)[1].strip().split(" ", 1)[0]
                solved.append(int(n))
        return solved

def get_max(values):
    max =0
    solution_index=0
    for i in range(len(values)):
        if(values[i]>max):
            max=values[i]
            solution_index=i
    return max,solution_index
def max_solutions(file_path):
    max_list=[]
    for path in os.listdir(file_path):
        max_list.append(get_max(get_solutions(os.path.join(file_path,path))))
    return max_list
def get_average(list):
    sum=0
    for item in list:
        sum+=item
    return sum/len(list)
def plot_distinct_solutions(file_path):
    # Get max solutions for each file
    max_list = max_solutions(file_path)

    # Count occurrences of each distinct value
    solution_counts = {}
    for solution in max_list:
        solution_counts[solution] = solution_counts.get(solution, 0) + 1

    distinct_solutions = list(solution_counts.keys())
    counts = list(solution_counts.values())

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(distinct_solutions, counts, color='skyblue', edgecolor='black')
    plt.xlabel('Distinct Solutions', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.title('Distribution of Distinct Solutions', fontsize=14)
    plt.xticks(distinct_solutions)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plot_k_most_repeated_solutions_binary(solutions, k, test_path, result_path):
    # Count the occurrences of each solution
    solution_counts = Counter(tuple(sample.items()) for sample in solutions)

    # Find the k most repeated solutions
    most_common_solutions = solution_counts.most_common(k)

    # Convert the most common solutions back to dictionaries for readability
    most_common_solutions_dicts = [
        (dict(solution), count) for solution, count in most_common_solutions
    ]

    # Print the k most repeated solutions
    with open(result_path,"a") as file:
        file.write(f"Top {k} Most Repeated Solutions:")
        for rank, (solution_dict, count) in enumerate(most_common_solutions_dicts, start=1):
            file.write(f"{rank}. Solution: {str(solution_dict)}, Occurrences: {count}, Satisfies: {QUBO_Converter.clauses_Satisfied(solution_dict, test_path)}\n".replace("np.int8(", "").replace(")", ""))

    return most_common_solutions_dicts

def plot_satisfaction_graph(result_path):             
    assignments= get_solutions(result_path)
    satisfied_counts = {}
    for solution in assignments:
        satisfied_counts[solution] = satisfied_counts.get(solution, 0) + 1
    # Prepare data for plotting
    distinct_solutions = list(satisfied_counts.keys())
    counts = list(satisfied_counts.values())
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(distinct_solutions, counts, color='skyblue', edgecolor='black')
    plt.xlabel('Satisfied Clauses', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.title('Distribution of Clause Satisfaction', fontsize=14)
    plt.xticks(distinct_solutions)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plot_energy(energies):
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(energies)), [energy[0] for energy in energies])  # Extract energy values from the list of tuples
    plt.xlabel('Solution Index')
    plt.ylabel('Energy')
    plt.title('Energy of Each Solution')
    plt.show()

def max_solvable(result_file):
    solved=get_solutions(result_file)
    max_solved,solution_index=get_max(solved)
    print("Maximums Closes Solved:", max_solved)
    return solution_index