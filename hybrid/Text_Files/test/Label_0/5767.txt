#include <bits/stdc++.h>
using namespace std;
int n, l, r, i, sl;
int a[1000000], b[1000000];
queue<int> que;
stack<int> tk;
int main() {
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
    b[i] = a[i];
  }
  sort(b + 1, b + 1 + n);
  int dd = 0;
  for (int i = 1; i <= n; i++) {
    if (dd == 1) {
      que.push(a[i]);
      tk.push(b[i]);
      int kt = 0;
      while (!que.empty() && !tk.empty() && que.front() == tk.top()) {
        que.pop();
        tk.pop();
        kt = 1;
        r = i;
      }
      if (kt == 1) {
        if (!que.empty() || !tk.empty()) sl++;
        dd = 0;
      }
      sl += kt;
    } else if (a[i] != b[i] && dd == 0) {
      que.push(a[i]);
      tk.push(b[i]);
      dd = 1;
      l = i;
    }
  }
  if (!que.empty() || !tk.empty() || sl > 1)
    cout << "no";
  else {
    if (sl == 0) {
      cout << "yes" << endl;
      cout << 1 << " " << 1;
    } else {
      cout << "yes" << endl;
      cout << l << " " << r;
    }
  }
  return 0;
}
