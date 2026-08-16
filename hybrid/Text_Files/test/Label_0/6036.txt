#include <bits/stdc++.h>
using namespace std;
int k, n, w, s, i, r;
int main() {
  cin >> k >> n >> w;
  s = 0;
  for (i = 1; i <= w; i++) s = s + (i * k);
  r = s - n;
  if (r > 0)
    cout << r;
  else
    cout << 0;
  return 0;
}
