#include <bits/stdc++.h>
using namespace std;
int main() {
  string a1, a2, a, b, b1, b2, s;
  cin >> a1 >> a2 >> b1 >> b2;
  swap(a2[0], a2[1]);
  swap(b2[0], b2[1]);
  a += a1 + a2;
  b += b1 + b2;
  a.erase(a.find('X'), 1);
  b.erase(b.find('X'), 1);
  s += a + a;
  if (s.find(b) != string::npos) {
    printf("YES\n");
  } else {
    printf("NO\n");
  }
}
