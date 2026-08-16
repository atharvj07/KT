#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:16777216")
using namespace std;
template <class T>
void pv(T a, T b) {
  for (T i = a; i != b; ++i) cout << *i << " ";
  cout << endl;
}
int f[1 << 20];
int n, N, k;
struct S {
  int a, b, c;
  S() {}
  S(int a, int b, int c) : a(a), b(b), c(c) { ord(); }
  void ord() {
    if (f[a] > f[b]) swap(a, b);
    if (f[a] > f[c]) swap(a, c);
    if (f[b] > f[c]) swap(b, c);
    if (b > c) swap(b, c);
  }
  bool operator<(const S& s) const { return f[a] < f[s.a]; }
};
vector<S> v;
int main() {
  cin >> n;
  N = 3 * n;
  for (int i = 0; i < N; i++) {
    int val;
    cin >> val;
    f[val] = i;
  }
  for (int i = 0; i < n; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    v.push_back(S(a, b, c));
  }
  for (int i = 1; i < n; i++) {
    assert(v[i - 1] < v[i]);
  }
  for (int i = 0; i < n; i++) {
  }
  cin >> k;
  vector<int> res, tmp;
  for (int i = 0; i < n; i++) {
    if (v[i].a == k) {
      res.push_back(v[i].b);
      res.push_back(v[i].c);
      for (int j = i + 1; j < n; j++) {
        tmp.push_back(v[j].a);
        tmp.push_back(v[j].b);
        tmp.push_back(v[j].c);
      }
      for (int j = 0; j < i; j++) {
        if (v[j].a < v[i].c)
          res.push_back(v[j].a);
        else
          tmp.push_back(v[j].a);
        if (v[j].b < v[i].c)
          res.push_back(v[j].b);
        else
          tmp.push_back(v[j].b);
        if (v[j].c < v[i].c)
          res.push_back(v[j].c);
        else
          tmp.push_back(v[j].c);
      }
      sort(res.begin(), res.end());
      sort(tmp.begin(), tmp.end());
      for (int j = 0; j < (int)tmp.size(); j++) res.push_back(tmp[j]);
      for (int j = 1; j < N; j++) {
        if (j != 1) printf(" ");
        printf("%d", res[j - 1]);
      }
      printf("\n");
      return 0;
    }
  }
  int foi = 0;
  for (int i = 1; i <= N; i++) {
    if (i == k) continue;
    if (foi++) printf(" ");
    printf("%d", i);
  }
  printf("\n");
  return 0;
}
