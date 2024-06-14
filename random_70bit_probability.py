import random
import matplotlib.pyplot as plt


def generate_binary_nums(num):
    binary_nums = []
    for i in range(num):
        binary_num = bin(random.randint(0, 2**70-1))[2:].zfill(70)
        binary_nums.append(binary_num)
    return binary_nums


def generate_binary_nums_01(num):
    binary_nums = []
    binary = []
    for i in range(num):
        binary_0 = []
        for j in range(70):
            binary_num = bin(random.randint(0, 1))[2:]
            binary_0.append(binary_num)
        #print(binary_0)
        binary = ''.join(binary_0)
        #print(binary)
        binary_nums.append(binary)
    print(binary_nums)
    return binary_nums


def count_zeros(binary_nums):
    zero_counts = []
    for binary_num in binary_nums:
        zero_count = binary_num.count('0')
        zero_counts.append(zero_count)
    return zero_counts


def main(repeat_times, percentage):
    zero_counts_list = []
    total_runs = repeat_times

    for _ in range(total_runs):
        # binary_nums = generate_binary_nums(70)
        binary_nums = generate_binary_nums_01(70)
        zero_counts = count_zeros(binary_nums)
        zero_counts_list.extend(zero_counts)

    counts_dict = {i: zero_counts_list.count(i) for i in range(70)}
    total_counts = sum(counts_dict.values())
    print(total_counts)
    percentage_dict = {k: v/total_counts for k, v in counts_dict.items()}
    # print(percentage_dict)
    # print(percentage_dict.values())
    values_list = list(percentage_dict.values())
    for i in range(70):
        print("0的个数：%s,占比：%f" % (i, 1-sum(values_list[i:])))

    plt.bar(percentage_dict.keys(), percentage_dict.values())
    plt.xlabel('Number of Zeros')
    plt.ylabel('Frequency')
    plt.title('Frequency of Zeros in 7000 Runs')
    plt.show()

    #num_zeros = int(70 * percentage / 100)
    #print(f"Number of Zeros: {num_zeros}")


if __name__ == "__main__":
    repeat_times = 1000
    percentage = 90
    main(repeat_times, percentage)