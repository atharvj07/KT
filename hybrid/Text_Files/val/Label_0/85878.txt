#include <bits/stdc++.h>
using namespace std;
int n, t[100000], l[100000], L, a, s;
int main() {
  cin >> n >> L >> a;
  for (int i = 0; i < n; i++) {
    scanf("%d%d", &t[i], &l[i]);
    if (!i)
      s += t[i] / a;
    else
      s += (t[i] - (t[i - 1] + l[i - 1])) / a;
  }
  if (n == 0)
    s = L / a;
  else
    s += (L - t[n - 1] - l[n - 1]) / a;
  cout << s;
}
