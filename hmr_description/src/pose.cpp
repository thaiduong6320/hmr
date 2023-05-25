// #include "ros/ros.h"
// #include "std_msgs/Float64.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include "unistd.h"

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
  // Khai báo vector để lưu các dòng đọc được
  vector<string> lines;
  string line;
  //Mở file bằng ifstream
  ifstream input_file(filename);
  //Kiểm tra file đã mở thành công chưa
  if (!input_file.is_open()) {
      cerr << "Could not open the file - '"
          << filename << "'" << endl;
      return EXIT_FAILURE;
  }
  //Đọc từng dòng trong
  while (getline(input_file, line, ',')){
      lines.push_back(line);//Lưu từng dòng như một phần tử vào vector lines.
  }
  //Xuất từng dòng từ lines và in ra màn hình
  for (const auto &i : lines)
      cout << i << endl;
      sleep(1);
      // lp1 = (i[0]);
      // lp2 = (i[1]);
      // lp3 = (i[2]);
      // rp1 = (i[3]);
      // rp2 = (i[4]);
      // rp3 = (i[5]);
  //Đóng file
  input_file.close();
  return 0;
}