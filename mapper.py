import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

no_ner = 0
no_ner_final = 0

perfect_match = 0
partial_match = 0
no_match = 0
regional_match = 0

perfect_match_final = 0
partial_match_final = 0
no_match_final = 0
regional_match_final = 0


def update_final_counts():
    global no_ner
    global no_ner_final

    global perfect_match_final
    global partial_match_final
    global no_match_final
    global regional_match_final

    global perfect_match
    global partial_match
    global no_match
    global regional_match

    if perfect_match > 0:
        perfect_match_final = perfect_match_final + 1
    elif partial_match > 0:
        partial_match_final = partial_match_final + 1
    elif no_match > 0:
        no_match_final = no_match_final + 1
    elif regional_match > 0:
        regional_match_final = regional_match_final + 1
    elif no_ner > 0:
        no_ner_final = no_ner_final + 1

    perfect_match, partial_match, no_match, regional_match = 0, 0, 0, 0


def check_no_match_condition(area_ner, area):
    with open('Dictionary of Places/location_data_dump.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for place in row:
                if place != area and place != area_ner:
                    return True


def check_for_alias(area_ner, area):
    count = 0
    with open('Dictionary of Places/location_data_dump.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                if len(row) > 0:
                    if row[4] != "":
                        if row[0] == area and row[1] == area_ner:
                            # print("Perfect Match", area_ner, area)
                            count = count + 1
                        elif row[0] == area_ner and row[1] == area:
                            # print("Perfect Match", area_ner, area)
                            count = count + 1
                        elif row[0] == area and row[3] == area_ner:
                            # print("Perfect Match", area_ner, area)
                            count = count + 1
                        elif row[0] == area_ner and row[3] == area:
                            # print("Perfect Match", area_ner, area)
                            count = count + 1
                        if row[1] == area and row[4] == area_ner:
                            # print("Perfect Match", area_ner, area)
                            count = count + 1
                        elif row[1] == area_ner and row[4] == area:
                            # print("Perfect Match", area_ner, area)
                            count = count + 1
            except:
                print(row)

        if count > 0:
            return True
        else:
            return False


def check_for_perfect_match(row):
    # global perfect_match
    count = 0
    flag = 0

    loc_arr_ner = row[5].split('|')
    area_arr = row[1:3]
    for area_ner in loc_arr_ner:
        for area in area_arr:
            if area_ner != "" and area != "":
                area_ner = area_ner.strip()
                area = area.strip()
                if area_ner == area:
                    # perfect_match = perfect_match + 1
                    count = count + 1
                elif check_for_alias(area_ner, area) == True:
                    # perfect_match = perfect_match + 1
                    count = count + 1
                else:
                    flag = flag + 1

    if count > 0 and flag <= 1:
        return True
    else:
        return False


def check_for_partial_match(row):
    # global partial_match
    count = 0
    loc_arr_ner = row[5].split('|')
    area_arr = row[:4]
    for area_ner in loc_arr_ner:
        for area in area_arr:
            if area_ner != "" and area != "":
                area_ner = area_ner.strip()
                area = area.strip()
                if area_ner == area:
                    # print("Partial Match", area_ner, area)
                    # partial_match = partial_match + 1
                    count = count + 1

    if count > 0:
        return True
    else:
        return False


def check_for_regional_match(row):
    global regional_match
    count = 0
    with open('Dictionary of Places/location_data_dump.csv') as csvfile:
        reader = csv.reader(csvfile)
        loc_arr_ner = row[5].split('|')
        area_arr = row[:4]
        for area_ner in loc_arr_ner:
            for area in area_arr:
                if area_ner != "" and area != "":
                    area_ner = area_ner.strip()
                    area = area.strip()
                    for row in reader:
                        if len(row) > 0 and has_empty_strings(row) == False:
                            if row[0] == area and row[2] == area_ner:
                                count = count + 1
                            elif row[2] == area and row[0] == area_ner:
                                count = count + 1
                            elif row[1] == area and row[0] == area_ner:
                                count = count + 1
                            elif row[1] == area_ner and row[0] == area:
                                count = count + 1
                            elif row[1] == area and row[2] == area_ner:
                                count = count + 1
                            elif row[1] == area_ner and row[2] == area:
                                count = count + 1
                            elif row[0] == area and row[1] == area_ner:
                                count = count + 1
                            elif row[0] == area_ner and row[1] == area:
                                count = count + 1

                            # elif row[2] == area:
                            #     # print(row[0], area)
                            #     count = count + 1
                            # elif row[2] == area_ner:
                            #     # print(row[0], area)
                            #     count = count + 1


        if count > 0:
            # print (count)
            return True
        else:
            return False




# def check_for_no_match(area_ner, area):
#     global no_match
#     # if area_ner != area:
#     #     print("No Match", area_ner, area)
#     #     no_match = no_match + 1
#     #     return
#     if check_no_match_condition(area_ner, area) == True:
#         print("No Match", area_ner, area)
#         no_match = no_match + 1
#         return

# def check_for_a_match(area_ner, area, no_of_loc_ner):
#     global no_match
#     if no_of_loc_ner == 2:
#         check_for_perfect_match(area_ner, area)
#
#     if perfect_match != 0:
#         if check_for_alias(area_ner, area) == False:
#             check_for_partial_match(area_ner, area)
#     elif perfect_match != 0 and partial_match != 0:
#         check_for_regional_match(area_ner, area)
#     else:
#         no_match = no_match + 1
#
#         # check_for_no_match(area_ner, area)

def has_loc_entity(row):
    if len(row) >= 5:
        ner = row[5:]
        for ele in ner:
            if ele != "":
                return True
            else:
                return False
    else:
        return False



def comparator(row):
    global no_ner
    global perfect_match
    global partial_match
    global regional_match
    global no_match

    # loc_arr_ner = row[5].split('|')
    # for area_ner in loc_arr_ner:
    #     for area in row[:4]:
    #         if area_ner == "":
    #             no_ner = no_ner + 1
            # check_for_a_match(area_ner.strip(), area.strip(), len(loc_arr_ner))
    if has_loc_entity(row) == True:
        if check_for_perfect_match(row) == True:
            print("Perfect Match", row)
            perfect_match = perfect_match + 1
        elif check_for_partial_match(row) == True:
            print("Partial Match", row)
            partial_match = partial_match + 1
        elif check_for_regional_match(row) == True:
            print("Regional Match", row)
            regional_match = regional_match + 1
        else:
            print("No Match", row)
            no_match = no_match + 1
    else:
        no_ner = no_ner + 1





def has_empty_strings(loc_arr_row):
    count = 0
    for row in loc_arr_row:
        if (len(row) == 0):
            count = count + 1

    if len(loc_arr_row) == count:
        return True
    else:
        return False

def mapper():
    with open('Data/location_data_dump_neu.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) > 0 and has_empty_strings(row) == False:
                comparator(row)
                update_final_counts()

def build_bar_chart():
    print(perfect_match_final, partial_match_final, regional_match_final, no_match_final, no_ner_final)
    objects = ('Perfect Match', 'Partial Match', 'Regional Match', 'No Match')
               # 'No Location Entity')
    y_pos = np.arange(len(objects))
    # performance = [perfect_match_final, partial_match_final, regional_match_final, no_match_final, no_ner_final]
    performance = [17768, 4441, 22115, 17914]
                   # 204284]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Occurences')
    plt.title('Correlation between tagged location and location extracted from the tweet')

    plt.show()

# mapper()
build_bar_chart()