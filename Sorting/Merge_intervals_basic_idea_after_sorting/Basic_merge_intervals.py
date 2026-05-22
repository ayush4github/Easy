def merge_intervals(intervals):
    intervals.sort()
    merged_intervals = []
    for interval in intervals: 
        if not merged_intervals or interval[0]>merged_intervals[-1][1]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1][1]=max(merged_intervals[-1][1], interval[1])
    return merged_intervals
number_of_intervals = int(input("Enter number of intervals: "))
intervals = []
for interval_index in range(number_of_intervals):
    start, end = map(int, input("Enter start and end: ").split())
    intervals.append([start, end])
result = merge_intervals(intervals)
print("Merged intervals", result)