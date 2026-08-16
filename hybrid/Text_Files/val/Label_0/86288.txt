#include<iostream>
#include<string>
using namespace std;

int main(){
  string s;
  int a=0,b=0,c=0,ab=0,d;

  while(cin>>d){
    cin>>s;
    if(s==",A") a++;
    if(s==",B") b++;
    if(s==",O") c++;
    if(s==",AB") ab++;
  }
  cout<<a<<endl;
  cout<<b<<endl;
  cout<<ab<<endl;
  cout<<c<<endl;
}