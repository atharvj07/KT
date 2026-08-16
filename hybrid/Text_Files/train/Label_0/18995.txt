#include <bits/stdc++.h>
using namespace std;
void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
}
long long int gcd(long long int x, long long int y) {
  if (y == 0) return x;
  return gcd(y, x % y);
}
long long int lcm(long long int a, long long int b) {
  return (a * b) / gcd(a, b);
}
long long int logx(long long int base, long long int num) {
  int cnt = 0;
  while (num != 1) {
    num /= base;
    ++cnt;
  }
  return cnt;
}
vector<long long int> vin(long long int n) {
  vector<long long int> a(n);
  for (long long int i = 0; i < n; i++) cin >> a[i];
  return a;
}
void in(long long int *a, long long int n) {
  for (long long int i = 0; i < n; i++) cin >> a[i];
}
void out(long long int *a, long long int n) {
  for (long long int i = 0; i < n; i++) {
    cout << a[i] << " ";
  }
  cout << '\n';
}
void vout(vector<long long int> v) {
  for (long long int i = 0; i < (long long int)v.size(); i++) {
    cout << v[i] << " ";
  }
  cout << endl;
}
const long long int maxN = (long long int)(1 * 1e6 + 7);
vector<long long int> a(maxN);
void solve() {
  long long int n, x;
  cin >> n >> x;
  for (long long int i = 1; i <= 9; i++) {
    a[0] = i;
    long long int c = 0;
    for (long long int j = 1; j <= n; j++) {
      a[j] = (a[j - 1] * x + c) % 10;
      c = (a[j - 1] * x + c) / 10;
    }
    if (a[n] == i && c == 0 && a[n - 1] != 0) {
      for (long long int j = n - 1; j >= 0; j--) {
        cout << a[j];
      }
      cout << '\n';
      return;
    }
  }
  cout << "Impossible\n";
}
int main() {
  fast();
  long long int t = 1;
  while (t--) {
    solve();
  }
  return 0;
}
