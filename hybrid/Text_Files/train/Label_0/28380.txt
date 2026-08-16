#include <bits/stdc++.h>
using namespace std;
long long n, b[150001], c[150001], a[150001], p, j;
vector<int> pr;
bool check(int X) {
  if (X == 1) return false;
  for (int i = 2; i <= n; ++i)
    if ((a[i] % X) * (b[i] % X) > 0) return false;
  return true;
}
void ktnt(int X) {
  j = 0;
  long long k = X;
  for (int i = 2; i * i <= k; ++i)
    if (k % i == 0) {
      j++, c[j] = i;
      while (k % i == 0) {
        k /= i;
      }
    }
  if (k > 1) j++, c[j] = k;
}
void run(int X) {
  ktnt(X);
  for (int i = 1; i <= j; ++i) {
    if (check(c[i])) {
      cout << c[i];
      exit(0);
    }
    if (check(X / c[i])) {
      cout << X / c[i];
      exit(0);
    }
  }
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> n;
  for (int i = 1; i <= n; ++i) cin >> a[i] >> b[i];
  run(a[1]);
  run(b[1]);
  cout << -1;
}
