#include <iostream>
#include <limits>
using namespace std;


int youngest = 100, oldest = 0;
int age0_18 = 0, age19_30 = 0, age31_40 = 0, age41_60 = 0, age61 = 0;
int sum = 0, numOfAgeInputs = 0;
int snack1 = 0, snack2 = 0, snack3 = 0, snack4 = 0, snack5 = 0, snack6 = 0, snack7 = 0;


void processAge(int age);
void processSnack(int snackchoice);
void displayResults();
void showSnackMenu();
int getValidAge();
int getValidSnackChoice();

int main() {
    int age = getValidAge();

    while (age != -1) {
        processAge(age);

        showSnackMenu();
        int snackchoice = getValidSnackChoice();
        processSnack(snackchoice);

        age = getValidAge();
    }

    displayResults();
    return 0;
}

int getValidAge() {
    int age;
    while (true) {
        cout << "Enter age of attendee (-1 to quit): ";
        cin >> age;

        if (cin.fail()) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input. Please enter an integer." << endl;
            continue;
        }

        if ((age >= 0 && age <= 100) || age == -1) {
            return age;
        } else {
            cout << "Age must be between 0 and 100, or -1 to quit." << endl;
        }
    }
}

int getValidSnackChoice() {
    int choice;
    while (true) {
        cout << "Select snack choice (1-7): ";
        cin >> choice;

        if (cin.fail()) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input. Please enter an integer between 1 and 7." << endl;
            continue;
        }

        if (choice >= 1 && choice <= 7) {
            return choice;
        } else {
            cout << "Snack choice must be between 1 and 7." << endl;
        }
    }
}

void processAge(int age) {
    if (age < youngest) youngest = age;
    if (age > oldest) oldest = age;

    if (age <= 18) age0_18++;
    else if (age <= 30) age19_30++;
    else if (age <= 40) age31_40++;
    else if (age <= 60) age41_60++;
        
    else age61++;

    sum += age;
    numOfAgeInputs++;
}

void processSnack(int snackchoice) {
    switch (snackchoice) {
        case 1: snack1++; break;
        case 2: snack2++; break;
        case 3: snack3++; break;
        case 4: snack4++; break;
        case 5: snack5++; break;
        case 6: snack6++; break;
        case 7: snack7++; break;
    }
}

void showSnackMenu() {
    cout << "\nMovie theater snacks available for purchase" << endl;
    cout << "==========================================" << endl;
    cout << "1 - Soft Drink" << endl;
    cout << "2 - Popcorn" << endl;
    cout << "3 - Nachos" << endl;
    cout << "4 - Soft drink & Popcorn" << endl;
    cout << "5 - Soft drink & Nachos" << endl;
    cout << "6 - Organic and Gluten-free snacks" << endl;
    cout << "7 - None" << endl;
    cout << "==========================================" << endl;
}

void displayResults() {
    cout << "\n========= THEATER STATS =========\n";
    cout << "Age 0 to 18: " << age0_18 << endl;
    cout << "Age 19 to 30: " << age19_30 << endl;
    cout << "Age 31 to 40: " << age31_40 << endl;
    cout << "Age 41 to 60: " << age41_60 << endl;
    cout << "Over 60: " << age61 << endl;

    cout << "\nSnacks sold:\n";
    cout << "1 - Soft Drink: " << snack1 << endl;
    cout << "2 - Popcorn: " << snack2 << endl;
    cout << "3 - Nachos: " << snack3 << endl;
    cout << "4 - Soft drink & Popcorn: " << snack4 << endl;
    cout << "5 - Soft drink & Nachos: " << snack5 << endl;
    cout << "6 - Organic/Gluten-free: " << snack6 << endl;
    cout << "7 - None: " << snack7 << endl;

    double average = (numOfAgeInputs > 0) ? (double)sum / numOfAgeInputs : 0;
    cout << "\nThe average age was " << average << endl;
    cout << "The youngest person in attendance was " << youngest << endl;
    cout << "The oldest person in attendance was " << oldest << endl;
}
