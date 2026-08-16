#include<bits/stdc++.h>
using namespace std;
int n,i,j,a,c;
string s;
int main()
{
  for(i=1,cin>>n;i<=n;i++){
    for(c=0,j=i;j!=0;j/=10)c++;
    if(c&1)a++;
  }
  cout<<a;
}