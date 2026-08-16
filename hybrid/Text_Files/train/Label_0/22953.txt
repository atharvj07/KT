#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
const int N = (2e5 + 20);
using namespace std;
int xd[5];
vector<int> x1;
vector<int> x2;
vector<int> x3;
vector<int> x4;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  cin >> n;
  string s1, s2;
  cin >> s1 >> s2;
  for (int i = 0; i < n; i++) {
    if (s1[i] == '0' and s2[i] == '0') {
      xd[0]++;
      x1.push_back(i + 1);
    }
    if (s1[i] == '0' and s2[i] == '1') {
      xd[1]++;
      x2.push_back(i + 1);
    }
    if (s1[i] == '1' and s2[i] == '0') {
      xd[2]++;
      x3.push_back(i + 1);
    }
    if (s1[i] == '1' and s2[i] == '1') {
      xd[3]++;
      x4.push_back(i + 1);
    }
  }
  int a = -1, b, c, d;
  for (int i = 0; i <= xd[1]; i++) {
    for (int j = 0; j <= xd[2]; j++) {
      int u = xd[1] + xd[3] - i - j;
      int v = n / 2 - i - j - u / 2;
      if (u % 2 == 0 and u / 2 >= 0 and u / 2 <= xd[3] and v >= 0 and
          v <= xd[0]) {
        b = i;
        c = j;
        d = u / 2;
        a = v;
        break;
      }
    }
  }
  if (a == -1) {
    cout << -1 << endl;
    return 0;
  } else {
    for (int i = 0; i < a; i++) cout << x1[i] << " ";
    for (int i = 0; i < b; i++) cout << x2[i] << " ";
    for (int i = 0; i < c; i++) cout << x3[i] << " ";
    for (int i = 0; i < d; i++) cout << x4[i] << " ";
    cout << endl;
  }
  return 0;
}
