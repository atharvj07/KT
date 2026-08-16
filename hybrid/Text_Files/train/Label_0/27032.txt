#include <bits/stdc++.h>
using namespace std;
long long poww(long long A, long long B, long long P) {
  if (!B) return 1;
  long long h = poww(A, B / 2, P);
  h *= h;
  h %= P;
  if (B % 2) h *= A;
  return h % P;
}
long long gcd(long long A, long long B) {
  return A > B ? gcd(B, A) : A ? gcd(B % A, A) : B;
}
string s;
int n, i;
int main() {
  cin >> s;
  swap(s[2], s[1]);
  swap(s[2], s[4]);
  n = 0;
  for (i = 0; i < s.size(); i++) n = n * 10 + s[i] - '0';
  {
    n = poww(n, 5, 100000);
    if (n < 10000) cout << 0;
    if (n < 1000) cout << 0;
    if (n < 100) cout << 0;
    if (n < 10) cout << 0;
    cout << n << endl;
  }
}
