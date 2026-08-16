#include <iostream>
using namespace std;
int main(){
  int r,g,b;
  cin>>r>>g>>b;
  int a=10*g+b;
  if(0==a%4){
    cout<<"YES";
  }else{
    cout<<"NO";
  }
}