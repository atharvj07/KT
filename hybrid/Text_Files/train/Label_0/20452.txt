#include <bits/stdc++.h>
const int MAXN = 105;
using namespace std;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
long long last_of(long long a, long long b) {
  assert(b != 1);
  if (a % (b - 1) == 0) return a / (b - 1) - 1;
  return a / (b - 1);
}
long long cei(long long a, long long b) { return (a + b - 1) / b; }
long long n, k, h[MAXN], val[MAXN];
void solve() {
  cin >> n >> k;
  vector<long long> lb;
  vector<pair<long long, long long> > ev;
  for (int i = 1; i <= n; i++) {
    cin >> h[i];
    long long d = 1;
    while (1) {
      lb.push_back(d);
      ev.push_back(pair<long long, long long>(d, i));
      if (cei(h[i], d) == 1) {
        break;
      }
      d = last_of(h[i], cei(h[i], d)) + 1;
    }
  }
  lb.push_back(1e13);
  sort((lb).begin(), (lb).end());
  lb.resize(unique((lb).begin(), (lb).end()) - lb.begin());
  sort((ev).begin(), (ev).end());
  int ptr = 0;
  long long sum = 0, sumh = 0, ans = 1;
  for (int i = 1; i <= n; i++) {
    sumh += h[i];
  }
  for (int i = 0; i < (int)lb.size() - 1; i++) {
    long long d = lb[i], r = lb[i + 1] - 1;
    while (ptr < ev.size() && ev[ptr].first <= d) {
      int id = ev[ptr].second;
      sum -= val[id];
      val[id] = cei(h[id], d);
      sum += val[id];
      ptr++;
    }
    long long best = (k + sumh) / sum;
    if (best >= d) {
      ans = max(ans, min(best, r));
    }
  }
  cout << ans << '\n';
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int tc = 1;
  for (int i = 1; i <= tc; i++) {
    solve();
  }
  return 0;
}
