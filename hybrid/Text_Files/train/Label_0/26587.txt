#include <bits/stdc++.h>
#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
using namespace std;
int main() {
  ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
  string a, b;
  cin >> a >> b;
  reverse(a.begin(), a.end());
  reverse(b.begin(), b.end());
  int i = 0, j = 0;
  int n = a.size(), m = b.size();
  int len = 0;
  while (i < n && j < m) {
    if (a[i] != b[j]) break;
    ++i;
    ++j;
  }
  cout << n - i + m - j;
  return 0;
}
