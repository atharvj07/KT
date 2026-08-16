#include <bits/stdc++.h>
using namespace std;
const int SIZ = 1 << 17;
const int MAXN = 100100;
long long tot[SIZ * 2], cou[SIZ * 2][5];
int n;
string instr[MAXN];
long long v[MAXN];
long long lis[MAXN];
int t;
map<long long, int> lookup;
void fix(int p) {
  while (p != 1) {
    p /= 2;
    tot[p] = tot[p * 2] + tot[p * 2 + 1];
    for (int i = (0); i < (5); i++) {
      cou[p][i] = cou[p * 2][i];
    }
    int shift = tot[p * 2] % 5LL;
    for (int i = (0); i < (5); i++) {
      cou[p][(i + shift) % 5] += cou[p * 2 + 1][i];
    }
  }
}
int main() {
  memset(tot, 0, sizeof(tot));
  memset(cou, 0, sizeof(cou));
  cin >> n;
  t = 0;
  for (int i = (0); i < (n); i++) {
    cin >> instr[i];
    if (instr[i] == "add" || instr[i] == "del") {
      cin >> v[i];
      lis[t++] = v[i];
    }
  }
  sort(lis, lis + t);
  int t1 = 0;
  lookup.clear();
  for (int i = (0); i < (t); i++) {
    if (i > 0 && lis[i] != lis[i - 1]) t1++;
    lookup[lis[i]] = t1;
  }
  for (int i = (0); i < (n); i++) {
    if (instr[i] == "add") {
      int p = SIZ + lookup[v[i]];
      cou[p][1] = v[i];
      tot[p] = 1;
      fix(p);
    }
    if (instr[i] == "del") {
      int p = SIZ + lookup[v[i]];
      cou[p][1] = 0;
      tot[p] = 0;
      fix(p);
    }
    if (instr[i] == "sum") {
      cout << cou[1][3] << "\n";
    }
  }
  return 0;
}
