#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i = 0; i < (int)n; i++)
typedef long long ll;
const ll INF = 1e15;

int main(){
  int A, B, Q;
  ll x;
  cin >> A >> B >> Q;
  ll s[A], t[B], ans[Q];
  rep(i, A) cin >> s[i];
  rep(i, B) cin >> t[i];
  rep(i, Q){
    cin >> x;
    int su = lower_bound(s, s+A, x) - s;
    int tu = lower_bound(t, t+B, x) - t;
    ll d[4];
    rep(i, 4) d[i] = INF;
    if(su < A && tu < B) d[0] = max(s[su]-x, t[tu]-x);
    if(su < A && tu > 0) d[1] = min(s[su]-x+2*(x-t[tu-1]), 2*(s[su]-x)+x-t[tu-1]);
    if(su > 0 && tu < B) d[2] = min(x-s[su-1]+2*(t[tu]-x), 2*(x-s[su-1])+t[tu]-x);
    if(su > 0 && tu > 0) d[3] = max(x-s[su-1], x-t[tu-1]);
    sort(d, d+4);
    ans[i] =  d[0];
  }
  rep(i, Q) cout << ans[i] << endl;
  return 0;
}
