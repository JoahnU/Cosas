#include <iostream>
#include <math.h>
using namespace std;

class Punto{
    public:
  double lat;
  double lon;
  

  Punto(){
    lat = 0;
    lon = 0;
  }
  double calc_dist(Punto p){
    return sqrt(pow(lat-p.lat, 2) + pow(lon-p.lon, 2));
  }

    Punto(double la, double lo){
        lat = la;
        lon = lo;
    }

    void print(){
        cout<< lat << ", "<< lon;
    }
};

int main(){
    Punto p;
    Punto p2 = Punto(1,1);

    p.print();
    p2.print();
    cout << p.calc_dist(p2);

    return 0;
}