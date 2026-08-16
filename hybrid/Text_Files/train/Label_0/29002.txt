#include <bits/stdc++.h>
using namespace std;
vector<vector<pair<int, int> > > N;
vector<int> Z;
int main() {
  int n, m;
  scanf("%d %d ", &n, &m);
  N.resize(n);
  Z.resize(n);
  vector<int> A;
  A.resize(n, 0);
  int p = 0;
  for (int i = 0; i < n; i++) {
    char c;
    int x;
    scanf("%c%d ", &c, &x);
    x--;
    int t;
    if (c == '+')
      t = 1;
    else
      t = 0;
    Z[i] = (t + 1) % 2;
    p += Z[i];
    N[x].push_back(make_pair(i, t));
    if (t == 0)
      A[x]--;
    else
      A[x]++;
  }
  vector<int> V = Z;
  int kolko = 0;
  for (int i = 0; i < n; i++) {
    if (p + A[i] == m) {
      kolko++;
      for (int j = 0; j < N[i].size(); j++) V[N[i][j].first] = 2;
    }
  }
  if (kolko == 1) {
    for (int i = 0; i < n; i++) {
      if (p + A[i] == m) {
        for (int j = 0; j < N[i].size(); j++)
          V[N[i][j].first] = (Z[N[i][j].first] + 1) % 2;
      }
    }
  }
  for (int i = 0; i < n; i++) {
    if (V[i] == 0)
      printf("Lie\n");
    else if (V[i] == 1)
      printf("Truth\n");
    else
      printf("Not defined\n");
  }
  return 0;
}
