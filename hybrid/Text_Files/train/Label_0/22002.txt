#include<bits/stdc++.h>
using namespace std;

int main(){
  int n,m;cin>>n>>m;
  long long s=0;
  for(int i=0;i<n;i++){int x;cin>>x;s+=x;}
  long long t=0;
  for(int j=0;j<m;j++){int x;cin>>x;t+=x;}
  cout<<(s*t)<<endl;
}
