#Variables
numbers = [];
num_index = 10;

#Functions
def my_array_search(search_number, numbers):
    for x, val in enumerate(numbers):
        if (int(search_number) == int(val)):
            return x;
    
    return -1;

### Main ###

#User input
for x in range(1,num_index + 1):
    number = input("Zadaj " +  str(x)  + ". číslo: ");

    #Input validation
    if (number.isnumeric()):
        numbers.append(int(number));
    else:
        print("Nezadali ste celé číslo. Koniec programu.");
        break;


if (len(numbers) == num_index): 
    print("Súčet všetkých zadaných čísel je: " + str(sum(numbers)));

    search_number = input("Aké číslo mám nájsť? ");

    #Input validation
    if (search_number.isnumeric()):

        #Number search
        search_index = my_array_search(search_number, numbers);

        if (search_index >= 0):
            print("Poradie: " + str(search_index+1) + ".");
        
        else:
            print("Zadané číslo sa nenašlo.");

    else:
        print("Nezadali ste celé číslo. Koniec programu.");

    