#include <bits/stdc++.h>
using namespace std;
long long nMod = 1e9 + 7;
inline long long GCD(long long a, long long b) {
  while (b != 0) {
    long long c = a % b;
    a = b;
    b = c;
  }
  return a;
};
inline long long LCM(long long a, long long b) { return (a / GCD(a, b)) * b; };
int m, n, k;
vector<set<int>> st(55);
void vietnakid() {
  cin >> m >> n;
  for (int i = 0; i < m; i++) {
    cin >> k;
    for (int j = 0; j < k; j++) {
      int x;
      cin >> x;
      st[i].insert(x);
    }
  }
  bool check = true;
  for (int i = 0; i < m; i++) {
    if (!check) break;
    for (int j = 0; j < m; j++) {
      bool ok = false;
      for (auto x : st[i]) {
        if (ok) break;
        if (st[j].count(x)) {
          ok = true;
        }
      }
      if (!ok) {
        check = false;
        break;
      }
    }
  }
  if (check) {
    cout << "possible\n";
  } else {
    cout << "impossible\n";
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie();
  vietnakid();
  cerr << "\nTime elapsed: " << 1000 * clock() / CLOCKS_PER_SEC << "ms\n";
  return 0;
}
