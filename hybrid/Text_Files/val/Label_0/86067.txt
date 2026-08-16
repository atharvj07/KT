#include<iostream>
using namespace std;
int main(){
  int a,b,day,A,B,bell;
  cin >> day;
  cin >> a >> b >> A >> B;
  while(a>0 || b>0){
    a=a-A;
    b=b-B;
    day--;
  }
  cout << day << endl;
}