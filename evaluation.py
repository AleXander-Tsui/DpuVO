def file_to_list(filename):
    with open(filename, 'r') as f:
        line = f.read().strip().split()
        res = [float(a) for a in line]
    return res

sim_res = file_to_list('simulation_result.txt')
dpu_res = file_to_list('result_CHW.txt')
# eval
correct = 0
L1 = L2 = 0
max_diff = abs(dpu_res[0] - sim_res[0])

for i in range(len(sim_res)):
    if sim_res[i] == dpu_res[i]:
        correct += 1
    if abs(dpu_res[i] - sim_res[i]) > max_diff:
        max_diff = abs(dpu_res[i] - sim_res[i])
    L1 += abs(dpu_res[i] - sim_res[i])
    L2 += (dpu_res[i] - sim_res[i])*(dpu_res[i] - sim_res[i])

print("Accuracy: ", correct/len(sim_res))
print("L1: ", L1)
print("L2: ", L2)
print("Maximum difference: ", max_diff)