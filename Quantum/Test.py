import dimod
import os
import QUBO_Converter
from collections import Counter
import re
import matplotlib.pyplot as plt
import analyze_file
def natural_sort_key(filename):
    # Extract numbers from the filename for natural sorting
    return [int(text) if text.isdigit() else text for text in re.split(r'(\d+)', filename)]

folder_path = "Input_Problems"
directory = "results"

# Sort files using natural sorting
sorted_files = sorted(os.listdir(folder_path), key=natural_sort_key)

for index, path in enumerate(sorted_files):
    os.makedirs(directory,exist_ok=True)
    test_path=os.path.join(folder_path,path)
    print (f"Running testcase No. {index+1}    {test_path}")
    result_path=os.path.join(directory,path)
    
    qubo={}
    n,m=QUBO_Converter.get_Number_of_Variables(test_path)
    print("Which QUBO transformation would you like to use? (FullApprox:0  Chancellor:1)")
    x=input()
    while(x=="0" or x=="1"):
        if x=="0":
            qubo= QUBO_Converter.FullApprox(n,test_path)
            break
        if x=="1":
            qubo= QUBO_Converter.Chancellor(n,m,test_path)
            break
        print("Please enter 0 or 1\n")
        
    #reset the result file
    with open(result_path,"w") as file:
        file.write(path)
        file.write("\n")
    # Initialize the SimulatedAnnealingSampler
    sampler = dimod.reference.samplers.SimulatedAnnealingSampler()
    
    # Sample the QUBO
    response = sampler.sample_qubo(qubo, num_reads=2)

    # Extract the solutions and energies
    solutions = [sample for sample in response.samples()]
    energies = list(response.data(['energy']))  # Convert to list

    # Visualizing the energy of each solution

    analyze_file.plot_energy(energies)

    #track how many times each variable is set to 1 across all solutions
    variable_counts = [0] * n  # We know we have 4 variables in this case

    for sample in solutions:
        for i in qubo.keys():  # Loop through the keys in the QUBO matrix
            if i[0] < n and sample[i[0]] == 1:  # Only consider original variables (indices < n)
                variable_counts[i[0]] += 1


    analyze_file.plot_k_most_repeated_solutions_binary(solutions,5, test_path, result_path)

    # Output the results
    with open(result_path, "a") as file:
        file.write("Solutions found:\n")
        for sample in solutions:
            file.write(str(sample))
            file.write(
                f"Objective value (energy): {energies[solutions.index(sample)][0]}   satisfies {QUBO_Converter.clauses_Satisfied(sample, test_path)}\n"
            )       
    analyze_file.plot_satisfaction_graph(result_path)
