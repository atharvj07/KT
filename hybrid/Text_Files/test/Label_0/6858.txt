#include <bits/stdc++.h>
using namespace std;
const long long mxn = 1e5 + 1;
const long long mod = 1073741824;
bool sortbysec(const pair<int, int> &a, const pair<int, int> &b) {
  return (a.second < b.second);
}
long long divi[1000001];
void solve() {
  long long a, b, c;
  cin >> a >> b >> c;
  long long sum = 0;
  for (int i = 1; i <= a; i++) {
    for (int j = 1; j <= b; j++) {
      for (int k = 1; k <= c; k++) {
        sum = (sum % mod + divi[i * j * k] % mod) % mod;
      }
    }
  }
  cout << sum << '\n';
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  ;
  long long n = 1e6;
  for (long long i = 1; i <= n; i++) {
    for (long long j = 1; j * i <= n; j++) divi[i * j]++;
  }
  solve();
  return 0;
}
