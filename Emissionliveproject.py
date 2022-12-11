import matplotlib.pyplot as plt
# task 6
# Time to handle exceptions and inputs entered by user.

# task 5
# 1 You will extract data for up to three user-selected countries and save it to a new file Emissions_subset.csv.
# 2 The new file should have the exact same format as the source file, i.e. first line of headers and then up to 3 lines
# for selected countries.
# 2 creating a fun that take one list input and check for 3 countries and write into Emissions_subset.csv
def extract_data(country):
    list_len = len(country)
    for length in range(0, list_len):
        if list_len > 3:
            print("error:at most 3 countries entered", end="\n")
            return False
        else:
            write_line_csv = list(dict_from_csv.keys())[0].title() + "," + ",".join(list(dict_from_csv.values())[0]) + "\n"
            for num in range(0, len(country)):
                write_line_csv += country[num].title() + "," + ",".join(
                    dict_from_csv[country[num]]) + "\n"
            # Open CSV in write mode and writing lines to CSV
            with open('Emissions_subset.csv', 'w') as new_file:
                new_file.writelines(write_line_csv)
            # Printing the value in required format
            print(f"Data successfully extracted for countries " + ", ".join(country).title() + " saved into file Emissions_subset.csv", end="\n\n")
        return True
# task 6
try:
    dict_from_csv = {}
    print("Emissions data Analysis")
    """
    Reading the countries in lower case.
    """
    with open('Emissions.csv', mode='r') as file:
        for data in file.read().split('\n'):
            dict_from_csv.update({data.split(',')[0].lower(): data.split(',')[1:]})
    print("All data from Emissions.csv has been read into a dictionary.", end='\n\n')

    # 2nd task
    # take input from user
    """
    looping until user don't enter expected input
    """
    while True:
        input_year = input("select the year for statistics (1997-2010)")
        if not input_year.isdigit() or not 1997 <= int(input_year) <= 2010:
            print("Sorry that is not a valid year.")
            continue
        else:
            break
    index_of = int()
    lines = []
    # Extract index of year
    for item in dict_from_csv.values():
        if input_year in item:
            index_of = (item.index(input_year))
    total = 0
    i = 0
    emission_in_year = []
    # Creating the list of emission in year
    for value in dict_from_csv.values():
        if i != 0:
            total += float(value[index_of])
            emission_in_year.append(list(dict_from_csv.values())[i][index_of])
        i += 1
    # Performing the analysis
    max_country_index = int(emission_in_year.index(str(max(float(str_value) for str_value in emission_in_year))))
    min_country_index = int(emission_in_year.index(str(min(float(str_value) for str_value in emission_in_year))))
    average_emission = total / 195
    max_emission = list(dict_from_csv.keys())[max_country_index + 1]
    min_emission = list(dict_from_csv.keys())[min_country_index + 1]
    # Printing the data in required format using formatted string
    print(f'In {input_year}, countries with minimum and maximum c02 emission levels are:[{min_emission}]'
          f'and [{max_emission}] respectively.')
    print(f'average co2 emission in {input_year} were {"%.6f" % round(average_emission, 6)}')
    print()
    """
    Making it case insensitive and checking for availability for country in keys
    """
    # task3
    # take input from user to visualize the data.
    while True:
        visualize_country = input("select country to visualize").lower()
        if visualize_country in dict_from_csv.keys():
            # Getting the index of Country and passing it to plot function, Setting the Title and Label of Plot
            number = list(dict_from_csv.keys()).index(visualize_country)
            plt.plot(list(map(float, list(dict_from_csv.values())[0])),
                     list(map(float, list(dict_from_csv.values())[number])))
            plt.title("Year vs Emissions in Capital")
            plt.xlabel("Year")
            plt.ylabel("Emissions in " + visualize_country.title())
            plt.show()
            print()
            break
        else:
            print("Sorry that is not a valid Country.")
            continue
    # task4
    # we will plot a comparison graph based on user input
    """
    Making it case insensitive and checking for availability for country in keys - Using power of python to get data into two country variable
    """
    while True:
        try:
            country1, country2 = input("write two countries separated by comma which you want to visualize data:").lower().split(", ")
        except ValueError:
            print("Please write up to two comma-separated countries for which you want to visualize data...")
            continue
        if country1 not in dict_from_csv.keys() or country2 not in dict_from_csv.keys():
            print("Sorry that is not a valid Country.")
            continue
        else:
            index_num1 = list(dict_from_csv.keys()).index(country1)
            index_num2 = list(dict_from_csv.keys()).index(country2)
            plt.plot(list(map(float, list(dict_from_csv.values())[0])),
                     list(map(float, list(dict_from_csv.values())[index_num1])), label=country1)
            plt.plot(list(map(float, list(dict_from_csv.values())[0])),
                     list(map(float, list(dict_from_csv.values())[index_num2])), label=country2)
            plt.title("year vs Emissions in Capital")
            plt.xlabel("Year")
            plt.ylabel("Emissions")
            plt.legend()
            plt.show()
            print()
            break
    # task 5
    """
    Step 1: Take input up to three comma-separated countries and creating list of countries (Passing value to our function)
    """
    """
    Making it case insensitive
    """

    while True:
        input_string = input("Write up to three comma-separated countries for which you want to extract data: ").lower()
        input_country = input_string.split(", ")
        # Calling the Function to validate input
        if not extract_data(input_country):
            continue
        else:
            break

except FileNotFoundError:
    print("File not found....")
except IOError:
    print("Output file can’t be saved")
