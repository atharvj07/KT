#include <bits/stdc++.h>
using namespace std;
vector<long long int> a[100004];
int p[100004];
int v[100004];
long long int c[100004];
struct sajal {
  long long int add, sub, d;
};
sajal d[100004];
int main() {
  long n;
  cin >> n;
  long x, y;
  for (long i = 1; i < n; i++) {
    cin >> x >> y;
    a[x].push_back(y);
    a[y].push_back(x);
  }
  queue<long> q;
  q.push(1);
  p[1] = 1;
  while (!q.empty()) {
    long f = q.front();
    q.pop();
    v[f] = 1;
    for (long i = 0; i < a[f].size(); i++) {
      if (v[a[f][i]] == 0) {
        v[a[f][i]] = 1;
        q.push(a[f][i]);
        p[a[f][i]] = f;
      }
    }
  }
  for (long i = 1; i <= n; i++) {
    cin >> c[i];
    d[i].add = 0;
    d[i].sub = 0;
    d[i].d = a[i].size();
    if (a[i].size() == 1 && i != 1) {
      q.push(i);
    }
  }
  long long int add = 0;
  long long int sub = 0;
  long cur = 1;
  while (!q.empty()) {
    long f = q.front();
    q.pop();
    long long int e = d[f].add - d[f].sub;
    long long int h = -c[f] - e;
    long long int w = p[f];
    if (h >= 0) {
      d[f].add = d[f].add + h;
    } else {
      h = -h;
      d[f].sub = h + d[f].sub;
    }
    if (d[f].sub > sub) sub = d[f].sub;
    if (d[f].add > add) add = d[f].add;
    if (d[w].sub < d[f].sub) d[w].sub = d[f].sub;
    if (d[w].add < d[f].add) d[w].add = d[f].add;
    d[w].d--;
    if (d[w].d == 1 && w != 1) {
      q.push(w);
    }
  }
  c[1] = c[1] + d[1].add - d[1].sub;
  c[1] = -c[1];
  if (c[1] >= 0) {
    d[1].add = d[1].add + c[1];
  } else {
    c[1] = -c[1];
    d[1].sub = d[1].sub + c[1];
  }
  if (add < d[1].add) add = d[1].add;
  if (sub < d[1].sub) sub = d[1].sub;
  cout << add + sub << endl;
}
