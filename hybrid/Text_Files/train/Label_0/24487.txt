#include <bits/stdc++.h>
using namespace std;
template <class t>
t mag(t a) {
  return a > 0 ? a : -a;
}
template <class T, class U>
T cdiv(T num, U den) {
  return (num / den) + ((num % den) > 0);
}
std::ifstream term("/dev/tty");
std::string tempstring;
using ll = int_fast64_t;
using ii = pair<int, int>;
using vi = vector<int>;
using vl = vector<ll>;
using vii = vector<ii>;
const int sij = 400010;
const ll mod = 1000000007ll;
ll n, k;
vl vec;
map<ll, ll> mp;
int esc(int tcase) {
  cin >> n >> k;
  vec.resize(n);
  for (auto &e : vec) cin >> e;
  int md = n / 2;
  ll cur = 0;
  for (auto i = 0; i != n; i++) {
    cur += mag(vec[i] - vec[md]);
  }
  if (cur <= k) {
    cout << 0 << '\n';
    return 0;
  }
  for (auto &e : vec) {
    mp[e]++;
  };
  if (mp.size() == 2) {
    ll maxi = prev(mp.end())->first, mini = mp.begin()->first;
    if (prev(mp.end())->second > mp.begin()->first) {
      maxi -= (k / prev(mp.end())->second);
      cout << maxi - mini << '\n';
      return 0;
    } else {
      mini += (k / mp.begin()->second);
      cout << maxi - mini << '\n';
      return 0;
    }
  }
  ll rem = k;
  while (1) {
    ;
    auto lst = prev(mp.end());
    auto beg = mp.begin();
    ;
    if (lst == beg) {
      cout << 0;
      return 0;
    }
    if ((rem / lst->second) == 0 and (rem / beg->second) == 0) {
      cout << lst->first - beg->first << '\n';
      return 0;
    }
    if (lst->second < beg->second) {
      auto plst = prev(prev(mp.end()));
      ;
      if ((lst->first - plst->first) * lst->second <= rem) {
        plst->second += lst->second;
        rem -= (lst->first - plst->first) * lst->second;
        mp.erase(prev(mp.end()));
        continue;
      } else {
        ll maxi = (lst->first) - (rem / lst->second);
        cout << maxi - beg->first << '\n';
        return 0;
      }
    } else {
      auto nxt = next(mp.begin());
      ;
      if ((nxt->first - beg->first) * beg->second <= rem) {
        nxt->second += beg->second;
        rem -= (nxt->first - beg->first) * beg->second;
        mp.erase(beg);
        continue;
      } else {
        ll mini = (beg->first) + (rem / beg->second);
        cout << lst->first - mini << '\n';
        return 0;
      }
    }
  }
  return 0;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int tc = 1;
  for (int i = 1; i <= tc; i++) esc(i);
}
