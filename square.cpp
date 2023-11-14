#include <iostream>
#include <math.h>
using namespace std;
class Square{
  public: 
  int x1;
  int x2;
  int y1;
  int y2;
  int px;
  int py;
  
  
  
  Square(){
    x1 = 0;
    x2 = 3;
    y1 = 0;
    y2 = 3;
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
  bool contains(int px, int py){
     bool contain = true;
      if(px > x1 && py > y1 || py == y1 && px < x2 || px == x2 && py < y2 || py == y2){
        return contain;
      }else{
        contain = false;
        return contain;
      }
  }
};
int main ()
{
  Square a;
  int punto_x;
  int punto_y;
    cin >> punto_x;
    cin >> punto_y;
    cout << a.perimeter()<< endl;
    cout << a.area() << endl;
    cout << a.contains(punto_x, punto_y);
    
  return 0;
}
