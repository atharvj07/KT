#include <bits/stdc++.h>
using namespace std;
long long power(long long b, long long e) {
  long long p = 1;
  while (e > 0) {
    if (e & 1) {
      p = (p * b) % 1000000007;
    }
    e = e >> 1;
    b = (b * b) % 1000000007;
  }
  return p;
}
vector<string> num;
string s, s1;
int main() {
  long long n, i, t, x = 0, j, m, c, q, ans = 0, l;
  scanf("%lld", &n);
  cin >> s;
  for (i = 0; i < 10; i++) {
    for (j = 0; j < n; j++) {
      s1 = s;
      for (l = 0; l < n; l++) {
        s1[l] = (char)((s[(l + j) % n] - 48 + i) % 10 + 48);
      }
      num.push_back(s1);
    }
  }
  sort((num).begin(), (num).end());
  cout << num[0] << "\n";
  return 0;
}
