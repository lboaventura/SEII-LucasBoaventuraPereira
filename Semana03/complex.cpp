#include <math.h>
#include "complex.hpp"

Complex::Complex() {}

Complex::Complex(double arg1, double arg2, Form f)
{
    if (f == RECTANGULAR)
    {
        a = arg1;
        b = arg2;

        r = sqrt(pow(a, 2) + pow(b, 2));
        theta = atan(b / a);
    }
    else if (f == POLAR)
    {
        r = arg1;
        theta = arg2;

        a = r * cos(theta);
        b = r * sin(theta);
    }
}

Complex Complex::operator+(Complex &c)
{
    return Complex(a + c.a, b + c.b, RECTANGULAR);
}

Complex Complex::operator-(Complex &c)
{
    return Complex(a - c.a, b - c.b, RECTANGULAR);
}

Complex Complex::operator*(Complex &c)
{
    return Complex(r * c.r, theta + c.theta, POLAR);
}

Complex Complex::operator/(Complex &c)
{
    return Complex(r / c.r, theta - c.theta, POLAR);
}

std::string Complex::print(Form f)
{
    if (f == RECTANGULAR)
    {
        return std::to_string(a) + " + " + std::to_string(b) + "i";
    }
    else if (f == POLAR)
    {
        return std::to_string(r) + " < " + std::to_string(theta * 180 / M_PI) + "°";
    }
    else
    {
        return "Invalid complex form";
    }
}