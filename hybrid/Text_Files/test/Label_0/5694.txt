#include <bits/stdc++.h>
using namespace std;
int n, dem;
bool f[102];
int main() {
  cin >> n;
  int l, r, a, b, fi;
  cin >> a >> b;
  fi = a;
  if (n == 1) {
    cout << b - a;
    return 0;
  }
  for (int i = 2; i <= n; i++) {
    cin >> l >> r;
    for (int j = l; j <= r - 1; j++) f[j] = true;
  }
  f[b] = true;
  while (true) {
    if (a > b) break;
    while (f[a] == false) a++;
    dem += (a - fi);
    a++;
    fi = a;
  }
  cout << dem;
}
