#include <bits/stdc++.h>
using namespace std;
pair<int, int> ii;
long long a[11];
void init() {
  long long n = 9, ten = 10, nine = 8;
  for (int i = 1; i < 10; ++i) {
    a[i] = n;
    n = n * 10 + 9;
  }
}
int numdigit(long long n) {
  int res = 0;
  while (n) {
    ++res;
    n /= 10;
  }
  return res;
}
long long ans(long long n) {
  if (n <= 9) return n;
  long long num = numdigit(n);
  long long diff = n - a[num - 1];
  return diff * num + ans(a[num - 1]);
}
int main() {
  init();
  long long n;
  cin >> n;
  cout << ans(n);
  return 0;
}
