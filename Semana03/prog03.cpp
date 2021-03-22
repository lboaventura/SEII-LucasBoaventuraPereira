#include <iostream>
using namespace std;

// recursive function to solve Tower of Hanoi puzzle
void towerOfHanoi(int n, char fromRod, char toRod, char auxRod)
{
    if (n == 1)
    {
        cout << "Move disk 1 from rod " << fromRod << " to rod " << toRod << endl;
        return;
    }
    towerOfHanoi(n - 1, fromRod, auxRod, toRod);
    cout << "Move disk " << n << " from rod " << fromRod << " to rod " << toRod << endl;
    towerOfHanoi(n - 1, auxRod, toRod, fromRod);
}

int main(int argc, char const *argv[])
{
    if (argc < 2)
    {
        cerr << "Missing number of disks argument" << endl;
        return EXIT_FAILURE;
    }

    int n = atoi(argv[1]);

    cout << "Running tower of Hanoi algorithm with " << n << " rods..." << endl;
    towerOfHanoi(n, 'A', 'C', 'B'); // A, B and C are names of rods

    return EXIT_SUCCESS;
}