#include <iostream>
#include <math.h>
using namespace std;
class Square{
  public: 
  int x1;
  int x2;
  int y1;
  int y2;
  
  
  Square(){
    x1 = 1;
    x2 = 2;
    y1 = 1;
    y2 = 2;
  }
  double calc_dist(){
      return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
  }
  int dist_x(){
      return fabs(x2 - x1);
  }
  int dist_y(){
      return fabs(y2 - y1);
  }
  int area(){
      return dist_x() * dist_y();
  }
  int perimeter(){
      return 2 * (dist_x() + dist_y());
  }
};
int main ()
{
  Square a;
    cout << a.perimeter()<< endl;
    cout<< a.area();
  return 0;
}
