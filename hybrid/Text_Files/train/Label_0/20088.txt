#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100001;
int arr[MAXN];
set<int> mp[MAXN];
map<int, int> loga[MAXN];
void add(int a, int b, int x) {
  for (int i = a + 1; i < MAXN; i += i & -i)
    for (int j = b + 1; j < MAXN; j += j & -j) loga[i][j] += x;
}
long long get(int a, int b) {
  long long ret = 0;
  for (int i = a + 1; i; i -= i & -i)
    for (int j = b + 1; j; j -= j & -j)
      if (loga[i].count(j)) ret += loga[i][j];
  return ret;
}
void remove(int i) {
  auto& s = mp[arr[i]];
  auto it = s.find(i);
  if (it != s.begin()) add(*prev(it), *it, *prev(it) - *it);
  if (next(it) != s.end()) add(*it, *next(it), *it - *next(it));
  if (it != s.begin() && next(it) != s.end())
    add(*prev(it), *next(it), *next(it) - *prev(it));
  s.erase(it);
}
void insert(int i) {
  auto& s = mp[arr[i]];
  auto it = s.insert(i).first;
  if (it != s.begin()) add(*prev(it), *it, *it - *prev(it));
  if (next(it) != s.end()) add(*it, *next(it), *next(it) - *it);
  if (it != s.begin() && next(it) != s.end())
    add(*prev(it), *next(it), *prev(it) - *next(it));
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, i;
  cin >> n >> m;
  for (i = 0; i < n; ++i) {
    cin >> arr[i];
    mp[arr[i]].insert(i);
  }
  for (const auto& x : mp)
    if (!x.empty()) {
      for (auto it = next(x.begin()); it != x.end(); ++it) {
        add(*prev(it), *it, *it - *prev(it));
      }
    }
  while (m--) {
    int q, a, b;
    cin >> q >> a >> b;
    --a;
    if (q == 1) {
      remove(a);
      arr[a] = b;
      insert(a);
    } else {
      --a, --b;
      cout << get(b, b) - get(a, b) - get(b, a) + get(a, a) << '\n';
    }
  }
}
