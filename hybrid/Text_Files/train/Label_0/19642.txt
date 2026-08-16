#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const long long LINF = 0x3f3f3f3f3f3f3f3f;
template <typename T, typename T2>
inline void _max(T &a, T2 b) {
  a = max((T)a, (T)b);
}
template <typename T, typename T2>
inline void _min(T &a, T2 b) {
  a = min((T)a, (T)b);
}
const int MAX = 3e5 + 10;
int n, m;
string s[MAX];
void clear() {}
void read() {
  for (int i = 0; i < n; i++) cin >> s[i];
}
void solve() {
  vector<char> v = {'A', 'C', 'T', 'G'};
  sort(v.begin(), v.end());
  int res = INF;
  vector<char> best;
  bool isHor = false;
  do {
    int tres = 0;
    for (int i = 0; i < n; i++) {
      vector<char> line = {v[i % 2], v[i % 2 + 2]};
      int ts1 = 0, ts2 = 0;
      for (int j = 0; j < m; j++) ts1 += line[j & 1] != s[i][j];
      swap(line[0], line[1]);
      for (int j = 0; j < m; j++) ts2 += line[j & 1] != s[i][j];
      tres += min(ts1, ts2);
    }
    if (tres < res) {
      res = tres;
      best = v;
      isHor = 1;
    }
    tres = 0;
    for (int j = 0; j < m; j++) {
      vector<char> line = {v[j % 2], v[j % 2 + 2]};
      int ts1 = 0, ts2 = 0;
      for (int i = 0; i < n; i++) ts1 += line[i & 1] != s[i][j];
      swap(line[0], line[1]);
      for (int i = 0; i < n; i++) ts2 += line[i & 1] != s[i][j];
      tres += min(ts1, ts2);
    }
    if (tres < res) {
      res = tres;
      best = v;
      isHor = 0;
    }
  } while (next_permutation(v.begin(), v.end()));
  v = best;
  vector<string> rs(n, string(m, '0'));
  if (isHor) {
    for (int i = 0; i < n; i++) {
      vector<char> line = {v[i % 2], v[i % 2 + 2]};
      int ts1 = 0, ts2 = 0;
      for (int j = 0; j < m; j++) ts1 += line[j & 1] != s[i][j];
      swap(line[0], line[1]);
      for (int j = 0; j < m; j++) ts2 += line[j & 1] != s[i][j];
      if (ts1 < ts2) swap(line[0], line[1]);
      for (int j = 0; j < m; j++) rs[i][j] = line[j & 1];
    }
  } else {
    for (int j = 0; j < m; j++) {
      vector<char> line = {v[j % 2], v[j % 2 + 2]};
      int ts1 = 0, ts2 = 0;
      for (int i = 0; i < n; i++) ts1 += line[i & 1] != s[i][j];
      swap(line[0], line[1]);
      for (int i = 0; i < n; i++) ts2 += line[i & 1] != s[i][j];
      if (ts1 < ts2) swap(line[0], line[1]);
      for (int i = 0; i < n; i++) rs[i][j] = line[i & 1];
    }
  }
  for (int i = 0; i < n; i++) cout << rs[i] << "\n";
}
int main() {
  while (scanf("%d%d", &n, &m) == 2) {
    clear();
    read();
    solve();
    return 0;
  }
  return 0;
}
