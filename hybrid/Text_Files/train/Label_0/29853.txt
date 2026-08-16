#include<bits/stdc++.h>
#define MOD 1000000007
using namespace std;
int i,n,a[52];
long long x;
string s,t;
int main(){
  cin>>n>>s>>t;
  if(s[0]==s[1])i=2,x=6;
  else i=1,x=3;
  for(;i<s.size();){
    if(s[i]==s[i+1]){
      if(s[i-2]==s[i-1])x=x*3%MOD;
      else x=x*2%MOD;
      i+=2;
    }
    else if(s[i-1]==t[i-1])x=x*2%MOD,++i;
    else ++i;
  }
  cout<<x<<endl;
}
