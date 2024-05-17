import csv
def read_csv(input_file):
    with open(input_file,"r",newline="") as csv_file:
        rows = list(csv.reader(csv_file))
        for row in rows:
            for i in row:
                print(i,end = " ")
            print()
def read_column(input_file,noofdays):
    col = []
    day = int(input("\nEnter the day: "))
    if day > 0 and day <= noofdays:
        with open(input_file,"r",newline="") as csv_file:
            rows = list(csv.reader(csv_file))
            for row in rows:
                col.append(row[day])
            for i in col:
                print(i)
    else:
        print("\nInvalid Day")
def modify_column(input_file):
    c = 0
    day = int(input("\nEnter the day: "))
    holiday = input("\nIs it a holiday?: ")
    if holiday.title() in ["Y","Yes"]:
        with open(input_file,"r",newline="") as csv_file:
            rows = list(csv.reader(csv_file))
            for i in range(1,len(rows[1:])+1):
                rows[i][day] = "Holiday"
        with open(input_file,"w",newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(rows)
        print("Data Written into {}".format(input_file))
    elif holiday.title() in ["N","No"]:
        with open(input_file,"r",newline="") as csv_file:
            rows = list(csv.reader(csv_file))
            for i in range(1,len(rows[1:])+1):
                mark = input("Number {}. Enter Yes to mark present. Enter no to mark absent: ".format(i))
                if mark.title() in ["Yes","Y"]:
                    rows[i][day] = "Present"
                elif mark.title() in ["No","N"]:
                    rows[i][day] = "Absent"
                else:
                    print("Invalid Option")
                    break
        with open(input_file,"w",newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(rows)
        print("Data Written into {}".format(input_file))
    else:
        print("Invalid Option")
            
while True:
    option = int(input("Press 1 to view records. Press 2 to add new records: "))
    if option == 1:
        month = input("\nEnter the month: ")
        if month.lower() in ["6","june","jun"]:
            option1 = int(input("\nPress 1 to view the whole records, 2 to display a specific row: "))
            if option1 == 1:
                read_csv("june.csv")
            elif option1 == 2:
                read_column("june.csv",30)
        elif month.lower() in ["7","july","jul"]:
            option1 = int(input("\nPress 1 to view the whole records, 2 to display a specific row: "))
            if option1 == 1:
                read_csv("july.csv")
            elif option1 == 2:
                read_column("july.csv",31)
        elif month.lower() in ["8","august","aug"]:
            option1 = int(input("\nPress 1 to view the whole records, 2 to display a specific row: "))
            if option1 == 1:
                read_csv("august.csv")
            elif option1 == 2:
                read_column("august.csv",31)
        elif month.lower() in ["9","september","sep"]:
            option1 = int(input("\nPress 1 to view the whole records, 2 to display a specific row: "))
            if option1 == 1:
                read_csv("september.csv")
            elif option1 == 2:
                read_column("september.csv",30)
        elif month.lower() in ["10","october","oct"]:
            option1 = int(input("\nPress 1 to view the whole records, 2 to display a specific row: "))
            if option1 == 1:
                read_csv("october.csv")
            elif option1 == 2:
                read_column("october.csv",31)
        elif month.lower() in ["11","november","nov"]:
            option1 = int(input("\nPress 1 to view the whole records, 2 to display a specific row: "))
            if option1 == 1:
                read_csv("november.csv")
            elif option1 == 2:
                read_column("november.csv",30)
        elif month.lower() in ["12","december","dec"]:
            option1 = int(input("\nPress 1 to view the whole records, 2 to display a specific row: "))
            if option1 == 1:
                read_csv("december.csv")
            elif option1 == 2:
                read_column("december.csv",31)
        elif month.lower() in ["1","january","jan"]:
            option1 = int(input("\nPress 1 to view the whole records, 2 to display a specific row: "))
            if option1 == 1:
                read_csv("january.csv")
            elif option1 == 2:
                read_column("january.csv",31)
        else:
            print("\nInvalid month/month does not exist.")
        print()
    elif option == 2:
        month = input("\nEnter the month: ")
        if month.title() in ["6","June","Jun"]:
            modify_column("june.csv")
        elif month.title() in ["7","July","Jul"]:
            modify_column("july.csv")
        elif month.title() in ["8","August","Aug"]:
            modify_column("august.csv")
        elif month.title() in ["9","September","Sep"]:
            modify_column("september.csv")
        elif month.title() in ["10","October","Oct"]:
            modify_column("october.csv")
        elif month.title() in ["11","November","Nov"]:
            modify_column("november.csv")
        elif month.title() in ["12","December","Dec"]:
            modify_column("december.csv")
        elif month.title() in ["1","January","Mar"]:
            modify_column("january.csv")
    else:
        break
