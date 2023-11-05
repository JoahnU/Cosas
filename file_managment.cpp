#include <iostream>
#include <fstream>
using namespace std;
int vocals() {
    fstream file;
    string vocals[] = {"a","e", "i" , "o", "u"};
    string x[] = {};
    int count = 0;
    file.open("dog_breeds.txt", ios::in);
    int i = 0;
    while (true) {
        i++;
        file<< x[i];
        count += 1;

        if (file.eof()) {
            break;
        }


    }
    int count_v = 0;
    for(int h = 0; h < count; h++){
        string letra = x[h];
        for(const string& vocal : vocals){
            if(letra == vocal){
                count_v++;
            }

        }
    }
    file.close();
    return count_v;
}
int consonants(){
    fstream file;
    string vocals[] = {"a","e", "i" , "o", "u"};
    string x[] = {};
    int count = 0;
    file.open("dog_breeds.txt", ios::in);
    int i = 0;
    while (true) {
        i++;
        file<< x[i];
        count += 1;

        if (file.eof()) {
            break;
        }


    }
    int count_con = 0;
    for(int h = 0; h < count; h++){
        string letra = x[h];
        for(const string& vocal : vocals){
            if(letra != vocal){
                count_con++;
            }

        }
    }
    cout<< x;
    file.close();
    return count_con;

}

int main(){
    cout<< vocals();
    cout<< consonants();



}
