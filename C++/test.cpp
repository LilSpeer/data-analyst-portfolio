#include <iostream>
#include <cstdlib>
#include <string>
#include <iomanip>

using namespace std;

int main() {
    double tankCapacity = 50.0;
    double mpgTown = 21.5;
    double mpgHighway = 26.8;
    double distanceTown = tankCapacity * mpgTown;
    double distanceHighway = tankCapacity * mpgHighway;
    cout << "Town Distance: " << distanceTown << " miles" << endl;
    std::cout << std::fixed << std::setprecision(2) << "Highway distance = " + std::to_string(distanceHighway) + " miles." << std::endl;

    system ("pause");
    return 0;

}