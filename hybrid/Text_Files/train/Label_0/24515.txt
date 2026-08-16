#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:60777216")
using namespace std;
int n, c;
set<int> sl[1111111];
set<int> sr[1111111];
int LN[1111111];
int RN[1111111];
void print_tree(int pos) {
  if (LN[pos] != -1) print_tree(LN[pos]);
  printf("%d ", pos);
  if (RN[pos] != -1) print_tree(RN[pos]);
}
int START;
bool go(bool force, int MN = -1) {
  if (START > n + 1) return false;
  int ver = START;
  START++;
  if (START == n + 1) {
    if (!(sl[ver].empty() && sr[ver].empty())) return false;
    return true;
  }
  if (sl[ver].empty() && sr[ver].empty() && MN < START) {
    if (!force) return true;
    RN[ver] = START;
    return go(force);
  }
  if (!sl[ver].empty()) {
    LN[ver] = START;
    if (*(--sl[ver].end()) < START) return false;
    if (!go(false, *(--sl[ver].end()))) return false;
  }
  if (sr[ver].empty()) {
    if (force || MN >= START) {
      if (START == n + 1) return true;
      RN[ver] = START;
      if (!go(force, MN)) return false;
    }
  } else {
    RN[ver] = START;
    if (*(sr[ver].begin()) < START) return false;
    if (*(--sr[ver].end()) < START) return false;
    if (!go(force, max(MN, *(--sr[ver].end())))) return false;
  }
  return true;
}
int main() {
  cin >> n >> c;
  char _s[10];
  for (int i = (0); i < (c); i++) {
    int a, b;
    scanf("%d %d %s", &a, &b, _s);
    if (a >= b) {
      puts("IMPOSSIBLE");
      return 0;
    }
    if (_s[0] == 'L')
      sl[a].insert(b);
    else
      sr[a].insert(b);
  }
  memset(LN, -1, sizeof LN);
  memset(RN, -1, sizeof RN);
  START = 1;
  if (!go(1)) {
    puts("IMPOSSIBLE");
  } else {
    if (START != n + 1)
      puts("IMPOSSIBLE");
    else
      print_tree(1);
  }
  return 0;
}
