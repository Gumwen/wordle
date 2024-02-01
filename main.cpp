#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main() {
  ifstream inFile;
  float temperature;
  float sum = 0.0;
  float average;
  int count = 15;
  inFile.open("InputFile.txt");

  if (!inFile)
  {
    cout<<"Cannot open file"<<endl;
    exit(-1);
  }
  while (count >0)
    {
      inFile>> temperature;
      sum = sum + temperature;
      count--;
    }
  average = sum/15;
  cout<<"The average temperature is "<<setprecision(4)<<average<<endl;
}