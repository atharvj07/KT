#include <bits/stdc++.h>
using namespace std;
long long n, a[1000005], as, bs, cs, ds;
long long f[5];
char ch[1000005];
int main() {
  cin >> n;
  for (int i = 0; i < n; i++) cin >> ch[i];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    if (ch[i] == 'h') f[1] += a[i];
    if (ch[i] == 'a') f[2] = min(f[1], f[2] + a[i]);
    if (ch[i] == 'r') f[3] = min(f[2], f[3] + a[i]);
    if (ch[i] == 'd') f[4] = min(f[3], f[4] + a[i]);
  }
  cout << f[4];
  return 0;
}
