#include<bits/stdc++.h>
using namespace std;
int main(){
  int a,b,c,k;
  cin>>a>>b>>c>>k;
  if(k<=a) cout<<k<<endl;
  else if(a<k&&k<=a+b) cout<<a<<endl;
  else cout<<2*a+b-k<<endl;

}
