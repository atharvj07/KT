#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5 + 5;
const int mod = 1e9 + 9;
map<pair<int, int>, int> mp;
pair<int, int> p[MAXN];
set<int> st;
int num[MAXN];
long long fast_pow(long long x, int n) {
  long long ret = 1;
  while (n) {
    if (n & 1) {
      ret = ret * x % mod;
    }
    x = x * x % mod;
    n >>= 1;
  }
  return ret;
}
bool check(int k) {
  int x = p[k].first, y = p[k].second;
  for (int i = -1; i < 2; ++i) {
    int tmp = mp[pair<int, int>(x + i, y + 1)];
    if (tmp && num[tmp] == 1) return false;
  }
  return true;
}
void add(int k) {
  int x = p[k].first, y = p[k].second;
  for (int i = -1; i < 2; ++i) {
    int tmp = mp[pair<int, int>(x + i, y - 1)];
    if (tmp && ~num[tmp] && check(tmp)) {
      st.insert(tmp);
    }
  }
}
void change(int k) {
  int x = p[k].first, y = p[k].second;
  for (int i = -1; i < 2; ++i) {
    int tmp = mp[pair<int, int>(x + i, y - 1)];
    if (tmp && ~num[tmp]) {
      set<int>::iterator it = st.lower_bound(tmp);
      if (*it == tmp) {
        st.erase(it);
      }
    }
  }
}
int main() {
  int n;
  while (~scanf("%d", &n)) {
    long long ans = 0;
    mp.clear();
    for (int i = 1; i <= n; ++i) {
      num[i] = 0;
      scanf("%d%d", &p[i].first, &p[i].second);
      mp[pair<int, int>(p[i].first, p[i].second)] = i;
    }
    for (int i = 1; i <= n; ++i) {
      int x = p[i].first, y = p[i].second;
      for (int j = -1; j < 2; ++j) {
        int tmp = mp[pair<int, int>(x + j, y + 1)];
        if (tmp) {
          ++num[tmp];
        }
      }
    }
    for (int i = 1; i <= n; ++i) {
      if (check(i)) {
        st.insert(i);
      }
    }
    int turn = 0, now = n - 1;
    while (!st.empty()) {
      set<int>::iterator it = turn ? st.begin() : --st.end();
      int m = *it;
      ans = (ans + (m - 1) * fast_pow(n, now--) % mod) % mod;
      num[m] = -1;
      int x = p[m].first, y = p[m].second;
      st.erase(it);
      for (int i = -1; i < 2; ++i) {
        int tmp = mp[pair<int, int>(x + i, y + 1)];
        if (tmp && ~num[tmp] && --num[tmp] == 1) {
          change(tmp);
        }
      }
      add(m);
      turn ^= 1;
    }
    printf("%I64d\n", ans);
  }
  return 0;
}
