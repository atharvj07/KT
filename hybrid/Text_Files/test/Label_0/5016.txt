#include <bits/stdc++.h>
using namespace std;
const int N = 1E6;
char arr[N];
long long s[N];
void solve() {
  long long n, m;
  cin >> n >> m;
  scanf("%s", arr + 1);
  long long pos = 1;
  for (long long i = 1; i <= n; i++) {
    if (arr[i] == '0') {
      s[pos++] = i;
    }
  }
  long long ans = 0;
  for (long long i = 1; i < pos; i++) {
    if (ans + s[i] - i <= m) {
      arr[s[i]] = '1';
      arr[i] = '0';
      ans += s[i] - i;
    } else {
      arr[s[i]] = '1';
      arr[s[i] + ans - m] = '0';
      break;
    }
  }
  puts(arr + 1);
}
int main() {
  int t;
  scanf("%d", &t);
  while (t--) solve();
  return 0;
}
