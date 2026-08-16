#include <bits/stdc++.h>
using namespace std;
template <class T>
bool setmax(T &_a, T _b) {
  if (_b > _a) {
    _a = _b;
    return true;
  }
  return false;
}
template <class T>
bool setmin(T &_a, T _b) {
  if (_b < _a) {
    _a = _b;
    return true;
  }
  return false;
}
template <class T>
T gcd(T _a, T _b) {
  return _b == 0 ? _a : gcd(_b, _a % _b);
}
struct Base {
  bitset<2000> a, id;
  int first;
  void make_first() {
    assert(a.any());
    first = 0;
    while (a[first] == 0) ++first;
  }
};
vector<Base> bases;
bitset<2000> translate(string s) {
  vector<int> xs;
  reverse(s.begin(), s.end());
  for (char c : s) xs.push_back(int(c - '0'));
  bitset<2000> ans;
  for (int i = 0; i < 2000; i += 20) {
    int r = 0;
    for (int j = int((xs.size()) - 1); j >= int(0); --j) {
      xs[j] += r * 10;
      r = xs[j] & ((1 << 20) - 1);
      xs[j] >>= 20;
    }
    for (int j = i; r > 0; ++j, r >>= 1) ans[j] = r & 1;
    while (xs.size() > 0 && xs.back() == 0) xs.pop_back();
    if (xs.empty()) break;
  }
  return ans;
}
void reduce(Base &y, const Base &x) {
  if (y.a.test(x.first)) {
    y.a ^= x.a;
    y.id ^= x.id;
  }
}
void go(bitset<2000> bits, int id) {
  Base cur;
  cur.a = bits;
  cur.id[id] = 1;
  for (Base &b : bases) reduce(cur, b);
  if (cur.a.any()) {
    printf("0\n");
    cur.make_first();
    for (Base &b : bases) reduce(b, cur);
    bases.push_back(cur);
  } else {
    cur.id[id] = 0;
    vector<int> ans;
    for (int i = int(0); i <= int((2000) - 1); ++i)
      if (cur.id.test(i)) ans.push_back(i);
    printf("%d", (int)ans.size());
    for (int x : ans) printf(" %d", x);
    printf("\n");
  }
}
int main() {
  int n;
  scanf("%d", &n);
  bases.clear();
  for (int i = int(0); i <= int((n)-1); ++i) {
    char buf[999];
    scanf("%s", buf);
    bitset<2000> cur = translate(buf);
    go(cur, i);
  }
  return 0;
}
