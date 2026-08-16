#include<bits/stdc++.h>
using namespace std;
signed main(){
  int a,b=0,d=0;
  string c[3];
  cin>>a;
  for(int i=0;i<3;i++) cin>>c[i];
  for(int i=0;i<a;i++){
    b=0;
    if(c[0][i]==c[1][i]);
    else b++;
    if(c[0][i]==c[2][i]);
    else b++;
    if(c[1][i]==c[2][i]);
    else b++;
    d=(b+1)/2+d;
    }
  cout<<d<<"\n";
  }
