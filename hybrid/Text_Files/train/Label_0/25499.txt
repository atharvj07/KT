#include <bits/stdc++.h>
using namespace std;
int main(){
  int n; cin >> n;
  map<int,int> a;
  for(int i = 0; i < n; i++){
    int x; cin >> x;
    a[x]++;
  }
  bool bad = false;
  if(n&1){
    if(a[0] != 1) bad = true;
    for(int i = 2; i < n; i += 2) if(a[i] != 2) bad = true;
  } else {
    for(int i = 1; i < n; i += 2) if(a[i] != 2) bad = true;
  }
  if(bad) cout << 0 << endl;
  else {
  	int ans = 1;
    for(int i = 0; i < n/2; i++) ans = (ans + ans) % 1000000007;
    cout << ans << endl;
  }
  return 0;
}