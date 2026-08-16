#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<ll,ll>;
#define rep(i,s,n) for(int i = s; i < (int)(n); i++)

int main() {
  int n,ans = 0;
  cin >> n;
  vector<ll>x(n);
  vector<ll>y(n);
  rep(i,0,n) cin >> x[i] >> y[i];
  rep(i,0,n-1){
    rep(j,i+1,n){
      int cnt = 0;
      ll sx = x[i]-x[j];
      ll sy = y[i]-y[j];
      rep(k,0,n-1){
        rep(l,k+1,n){
          if((x[k]-x[l] == sx && y[k]-y[l] == sy)||(x[k]-x[l] == -sx && y[k]-y[l] == -sy)) cnt++;
        }
      }
      ans = max(ans,cnt);
    }
  }
  cout << n-ans << endl;
}