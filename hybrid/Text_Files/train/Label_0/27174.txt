#include <iostream>
using namespace std;
int main(void){
    int h,a,b,i,I,s;
    cin>>h>>a>>b;
    i=a;
    s=0;
    while(1){
        if(i>b){break;}
        I=h%i;
        if(I==0){s++;}
        I=0;
        i++;
    }
    cout<<s<<endl;
}

