#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char const *argv[])
{
    if (argc < 3)
    {
        cerr << "Missing arguments" << endl;
        return EXIT_FAILURE;
    }

    string src = argv[1];
    string dst = argv[2];

    streampos size;
    char *buffer;

    //src file is open with the ios::ate flag, which means that the get pointer will be positioned at the end of the file
    //this way, when we call to member tellg(), we will directly obtain the size of the file
    ifstream in(src, ios::in | ios::binary | ios::ate);
    if (in.is_open())
    {
        size = in.tellg();
        buffer = new char[size];

        //set the get position at the beginning of the file, then we read the entire file
        in.seekg(0, ios::beg);
        in.read(buffer, size);
        in.close();

        cout << "File " << src << " successfully read" << endl;
        cout << "Size: " << size << endl;
    }
    else
    {
        cerr << "Failed to open src file " << src << endl;
        return EXIT_FAILURE;
    }

    ofstream out(dst, ios::out | ios::binary);
    if (out.is_open())
    {
        out.write(buffer, size);
        out.close();
        cout << "File " << dst << " successfully written" << endl;
    }
    else
    {
        cerr << "Failed to open dst file " << dst << endl;
        return EXIT_FAILURE;
    }

    delete[] buffer;

    return EXIT_SUCCESS;
}