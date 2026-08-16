#include <bits/stdc++.h>
using namespace std;
long long int gcd(long long int a, long long int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
void solve() {
  string s1, s2;
  cin >> s1 >> s2;
  long long int n1 = s1.length() - 1, n2 = s2.length() - 1;
  long long int count1 = 0;
  while (n1 >= 0 && n2 >= 0 && s1[n1] == s2[n2]) {
    count1 += 2;
    n1--;
    n2--;
  }
  n1 = s1.length();
  n2 = s2.length();
  cout << (n1 + n2 - count1) << endl;
}
int main() {
  int t;
  t = 1;
  while (t--) {
    solve();
  }
}
