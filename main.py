import os
import json
import csv

# Data structure that all files will be converted into
# data = [
#     {"name": "John Doe", "email": "john@example.com", "age": "30"},
#     {"name": "Jane Smith", "email": "jane@example.com", "age": "25"},
#     {"name": "", "email": "missingemail@sample.com", "age": "27"},
#     {"name": "Bob Ross", "email": "bob@example.com", "age": ""}
# ]



def load_csv(filepath):
    # open the file using csv.DictReader
    # read all rows into a list of dictionaries
    # return the list
    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                for key in row:
                    if row[key] == "":
                        row[key] = "none"
                
                data.append(row)
            return data
    except Exception as e:
        print(e)
            


def load_json(filepath):
    # open the file and parse using json.load
    # get the value from the top-level key (e.g., data["employees"])
    # return the list
    try:
        with open(filepath, "r") as file:
            records = json.load(file)

            #unwrapper, most real world examples know what the key is, but in this case we dont
            if isinstance(records, dict) and len(records) == 1: #checks if its wrapped and if its a toplevel dict
                value = next(iter(records.values()))

                if isinstance(value, list): #if its a list like we assumed
                    records = value


            for row in records:
                for key in row:
                    if row[key] == "":
                        row[key] = "none"
                    else:
                        row[key] = str(row[key]) #because json saves original type
            
            return records
    except Exception as e:
        print(e)  
                
            



def load_txt(filepath):
    # open the file and read lines
    # for each line:
    #     split by ',' → key:value pairs then split again into individual keys and values
    #     build a dictionary
    #     append to a dictionary for each row
    # append the dictionary to the list
    try:
        with open(filepath, "r") as file:
            data = []
            
            for line in file:
                line = line.strip()
                diction = {}
                parts = line.split(",")
                for part in parts:
                    key, value =part.split(":", 1)
                    diction[key] = value
                    if diction[key] == "":
                        diction[key] = "none"

                data.append(diction)
            
            return data
                    


    except Exception as e:
        print(e)


def preview_data(data):
    # loop over the first 5 items in data
    # print each item clearly
    for dictionary in data[:5]:
        print(dictionary)

def search_data(data):
    # loop over each entry in data
    # if entry exists within data
    #     print the entry
    # if no matches found:
    #     print "No matches found."

    try:
        
        value = input("What value are you looking for?").lower()

        found = False
        for row in data:
            for key in row:
                if row[key].lower() == value:
                    print(f"Value {value} found within {key}")
                    print(f"\nFull row: {row}")
                    found = True
                
        if not found:
            print("No value found")
            
    
    except Exception as e:
        print(f"Error, {e}")
    


def export_csv(data, filename):
    # get all fieldnames from first entry
    # open output/filename.csv
    # write header and rows using csv.DictWriter
    # use newline because windows
    try:
        with open(filename, "w", newline='') as file:
            fieldnames = []
            for key in data[0]:
                fieldnames.append(key)

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    except Exception as e:
        print(f"Failed to write, {e}")
                




def export_json(data, filename):
    # wrap data in a top-level key (e.g., {"employees": data})
    # open output/filename.json and dump using json.dump
    try:
        with open(filename, "w") as file:
            name = input("What do you want to name the list of dictionaries?")

            wrapped = {name: data}
            json.dump(wrapped, file, indent= 4)
    
    except Exception as e:
        print(f"Failed to write, {e}")



def export_txt(data, filename):
    # open output/filename.txt
    # for each entry in data:
    #     convert to "key:value,key:value" format
    #     write line to file
    try:
        with open(filename, "w") as file:

            for row in data:

                line = ""

                for key, value in row.items():
                    line += (f"{key}:{value},")
                    
                line = line[:-1] #remove trailing comma
                file.write(line + "\n")


    except Exception as e:
        print(f"Failed to write. {e}")
        


def main():
    while True:
        filepath = input("Enter path of file you want to parse ").strip()
        filepath = "data/" + filepath  #always look in data folder

        if not os.path.isfile(filepath):
            print("File path nonexistant")
            continue
        
        ext = os.path.splitext(filepath)[1].lower() #1 looks at extension, 0 gives file name

        if not ext in [".json", ".csv", ".txt"]:
            print("Unsupported file type")
            continue

        else:
            break
    
    if ext == ".csv":
       data = load_csv(filepath)
    
    elif ext == ".json":
       data = load_json(filepath)
    
    elif ext == ".txt":
       data = load_txt(filepath)

    while True:
        print("\nWhat do you want to do?")
        print("1. Preview data")
        print("2. Search by key/value")
        print("3. Export cleaned data")
        print("4. Exit")

        menu_actions = input("Select number correlating to an action: ").strip()

        if menu_actions == "1":
            preview_data(data)

        elif menu_actions == "2":
            search_data(data)  # search_data(data, key, value)


        elif menu_actions == "3":
            print("1: Export as CSV")
            print("2: Export as JSON")
            print("3: Export as TXT")

            while True:
                export_type = input("Select a number correlating to an action: ").strip()

                if export_type in ["1", "2", "3"]:
                    filename = input("What do you want to name the file? ").strip()

                    if export_type == "1":
                        if not filename.endswith(".csv"):
                            filename += ".csv"
                        export_csv(data, filename)

                    elif export_type == "2":
                        if not filename.endswith(".json"):
                            filename += ".json"
                        export_json(data, filename)

                    elif export_type == "3":
                        if not filename.endswith(".txt"):
                            filename += ".txt"
                        export_txt(data, filename)

                    break

                else:
                    print("Invalid selection, try again.")


            

        elif menu_actions == "4":
            print("Exiting.")
            break

        else:
            print("Invalid selection. Try again.")

    



if __name__ == "__main__":
    main()