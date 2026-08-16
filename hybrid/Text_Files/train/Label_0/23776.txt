#include <bits/stdc++.h>
using namespace std;
template <typename T>
void cmax(T& a, T b) {
  a = max(a, b);
}
template <typename T>
void cmin(T& a, T b) {
  a = min(a, b);
}
void _BG(const char* s) {}
template <typename T, typename... TT>
void _BG(const char* s, T a, TT... b) {
  for (int c = 0; *s && (c || *s != ','); ++s) {
    cerr << *s;
    switch (*s) {
      case '(':
      case '[':
      case '{':
        ++c;
        break;
      case ')':
      case ']':
      case '}':
        --c;
        break;
    }
  }
  cerr << " = " << a;
  if (*s) {
    cerr << ", ";
    _BG(++s, b...);
  } else
    cerr << endl;
}
bool RD(void) { return true; }
bool RD(char& a) { return scanf(" %c", &a) == 1; }
bool RD(char* a) { return scanf("%s", a) == 1; }
bool RD(double& a) { return scanf("%lf", &a) == 1; }
bool RD(int& a) { return scanf("%d", &a) == 1; }
bool RD(long long& a) { return scanf("%lld", &a) == 1; }
template <typename T, typename... TT>
bool RD(T& a, TT&... b) {
  return RD(a) && RD(b...);
}
void PT(const char a) { putchar(a); }
void PT(const char* a) { fputs(a, stdout); }
void PT(char* a) { fputs(a, stdout); }
void PT(const double a) { printf("%.16f", a); }
void PT(const int a) { printf("%d", a); }
void PT(const long long a) { printf("%lld", a); }
template <char sep = ' ', char end = '\n'>
void PL(void) {
  if (end) PT(end);
}
template <char sep = ' ', char end = '\n', typename T, typename... TT>
void PL(const T a, const TT... b) {
  PT(a);
  if (sizeof...(b) && sep) PT(sep);
  PL<sep, end>(b...);
}
const int N = 1e5 + 87;
pair<int, int> a[N];
int main() {
  int n;
  long long k, h = 0;
  RD(n, k);
  for (int i(0), _B(n); i < _B; ++i) {
    RD(a[i].first);
    h += a[i].first;
    a[i].second = i + 1;
  }
  if (h < k) {
    cout << "-1\n";
    return 0;
  } else if (h == k) {
    return 0;
  }
  sort(a, a + n);
  h = 0;
  int r;
  for (r = 0; r < n;) {
    long long v = (n - r) * (a[r].first - h);
    if (v <= k) {
      k -= v;
      h = a[r].first;
      while (++r < n && a[r].first == a[r - 1].first)
        ;
    } else {
      break;
    }
  }
  int m = n - r;
  for (int i(r), _B(n); i < _B; ++i) a[i].first -= h + k / m;
  k %= m;
  sort(a + r, a + n, [](pair<int, int> x, pair<int, int> y) -> bool {
    return x.second < y.second;
  });
  queue<pair<int, int> > q;
  for (int i(r), _B(n); i < _B; ++i) q.push(a[i]);
  while (k--) {
    pair<int, int> x = q.front();
    q.pop();
    if (--x.first) q.push(x);
  }
  for (; ((int)q.size()); q.pop())
    cout << q.front().second << " \n"[((int)q.size()) == 1];
}
