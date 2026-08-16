#include <bits/stdc++.h>
using namespace std;
long long in() {
  int32_t x;
  scanf("%d", &x);
  return x;
}
inline long long lin() {
  long long x;
  scanf("%lld", &x);
  return x;
}
const long long maxn = 2e5 + 10;
const long long mod = 1e9 + 7;
map<long long, long long> mp, where;
long long fen[maxn];
inline long long get_num(long long x) {
  return mp.find(x) == mp.end() ? x : mp[x];
}
long long res;
inline long long get(long long x) {
  long long ret = 0;
  for (x++; x > 0; x -= x & -x) ret += fen[x];
  return ret;
}
vector<long long> fuck;
inline void update(long long x, long long val) {
  for (x++; x < maxn; x += x & -x) fen[x] += val;
}
inline long long get_interval(long long l, long long r) {
  return upper_bound(fuck.begin(), fuck.end(), r) -
         lower_bound(fuck.begin(), fuck.end(), l);
}
int32_t main() {
  long long n = in();
  for (long long i = 0; i < n; i++) {
    long long a = in(), b = in();
    long long A = get_num(a), B = get_num(b);
    mp[a] = B, mp[b] = A;
    where[A] = b, where[B] = a;
  }
  long long cur = 0;
  vector<pair<long long, long long> > vc;
  for (auto it : mp) {
    vc.push_back({it.second, cur++});
    fuck.push_back(it.first);
  }
  sort(fuck.begin(), fuck.end());
  sort(vc.begin(), vc.end());
  for (long long i = 0; i < vc.size(); i++) {
    res += i - get(vc[i].second);
    update(vc[i].second, 1);
  }
  for (long long i = 0; i < vc.size(); i++) {
    long long www = where[vc[i].first];
    if (www < vc[i].first) {
      res += vc[i].first - www + 1 - get_interval(www, vc[i].first);
    } else {
      res += www - vc[i].first + 1 - get_interval(vc[i].first, www);
    }
  }
  cout << res << endl;
}
