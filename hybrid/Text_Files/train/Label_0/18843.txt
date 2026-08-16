#include <bits/stdc++.h>
using namespace std;
int main(){
  int n,ans=0;
  cin>>n;
  for(int i=0,a;i<n;i++){
    cin>>a;ans+=a-1;
  }
  cout<<ans<<endl;
}