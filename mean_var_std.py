import numpy as np

List1 = []
i = 0
while i < 9:
    Value =input(f'Enter the value {i+1} for the array:  ')
    List1.append(Value)
    i+= 1
array_original = np.array(List1)
x = array_original.reshape((3,3)).astype(float)
print(x)

def calculate(t):
    #lists can be appended to other lists
    Mean = []
    Variance =[]
    StandardDev =[]
    Max = []
    Min = []
    Sum = []

    #Mean array
    Mean_List1 =  (x.mean(axis = 0)).tolist()
    Mean_List2 =  (x.mean(axis = 1)).tolist()
    Mean_List3 =  ((x.flatten()).mean()).tolist()
    Mean.append(Mean_List1)
    Mean.append(Mean_List2)
    Mean.append(Mean_List3)

    #Variance Array
    Var_List1 =  (x.var(axis = 0)).tolist()
    Var_List2 =  (x.var(axis = 1)).tolist()
    Var_List3 =  ((x.flatten()).var()).tolist()
    Variance.append(Var_List1)
    Variance.append(Var_List2)
    Variance.append(Var_List3)

    #Std Array
    SD_List1 =  (x.std(axis = 0)).tolist()
    SD_List2 =  (x.std(axis = 1)).tolist()
    SD_List3 =  ((x.flatten()).std()).tolist()
    StandardDev.append(SD_List1)
    StandardDev.append(SD_List2)
    StandardDev.append(SD_List3)

    #Max List
    Max_List1 =  (x.max(axis = 0)).tolist()
    Max_List2 =  (x.max(axis = 1)).tolist()
    Max_List3 =  ((x.flatten()).max()).tolist()
    Max.append(Max_List1)
    Max.append(Max_List2)
    Max.append(Max_List3)

    #Min List
    Min_List1 =  (x.min(axis = 0)).tolist()
    Min_List2 =  (x.min(axis = 1)).tolist()
    Min_List3 =  ((x.flatten()).min()).tolist()
    Min.append(Min_List1)
    Min.append(Min_List2)
    Min.append(Min_List3)

    #Sum List
    Sum_List1 =  (x.sum(axis = 0)).tolist()
    Sum_List2 =  (x.sum(axis = 1)).tolist()
    Sum_List3 =  ((x.flatten()).sum()).tolist()
    Sum.append(Sum_List1)
    Sum.append(Sum_List2)
    Sum.append(Sum_List3)


    Analysis = {
        'mean': Mean,
        'Variance': Variance,
        'Standard Deviation': StandardDev,
        'Max': Max,
        'Min': Min,
        'Sum': Sum
        }
    return Analysis

print(calculate(x))




