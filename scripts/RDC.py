import csv


def process_csv(input_file, output_file):
    with open(input_file, 'r') as csv_input:
        reader = csv.reader(csv_input)
        next(reader)  # Skip header
        data = list(reader)
    
    cumulative_failure_count = 0
    cumulative_time = 0

    with open(output_file, 'w', newline='') as csv_output:
        writer = csv.writer(csv_output, delimiter=',')
        writer.writerow(['Cumulative Failure Count', 'Time Between Failure', 'Cumulative Time'])
        
        for row in data:
            equal_distribution = 1

            if int(row[1]) != 0:
                equal_distribution = 1 / int(row[1])
            
            for _ in range(int(row[1])):
                cumulative_failure_count += 1
                cumulative_time += equal_distribution
                writer.writerow([cumulative_failure_count, "{:.4f}".format(equal_distribution), "{:.4f}".format(cumulative_time)])


if __name__ == "__main__":
    input_file = "failure-data-a5/failure-dataset-a5.csv"
    output_file = "failure-data-a5/failure-data-RDC.csv"
    process_csv(input_file, output_file)
    print("Data prepared.")
