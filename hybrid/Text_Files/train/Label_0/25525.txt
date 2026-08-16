#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;
inline int pt(int a[], int l, int r) {
  int p, i, j;
  p = a[l];
  i = l;
  j = r + 1;
  for (;;) {
    while (a[++i] < p)
      if (i >= r) break;
    while (a[--j] > p)
      if (j <= l) break;
    if (i >= j)
      break;
    else
      swap(a[i], a[j]);
  }
  if (j == l) return j;
  swap(a[l], a[j]);
  return j;
}
inline void q_sort(int a[], int l, int r) {
  int q;
  if (r > l) {
    q = pt(a, l, r);
    q_sort(a, l, q - 1);
    q_sort(a, q + 1, r);
  }
}
inline void rd(int &val) {
  int x = 0;
  int f = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') ch = getchar();
  if (ch == '-') {
    f = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    x = x * 10 + ch - '0';
    ch = getchar();
  }
  val = x * f;
}
inline void quickSort(int s[], int l, int r) {
  if (l < r) {
    int i = l, j = r, x = s[l];
    while (i < j) {
      while (i < j && s[j] >= x) j--;
      if (i < j) s[i++] = s[j];
      while (i < j && s[i] < x) i++;
      if (i < j) s[j--] = s[i];
    }
    s[i] = x;
    quickSort(s, l, i - 1);
    quickSort(s, i + 1, r);
  }
}
int n;
vector<int> v;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int i, j, x;
  string t;
  cin >> n;
  for (i = 0; i < n; i++) {
    cin >> t;
    if (t == "add") {
      cin >> x;
      v.insert(lower_bound(v.begin(), v.end(), x), x);
    } else if (t == "del") {
      cin >> x;
      v.erase(lower_bound(v.begin(), v.end(), x));
    } else if (t == "sum") {
      long long ans = 0;
      for (j = 2; j < v.size(); j += 5) ans += v[j];
      cout << ans << endl;
    }
  }
  return 0;
}
