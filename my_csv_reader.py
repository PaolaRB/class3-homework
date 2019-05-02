import os

file_path = "./data/wdbc.data"

if os.path.isfile(file_path):
    print('I have a valid file!!!')
else:
    print('Invalid file, I\'ll crash')


file = open(file_path)
corrected_file = []

for line in file.readlines():
    line_values = line.split(',')
    corrected_line = []
    i = 0
    for value in line_values:
        if i == 0:
            corrected_line.append(int(value))
        elif i == 1:
            corrected_line.append(str(value))
        else:
            corrected_line.append(float(value))
        i = i + 1
    corrected_file.append(corrected_line)

print("Total records in corrected_file list = " + str(len(corrected_file)))
print("First row : " + str(corrected_file[0]))
file.close()


# saving the data in a file without transposing columns
file_path = "./data/corrected_file_no_transposing.txt"
with open(file_path, '+w') as file_handler:
    for item in corrected_file:
        file_handler.write("{}\n".format(item))


# creating a transposing nested list and saving to a file
corrected_list = [[[] for x in range(len(corrected_file))] for x in range(len(corrected_file[0]))]
print("Total records in empty corrected_list = " + str(len(corrected_list)))
print("First row : " + str(corrected_list[0]))

for i in range(len(corrected_file)):
    for j in range(len(corrected_file[0])):
        corrected_list[j][i] = corrected_file[i][j]

print("Total records in full corrected_list = " + str(len(corrected_list)))
print("First row : " + str(corrected_list[0]))

file_path = "./data/corrected_file_with_transposing.txt"
with open(file_path, '+w') as write_handler:
    for item in corrected_list:
        write_handler.write("{}\n".format(item))
