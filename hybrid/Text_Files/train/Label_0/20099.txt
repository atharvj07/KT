#include <bits/stdc++.h>
using namespace std;
const long long N = 1e6 + 5;
long long n, ans, sum, a[N];
char s[N];
inline long long read() {
  long long ret = 0, f = 0;
  char c = getchar();
  while (!isdigit(c)) {
    if (c == '-') f = 1;
    c = getchar();
  }
  while (isdigit(c)) {
    ret = ret * 10 + c - 48;
    c = getchar();
  }
  if (f) return -ret;
  return ret;
}
signed main() {
  n = read();
  scanf("%s", s + 1);
  for (long long i = 1, j = 1; i <= n; i = j + 1) {
    j = i;
    if (s[i] == '0')
      ans += sum;
    else {
      while (j + 1 <= n && s[j + 1] == s[j]) j++;
      for (long long k = i; k <= j; k++) {
        sum += k - a[k - i + 1];
        ans += sum;
      }
      for (long long k = i; k <= j; k++) a[j - k + 1] = k;
    }
  }
  cout << ans;
  return 0;
}
