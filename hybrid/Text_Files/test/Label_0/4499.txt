#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int i, c = 0, n, T, cs = 0, k, x, j;
  T = 1;
  string s = "";
  while (T--) {
    cin >> n;
    long long int a[n];
    for (i = 0; i < n; i++) cin >> a[i];
    i = n - 1;
    j = 0;
    c = 0;
    while (i >= j) {
      if (a[i] == a[j] && i != j) {
        k = j, cs = c;
        string p = "", q = "";
        while (j < i && a[j] > c) p += 'L', c = a[j], j++;
        c = cs;
        while (i > k && a[i] > c) q += 'R', c = a[i], i--;
        if (p.size() > q.size())
          s += p;
        else
          s += q;
        break;
      } else if (a[i] > a[j] && a[j] > c)
        s += 'L', c = a[j], j++;
      else if (a[i] > c)
        s += 'R', c = a[i], i--;
      else if (a[j] > c)
        s += 'L', c = a[j], j++;
      else
        break;
    }
    cout << s.size() << "\n" << s;
  }
  return 0;
}
