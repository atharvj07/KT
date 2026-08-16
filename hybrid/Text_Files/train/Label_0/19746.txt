#include <bits/stdc++.h>
using namespace std;
long long max(long long a, long long b) {
  if (a > b) return a;
  return b;
}
long long min(long long a, long long b) {
  if (a > b) return b;
  return a;
}
void faster() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
}
int main() {
  faster();
  long long n;
  cin >> n;
  long long cur;
  bool ok = false;
  cin >> cur;
  for (int i = 2; i <= n; i++) {
    long long x;
    cin >> x;
    if (abs(x - cur) > 1) ok = true;
    cur = x;
  }
  if (ok) {
    cout << "NO" << endl;
  } else {
    cout << "YES" << endl;
  }
  return 0;
}
