# shell sort, aka 'interleaved insertion algorithm', similar to insertion sort.
def insertion_sort_interleaved(num_list, start_i, gap):

    for i in range(start_i + gap, len(num_list), gap):
        insert_index = i
        swap = 0  # notes how many times values were spwapped
        print("    current insert index: ", i)

        while ((insert_index - gap >= start_i) and (num_list[insert_index] < num_list[insert_index-gap])):
            temp1 = num_list[insert_index]
            temp2 = num_list[insert_index - gap]

            print("swapping {value_1} and {value_2}".format
                  (value_1=temp1, value_2=temp2))

            num_list[insert_index] = temp2
            num_list[insert_index-gap] = temp1

            insert_index = insert_index - gap

            swap += 1
            print("        updated list: ", num_list)
        print(
            "total number of swaps performed by insertion sort: {s}\n".format(s=swap))


# parameters are the list to be sorted, and a list of gap values to use
def shell_sort_algorithm(n_list, gap_values):
    for gap_value in gap_values:

        for i in range(gap_value):
            insertion_sort_interleaved(n_list, i, gap_value)


# main program
number_list = [19, 200, 2, 5, 90, 0]
# note that gap values should be in decending order, and recommended to have 1 as the last number
gap_values_list = [6, 3, 1]
print("Initial list: ", number_list)

#test_insertion_sort = insertion_sort_interleaved(number_list, 0, 1)

result = shell_sort_algorithm(number_list, gap_values_list)
print("final result: ", number_list)
