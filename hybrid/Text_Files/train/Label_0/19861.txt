#include <bits/stdc++.h>
using namespace std;
int const MAX = 1000 * 1000 + 41;
int n, m, k;
string s, t;
vector<int> buildpf(string s) {
  int n = (int)s.size();
  vector<int> res(n, 0);
  for (int i = 1; i <= n - 1; i++) {
    int cur = res[i - 1];
    while (cur > 0 && s[cur] != s[i]) {
      cur = res[cur - 1];
    }
    if (s[cur] == s[i]) cur++;
    res[i] = cur;
  }
  return res;
}
string rev(string s) {
  reverse(s.begin(), s.end());
  return s;
}
int f1[MAX], f2[MAX];
void solve() {
  string s1 = t.substr(0, min(k, m));
  s1 += "#";
  s1 += s;
  vector<int> p1 = buildpf(s1);
  while (false) {
  };
  for (int i = 0; i <= (int)p1.size() - 1; i++) {
    while (false) {
    };
  }
  while (false) {
  };
  string tr = rev(t);
  string sr = rev(s);
  string s2 = tr.substr(0, min(k, m));
  s2 += "#";
  s2 += sr;
  vector<int> p2 = buildpf(s2);
  while (false) {
  };
  for (int i = 0; i <= (int)p2.size() - 1; i++) {
    while (false) {
    };
  }
  while (false) {
  };
  memset(f1, 255, sizeof(f1));
  int st1 = min(m, k) + 1;
  for (int i = min(m, k) + k; i <= (int)s1.size() - 1; i++) {
    int cur = p1[i];
    while (1) {
      if (f1[cur] != -1) break;
      f1[cur] = i - st1;
      if (cur == 0) break;
      cur = p1[cur - 1];
    }
  }
  for (int i = 0; i <= (int)s1.size() - 1; i++) {
    while (false) {
    };
  }
  while (false) {
  };
  memset(f2, 255, sizeof(f2));
  int st2 = min(m, k) + 1;
  for (int i = min(m, k) + k; i <= (int)s2.size() - 1; i++) {
    int cur = p2[i];
    while (1) {
      if (f2[cur] != -1) break;
      f2[cur] = n - 1 - (i - st2);
      if (cur == 0) break;
      cur = p2[cur - 1];
    }
  }
  for (int i = 0; i <= (int)s2.size() - 1; i++) {
    while (false) {
    };
  }
  while (false) {
  };
  for (int i = min(k, m) + 1; i <= (int)s1.size() - 1; i++) {
    if (p1[i] < m) continue;
    int x = max(i, min(k, m) + k);
    if ((int)s1.size() - x < k) continue;
    int l = x - min(k, m) - k + 1;
    int r = l + k;
    printf("Yes\n%d %d\n", l, r);
    exit(0);
  }
  for (int i = min(k, m) + 1; i <= (int)s1.size() - 1; i++) {
    if (p1[i] < m) continue;
    int r = min(i - m + 1, (int)s1.size() - k) - min(m, k);
    if (r <= k) continue;
    int l = 1;
    printf("Yes\n%d %d\n", l, r);
    exit(0);
  }
  for (int i = 0; i <= min(k, m); i++) {
    if (f1[i] == -1) continue;
    if (f2[m - i] == -1) continue;
    if (f1[i] < f2[m - i]) {
      int l = f1[i] - k + 1 + 1;
      int r = f2[m - i] + 1;
      printf("Yes\n%d %d\n", l, r);
      exit(0);
    }
  }
  printf("No\n");
}
int main() {
  cin >> n >> m >> k;
  cin >> s;
  cin >> t;
  solve();
  return 0;
}
