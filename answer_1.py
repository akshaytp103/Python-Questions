import statistics
import csv


def find_mean_and_standard_deviation(start_time, end_time):
    data = [] 
    # open the csv file 
    with open('Data/API_response_time.csv', 'r') as file:
        my_reader = csv.DictReader(file, )  
        for row in my_reader:
            if start_time <= row['date_time'] <=end_time:
                data.append(float(row['response_time']))
    # find mean and stdev 
    print('Average=',statistics.mean(data))
    print('Standard deviation=',statistics.stdev(data))

start_time=input('Enter starting time (Format=05/16/2021 16:14:36)')
end_time=input('Enter ending time (Format=05/16/2021 16:15:17)')
# start_time='05/16/2021 16:14:36'
# end_time='05/16/2021 16:15:17'

find_mean_and_standard_deviation(start_time, end_time)







        






# find_mean_and_standard_deviation(start_time="05/16/2021 16:14:36",
# end_time="05/16/2021 16:15:17")
