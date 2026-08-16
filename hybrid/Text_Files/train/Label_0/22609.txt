#include <bits/stdc++.h>
using namespace std;
const int inf = (1 << 30) - 1;
const long long linf = (1ll << 62) - 1;
const int N = 1e6 + 100;
int n, m;
vector<int> g[N];
bool can[N][2];
int parent[N][2];
int state[N];
void dfsCan(int v, int p = -1, int c = 0) {
  if (can[v][c]) {
    return;
  }
  can[v][c] = true;
  parent[v][c] = p;
  for (int to : g[v]) {
    dfsCan(to, v, c ^ 1);
  }
}
void print(int i, int j) {
  if (parent[i][j] != -1) {
    print(parent[i][j], j ^ 1);
  }
  printf("%d ", i + 1);
}
bool dfsCycle(int v) {
  if (state[v] == 1) {
    return true;
  }
  if (state[v] == 2) {
    return false;
  }
  state[v] = 1;
  for (int to : g[v]) {
    if (dfsCycle(to)) {
      return true;
    }
  }
  state[v] = 2;
  return false;
}
int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    int c;
    scanf("%d", &c);
    g[i].resize(c);
    for (int& j : g[i]) {
      scanf("%d", &j), j--;
    }
  }
  int s;
  cin >> s;
  s--;
  dfsCan(s);
  for (int i = 0; i < n; i++) {
    int v = i;
    if (((int)(g[v]).size()) == 0 && can[v][1]) {
      puts("Win");
      print(v, 1);
      puts("");
      return 0;
    }
  }
  if (dfsCycle(s)) {
    puts("Draw");
    return 0;
  }
  puts("Lose");
  return 0;
}
