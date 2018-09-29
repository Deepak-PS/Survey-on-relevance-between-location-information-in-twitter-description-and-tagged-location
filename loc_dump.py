import csv


def operate_us_data():
    with open('Dictionary of Places/us_cities_states_counties.csv') as csvfile:
        reader = csv.reader(csvfile)
        with open('Dictionary of Places/location_data_dump.csv', "a+") as csv_file:
            for row in reader:
                #                 print(row[0])
                loc_arr = row[0].split('|')
                loc_arr.append('USA')
                loc_arr.append('The US')
                loc_arr.append('America')
                #                 line = loc_arr[0] + ',' + loc_arr[1] + ',' + loc_arr[2] + ',' + loc_arr[3] + ',' + loc_arr[4]
                #                 print(line)
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(loc_arr)
                # print(loc_arr)

operate_us_data()


def operate_ca_data():
    loc_arr_final = []
    with open('Dictionary of Places/ca-cities-sample.csv') as csvfile:
        reader = csv.reader(csvfile)
        with open('Dictionary of Places/location_data_dump.csv', "a+") as csv_file:
            for row in reader:
                # print(row)
                loc_arr = []
                loc_arr.append(row[1])
                loc_arr.append(row[4])
                loc_arr.append(row[3])
                loc_arr.append(row[2])
                loc_arr.append('')
                loc_arr.append('Canada')

                loc_arr_final.append(loc_arr)

            for loc_ele in loc_arr_final:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(loc_ele)
            # print(loc_arr_final)


operate_ca_data()

def operate_nz_data():
    with open('Dictionary of Places/new_zealand-cities-sample.csv') as csvfile:
        reader = csv.reader(csvfile)
        with open('Dictionary of Places/location_data_dump.csv', "a+") as csv_file:
            for row in reader:
                row.append('New Zealand')
                row.append('NZ')
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(row)
            # print(loc_arr_final)


operate_nz_data()

def operate_au_data():
    loc_arr_final = []
    with open('Dictionary of Places/list-cities-australia-sample.csv') as csvfile:
        reader = csv.reader(csvfile)
        with open('Dictionary of Places/location_data_dump.csv', "a+") as csv_file:
            for row in reader:
                row.append('Australia')
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(row)
            # print(loc_arr_final)


operate_au_data()

def operate_uk_data():
    with open('Dictionary of Places/list-cities-uk.csv') as csvfile:
        reader = csv.reader(csvfile)
        with open('Dictionary of Places/location_data_dump.csv', "a+") as csv_file:
            for row in reader:
                row.append('UK')
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(row)
            # print(loc_arr_final)


operate_uk_data()