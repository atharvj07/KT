#include <bits/stdc++.h>
using namespace std;
const double esp = 1e-7;
const double pi = acos(-1.0);
const int maxx = 1101000;
const int mod = int(1e9 + 7);
namespace fastIO {
bool IOerror = 0;
inline char nc() {
  static char buf[100000], *p1 = buf + 100000, *pend = buf + 100000;
  if (p1 == pend) {
    p1 = buf;
    pend = buf + fread(buf, 1, 100000, stdin);
    if (pend == p1) {
      IOerror = 1;
      return -1;
    }
  }
  return *p1++;
}
inline bool blank(char ch) {
  return ch == ' ' || ch == '\n' || ch == '\r' || ch == '\t';
}
inline void read(int &x) {
  char ch;
  while (blank(ch = nc()))
    ;
  if (IOerror) return;
  for (x = ch - '0'; (ch = nc()) >= '0' && ch <= '9'; x = x * 10 + ch - '0')
    ;
}
inline void readll(long long int &x) {
  char ch;
  while (blank(ch = nc()))
    ;
  if (IOerror) return;
  for (x = ch - '0'; (ch = nc()) >= '0' && ch <= '9'; x = x * 10 + ch - '0')
    ;
}
inline void reads(char *s) {
  char ch;
  while (blank(ch = nc()))
    ;
  if (IOerror) return;
  s[0] = ch;
  for (int i = 1; (!blank(ch = nc())); ++i) {
    s[i] = ch;
  }
}
};  // namespace fastIO
string s;
int main() {
  int n;
  scanf("%d", &n);
  cin >> s;
  int l = 0, r = 0;
  bool ans = true;
  for (int i = 0; i < n; ++i) {
    if (i) {
      if (s[i] < s[i - 1]) {
        ans = false;
        l = i - 1;
        r = i;
        break;
      }
    }
  }
  if (ans) {
    cout << "NO\n";
  } else {
    cout << "YES\n" << l + 1 << " " << r + 1 << endl;
  }
  return 0;
}
