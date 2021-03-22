#include <iostream>
#include <math.h>
#include "complex.hpp"
using namespace std;

int main()
{
    Complex c1(2, 3, Complex::RECTANGULAR);
    cout << "c1: " << c1.print(Complex::RECTANGULAR) << endl;
    cout << "c1: " << c1.print(Complex::POLAR) << endl;

    Complex c2(5, M_PI / 4, Complex::POLAR);
    cout << "c2: " << c2.print(Complex::RECTANGULAR) << endl;
    cout << "c2: " << c2.print(Complex::POLAR) << endl;

    Complex res;

    res = c1 + c2;
    cout << "c1 + c2: " << res.print(Complex::RECTANGULAR) << endl;

    res = c1 - c2;
    cout << "c1 - c2: " << res.print(Complex::RECTANGULAR) << endl;

    res = c1 * c2;
    cout << "c1 * c2: " << res.print(Complex::POLAR) << endl;

    res = c1 / c2;
    cout << "c1 / c2: " << res.print(Complex::POLAR) << endl;

    return EXIT_SUCCESS;
}