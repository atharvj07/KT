#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i = 0; i < (int)n; i++)
using ll = long long;
using P = pair<ll,ll>;

int main(){
  int n;
  cin >> n;
  ll a[n], b[n];
  priority_queue<P> que;
  bool can = true;
  rep(i,n) cin >> a[i];
  rep(i,n) {
    cin >> b[i];
    if(a[i] > b[i]) can = false;
    que.push(P(b[i],i));
  }
  if(!can) {
    cout << -1 << endl;
    return 0;
  }
  ll d = 0;
  while(!que.empty()) {
    P p = que.top();
    que.pop();
    int l = (p.second-1+n) % n, r = (p.second+1) % n;
    ll s = b[l] + b[r];
    ll c = min(b[p.second]/s,(b[p.second]-a[p.second])/s);
    if(c != 0) {
      b[p.second] -= s*c;
      que.push(P(b[p.second],p.second));
      d += c;
    } 
  }
  rep(i,n) {
    if(a[i] != b[i]) can = false;
  }
  cout << (can? d : -1) << endl;
  return 0;
}