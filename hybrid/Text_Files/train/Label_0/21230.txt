#include<bits/stdc++.h>
using namespace std;
int main(){
  string s;cin >> s;
  int n=s.size();
  int ans=1e7;
  for(int i=0;i<n-1;i++){
    if(s[i]!=s[i+1]){
      ans=min(ans,max(i+1,n-i-1));
    }
  }
  if(ans==1e7){
    ans=n;
  }
  cout << ans << endl;
}