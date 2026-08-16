#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
const int maxn = 1e6 + 5;
void go() {
  long long n;
  cin >> n;
  n /= 2;
  n += 2;
  long long a = n / 2;
  long long b = (n + 1) / 2;
  cout << (a % mod) * (b % mod) % mod << '\n';
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int c = 1;
  int t;
  if (!c) {
    t = 1;
  } else {
    cin >> t;
  }
  while (t--) {
    go();
  }
}
