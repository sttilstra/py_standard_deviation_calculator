import math

# this function calculates the standard deviation based on a population
def pop_dev():
    mean = sum(sample) / len(sample)
    sample_sub_mean = []

    for num in sample:
        num = num - mean
        numsq = num ** 2
        sample_sub_mean.append(numsq)

    mean2 = sum(sample_sub_mean) / len(sample_sub_mean)
    meansqrt = round(math.sqrt(mean2), 4)
    return meansqrt

# this function calculates the standard deviation based on a sample
def sample_dev():
    mean = sum(sample) / len(sample)
    sample_sub_mean = []

    for num in sample:
        num = num - mean
        numsq = num ** 2
        sample_sub_mean.append(numsq)

    mean2 = sum(sample_sub_mean) / (len(sample_sub_mean) - 1)
    meansqrt = round(math.sqrt(mean2), 4)
    return meansqrt


sample = []
more_numbers = True

while more_numbers:
    user_num = input("Please enter a number: ")
    sample.append(float(user_num))
    another_number = input("Do you wish to enter another number? Type Y or N.")
    if another_number.upper() == "N":
        more_numbers = False

sample_or_pop = input("Are these numbers part of a sample or population? \nEnter S for sample or P for population:")

if sample_or_pop.upper() == "S":
    print(f"The standard deviation is {sample_dev()}")
else:
    print(f"The standard deviation is {pop_dev()}")
