#include <bits/stdc++.h>
using namespace std;
string getString(long long n) {
  string k;
  while (n != 0) {
    k += (n % 10) + '0';
    n /= 10;
  }
  reverse(k.begin(), k.end());
  return k;
}
long getSo(string a) {
  long long x = 0;
  for (int i = 0; i < a.length(); i++) {
    x = x * 10 + (a[i] - '0');
  }
  return x;
}
using namespace std;
int main() {
  long long a;
  cin >> a;
  long long b;
  cin >> b;
  int k = a + b;
  string a1 = getString(a);
  string b1 = getString(b);
  string c1 = getString(k);
  string a2, b2, c2;
  for (int i = 0; i < a1.length(); i++) {
    if (a1[i] == '0') {
      continue;
    }
    a2 += a1[i];
  }
  for (int i = 0; i < b1.length(); i++) {
    if (b1[i] == '0') {
      continue;
    }
    b2 += b1[i];
  }
  for (int i = 0; i < c1.length(); i++) {
    if (c1[i] == '0') {
      continue;
    }
    c2 += c1[i];
  }
  long long x1 = getSo(a2);
  long long x2 = getSo(b2);
  long long x3 = getSo(c2);
  if (x1 + x2 == x3)
    cout << "YES" << endl;
  else
    cout << "NO" << endl;
}
