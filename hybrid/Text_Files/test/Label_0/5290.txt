#include <bits/stdc++.h>
using namespace std;
int main() {
  float k, n, s, p;
  cin >> k >> n >> s >> p;
  int reqSheet = ceil(n / s);
  int total = reqSheet * k;
  int ans = ceil(total / p);
  cout << ans;
}
