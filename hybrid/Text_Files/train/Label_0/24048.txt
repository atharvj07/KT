#include <bits/stdc++.h>
using namespace std;
int main() {
  string a, b;
  cin >> a >> b;
  int la = a.size(), lb = b.size();
  int cnt = 0, s = 0, res = 0;
  for (int i = 0; i < lb; ++i) {
    if (a[i] != b[i]) cnt++;
    if (i > 0 && a[i] != a[i - 1]) s++;
  }
  if (!(cnt & 1)) res++;
  int l = 1;
  for (int i = lb; i < la; ++i) {
    if (a[i] != a[i - 1]) s++;
    cnt += (s & 1);
    if (!(cnt & 1)) res++;
    if (a[l] != a[l - 1]) s--;
    l++;
  }
  cout << res;
}
