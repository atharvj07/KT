#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;
  cin>>n;
  int m=n%10;
  if(m==3)cout<<"bon"<<endl;
  else if(m==0||m==1||m==6||m==8)cout<<"pon"<<endl;
  else cout<<"hon"<<endl;
  return 0;
}
