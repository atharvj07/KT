#include<bits/stdc++.h>
using namespace std;

int main(){
  int n,ans=0,i;
  cin >> n;
  vector<int> v(n), c(n);
  for(i=0; i<n; i++){
    cin >> v[i];
  }
  for(i=0; i<n; i++){
    cin >> c[i];
    ans+=max(0,v[i]-c[i]);
  }
  cout << ans;
}