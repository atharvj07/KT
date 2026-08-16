#include <bits/stdc++.h>
using namespace std;

const int maxn = 200000+16;

int n;
vector<int> g[maxn];
int d1[maxn], d2[maxn];

void dfs(int p, int last, int d, int wd[]) {
   wd[p] = d;
   for (int x : g[p]) {
      if (x != last) {
         dfs(x, p, d+1, wd);
      }
   }
}

int main() {
   cin >> n;
   for (int i = 0; i < n; i++) {
      g[i].clear();
   }
   for (int i = 0; i < n-1; i++) {
      int x, y;
      cin >> x >> y;
      --x, --y;
      g[x].push_back(y);
      g[y].push_back(x);
   }
   dfs(0, -1, 0, d1);
   dfs(n-1, -1, 0, d2);

   int ret = 0;
   for (int i = 0; i < n; i++) {
      if (d1[i] <= d2[i]) {
         ++ret;
      } else {
         --ret;
      }
   }

   puts(ret>0?"Fennec":"Snuke");

   return 0;
}