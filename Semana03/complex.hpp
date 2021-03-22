#ifndef COMPLEX_HPP
#define COMPLEX_HPP

#include <string>

class Complex
{
private:
    double a, b;
    double r, theta;

public:
    enum Form
    {
        RECTANGULAR,
        POLAR
    };

    Complex();
    Complex(double arg1, double arg2, Form f);
    Complex operator+(Complex &c);
    Complex operator-(Complex &c);
    Complex operator*(Complex &c);
    Complex operator/(Complex &c);
    std::string print(Form f);
};

#endif // COMPLEX_HPP
