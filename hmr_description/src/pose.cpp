// #include "ros/ros.h"
// #include "std_msgs/Float64.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <cctype>
#include <cstring>
#include "unistd.h"
#include <cassert>

using namespace std;

string split(string str, string delimiter){
    size_t pos = 0;
    string token;
    while ((pos = str.find(delimiter)) != string::npos) {
        token = str.substr(0, pos);
        cout << token << endl;
        str.erase(0, pos + delimiter.length());
    }
    return str;
}

int main(int argc, char **argv)
{
    string lp1;
    string lp2;
    string lp3;
    string rp1;
    string rp2;
    string rp3;
    string filename("/home/dev/hmr_ws/src/hmr/hmr_description/src/pose.csv");
    vector<string> lines;
    string line;
    int i = 0;
    //Open file with ifstream
    ifstream input_file(filename);
    //Check open file
    if (!input_file.is_open()) {
        cerr << "Could not open the file - '"
            << filename << "'" << endl;
        return EXIT_FAILURE;
    }
    //Read line
    while (getline(input_file, line, '\n'))
    {
        lines.push_back(line);//Save line
        if (i<7)
        {
            string f = {lines[i].c_str()};
            float k[] = {stof(split(f,","))};
            char arr[]  = "k";
            cout << arr << endl;
            sleep(1);
            i = i + 1;
        }
    }
    
    input_file.close();
    return 0;
}