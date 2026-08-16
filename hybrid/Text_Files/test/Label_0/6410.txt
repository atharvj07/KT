#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;
  string s;
  cin>>n>>s;
  int ans=0;
  int a=0;
  for(int i=0;i<n;i++){
    if(s.at(i)=='I'){a++;ans=max(ans,a);}
    else{a--;}
  }
  cout<<ans;
}