#include <bits/stdc++.h>
using namespace std;
int ara[120];
int main() {
  vector<int> v;
  long long int a, b, c, d, e, f, g, i, j, sum = 0, mn = 0, rr = 0, uu = 0;
  string s;
  cin >> a;
  cin >> s;
  for (i = 0; i < a - 3; i++) {
    if (s[i] >= 'A') {
      d = s[i] - 'A';
      e = 'Z' - s[i] + 1;
      mn = min(d, e);
    }
    sum = sum + mn;
    uu = 10000;
    rr = 10000;
    if (s[i + 1] >= 'C') {
      d = s[i + 1] - 'C';
      e = ('C' - 'A') + ('Z' - s[i + 1]) + 1;
      rr = min(d, e);
    } else {
      d = 'C' - s[i + 1];
      e = (s[i + 1] - 'A') + 1 + ('Z' - 'C');
      uu = min(d, e);
    }
    sum = sum + min(uu, rr);
    uu = 10000;
    rr = 10000;
    if (s[i + 2] >= 'T') {
      d = s[i + 2] - 'T';
      e = ('T' - 'A') + ('Z' - s[i + 2]) + 1;
      rr = min(d, e);
    } else {
      d = 'T' - s[i + 2];
      e = (s[i + 2] - 'A') + 1 + ('Z' - 'T');
      uu = min(d, e);
    }
    sum = sum + min(uu, rr);
    uu = 10000;
    rr = 10000;
    if (s[i + 3] >= 'G') {
      d = s[i + 3] - 'G';
      e = ('G' - 'A') + ('Z' - s[i + 3]) + 1;
      rr = min(d, e);
    } else {
      d = 'G' - s[i + 3];
      e = (s[i + 3] - 'A') + 1 + ('Z' - 'G');
      uu = min(d, e);
    }
    sum = sum + min(uu, rr);
    v.push_back(sum);
    sum = 0;
  }
  sort(v.begin(), v.end());
  cout << v[0];
  return 0;
}
