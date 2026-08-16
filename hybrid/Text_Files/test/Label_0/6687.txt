#include <bits/stdc++.h>
using namespace std;
void __print(int x) { cerr << x; }
void __print(long x) { cerr << x; }
void __print(long long x) { cerr << x; }
void __print(unsigned x) { cerr << x; }
void __print(unsigned long x) { cerr << x; }
void __print(unsigned long long x) { cerr << x; }
void __print(float x) { cerr << x; }
void __print(double x) { cerr << x; }
void __print(long double x) { cerr << x; }
void __print(char x) { cerr << '\'' << x << '\''; }
void __print(const char *x) { cerr << '\"' << x << '\"'; }
void __print(const string &x) { cerr << '\"' << x << '\"'; }
void __print(bool x) { cerr << (x ? "true" : "false"); }
template <typename T, typename V>
void __print(const pair<T, V> &x) {
  cerr << '{';
  __print(x.first);
  cerr << ',';
  __print(x.second);
  cerr << '}';
}
template <typename T>
void __print(const T &x) {
  int f = 0;
  cerr << '{';
  for (auto &i : x) cerr << (f++ ? "," : ""), __print(i);
  cerr << "}";
}
void _print() { cerr << "]\n"; }
template <typename T, typename... V>
void _print(T t, V... v) {
  __print(t);
  if (sizeof...(v)) cerr << ", ";
  _print(v...);
}
const int N = 2e5 + 10;
const int mod = 1e9 + 7;
int dp[N][2];
int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  int mx = 1;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    if (i == 0) {
      dp[i][0] = dp[i][1] = 1;
      continue;
    }
    if (a[i] > a[i - 1]) {
      dp[i][0] = dp[i - 1][0] + 1;
      dp[i][1] = max(dp[i - 1][1] + 1,
                     (i > 1 and a[i] > a[i - 2]) ? dp[i - 2][0] + 1 : 1);
    } else {
      dp[i][0] = 1;
      if (i > 1 and a[i] > a[i - 2]) {
        dp[i][1] = dp[i - 2][0] + 1;
      } else {
        dp[i][1] = 1;
      }
    }
    mx = max({dp[i][0], dp[i][1], mx});
  }
  cout << mx << endl;
}
