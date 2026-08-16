#include <bits/stdc++.h>
using namespace std;
template <class T>
bool chmax(T &a, const T &b) {
  if (a < b) {
    a = b;
    return 1;
  }
  return 0;
}
template <class T>
bool chmin(T &a, const T &b) {
  if (a > b) {
    a = b;
    return 1;
  }
  return 0;
}
template <class T>
ostream &operator<<(ostream &os, const vector<T> &t) {
  os << "[";
  for (__typeof((t).begin()) it = (t).begin(); it != (t).end(); it++) {
    if (it != t.begin()) os << ",";
    os << *it;
  }
  os << "]";
  return os;
}
template <class T>
ostream &operator<<(ostream &os, const set<T> &t) {
  os << "{";
  for (__typeof((t).begin()) it = (t).begin(); it != (t).end(); it++) {
    if (it != t.begin()) os << ",";
    os << *it;
  }
  os << "}";
  return os;
}
template <class S, class T>
ostream &operator<<(ostream &os, const pair<S, T> &t) {
  return os << "(" << t.first << "," << t.second << ")";
}
const int INF = 1 << 28;
const double EPS = 1e-8;
const int MOD = 1000000007;
long long int t, a, b;
long double x[2][60];
long long int dfs(int co, long long int re1, long long int re2) {
  if (co == 1) {
    if (t == a || (re1 - re2) % (t - a)) return 0;
    long long int i = (re1 - re2) / (t - a);
    return !(re1 - i * t < 0 || re2 - i * a < 0 || i < 0);
  }
  long long int ans = 0;
  while (re1 >= 0 && re2 >= 0) {
    ans += dfs(co - 1, re1, re2);
    re1 -= x[0][co];
    re2 -= x[1][co];
  }
  return ans;
}
int main() {
  cin >> t >> a >> b;
  if (t == 1 && a == 1 && b == 1) {
    puts("inf");
    return 0;
  }
  if (t == a && a == b) {
    puts("2");
    return 0;
  }
  if (t == a) {
    puts("0");
    return 0;
  }
  for (long long int i = 0; i < (long long int)(60); i++) {
    x[0][i] = powl(t, i);
    x[1][i] = powl(a, i);
  }
  cout << dfs(59, a, b) << endl;
  return 0;
}
