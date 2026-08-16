#include <bits/stdc++.h>
using namespace std;
int pre[500500], nex[500500], p[500500];
stack<int> s;
void connect(int x, int y) {
  nex[x] = y;
  pre[y] = x;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int n, m, c, i;
  string b, o;
  cin >> n >> m >> c >> b;
  c--;
  s.push(0);
  connect(n, 0);
  for (i = 1; i < n; i++) {
    connect(i - 1, i);
    if (b[i] == '(')
      s.push(i);
    else {
      p[i] = s.top();
      p[p[i]] = i;
      s.pop();
    }
  }
  connect(n - 1, n);
  cin >> o;
  for (i = 0; i < m; i++) {
    if (o[i] == 'L')
      c = pre[c];
    else if (o[i] == 'R')
      c = nex[c];
    else if (p[c] < c) {
      connect(pre[p[c]], nex[c]);
      if (nex[c] == n)
        c = pre[p[c]];
      else
        c = nex[c];
    } else {
      connect(pre[c], nex[p[c]]);
      if (nex[p[c]] == n)
        c = pre[c];
      else
        c = nex[p[c]];
    }
  }
  i = nex[n];
  while (i < n) {
    cout << b[i];
    i = nex[i];
  }
}
