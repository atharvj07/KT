#include <bits/stdc++.h>
using namespace std;
template <typename T>
void out(T x) {
  cout << x << endl;
  exit(0);
}
const int maxn = 1e6 + 5;
int n, k;
vector<string> s;
bool test(string x) {
  for (int i = 0; i < n; i++) {
    int cnt = 0;
    map<char, int> freq;
    for (int j = 0; j < k; j++) {
      freq[s[i][j]]++;
      cnt += x[j] != s[i][j];
    }
    bool same = false;
    for (auto p : freq) {
      if (p.second > 1) same = true;
    }
    if (cnt == 2) continue;
    if (cnt == 0 && same) continue;
    return false;
  }
  return true;
}
void check() {
  string res = s[0];
  sort(res.begin(), res.end());
  for (string x : s) {
    sort(x.begin(), x.end());
    if (x != res) out(-1);
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> k;
  s.resize(n);
  for (int i = 0; i < n; i++) {
    cin >> s[i];
  }
  sort(s.begin(), s.end());
  s.erase(unique(s.begin(), s.end()), s.end());
  n = s.size();
  if (int(s.size()) == 1) {
    swap(s[0][0], s[0][1]);
    cout << s[0] << endl;
    return 0;
  }
  check();
  vector<int> difs;
  for (int i = 0; i < k; i++) {
    if (s[0][i] != s[1][i]) difs.push_back(i);
  }
  if ((int)difs.size() > 4) out(-1);
  for (int x : difs) {
    for (int i = 0; i < k; i++) {
      string f = s[0];
      swap(f[i], f[x]);
      if (test(f)) {
        out(f);
      }
    }
  }
  out(-1);
  return 0;
}
