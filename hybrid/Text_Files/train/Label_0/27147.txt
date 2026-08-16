#include <bits/stdc++.h>
using namespace std;
int n, m, a, b, c, d;
struct node {
  int a, b;
};
bool cmp(node x, node y) {
  if (x.a == y.a) return x.b > y.b;
  return x.a > y.a;
}
string s;
int num[30];
char cr, cr1;
int check(char cc) {
  for (int i = cc - 'a' + 1; i < 26; ++i) {
    if (num[i]) return num[i];
  }
  return 0;
}
int main() {
  cin >> n;
  getchar();
  while ((cr = getchar()) && cr != '\n') {
    m++;
    if (!num[cr - 'a']) {
      num[cr - 'a'] = m;
    }
    if (check(cr)) {
      cout << "YES" << endl;
      cout << check(cr) << " " << m << endl;
      return 0;
    }
  }
  cout << "NO" << endl;
  return 0;
}
