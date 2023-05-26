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
    // const char *f;
    // const char *s = ",";
    //Open file with ifstream
    ifstream input_file(filename);
    //Check open file
    if (!input_file.is_open()) {
        cerr << "Could not open the file - '"
            << filename << "'" << endl;
        return EXIT_FAILURE;
    }
    //Read line
    while (getline(input_file, line, '\n')){
        lines.push_back(line);//Save line
    }
    for (int i = 0; i < 7; i++)
    {   
        string f(string lines[], ',');
        // f = lines[i].c_str();
        // const char *token;
        // token = strtok(f, s);
        // while (token != NULL)
        // {
        //     token = strtok(NULL,s);
        // }
        
        // cout << f << endl;
    }
    input_file.close();
    return 0;
}