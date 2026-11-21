#include <iostream>
#include <string>

struct LabStatus {
    std::string mode = "RED_HACKER";
    bool simulationOnly = true;
    bool networkAccess = false;
};

int main() {
    const LabStatus status{};
    std::cout << "NATIONVK LAB: " << status.mode
              << "\nSIMULATION ONLY: " << std::boolalpha << status.simulationOnly
              << "\nNETWORK ACCESS: " << status.networkAccess << '\n';
    return 0;
}
