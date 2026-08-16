#include <bits/stdc++.h>
using namespace std;

#define int long long
#define rep(i,n) for(int i=0,i##_cond=(n);i<i##_cond;++i)

signed main(){
  int n, k; cin >> n >> k;
  int ans = 0;
  rep(i,n-1){
    ans += ans/(k-1) + 1;
  }
  cout << ans << endl;
}
