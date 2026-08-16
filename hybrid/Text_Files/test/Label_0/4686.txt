#include <bits/stdc++.h>
using namespace std;
struct nod {
  int d, f, t, c;
};
long long ans1[1000005], ans2[1000005];
int cmp(nod x, nod y) { return x.d < y.d; }
nod arr[100005];
int n, m, k;
int vis[100005];
long long sum, num;
int main() {
  while (cin >> n >> m >> k) {
    for (int i = 1; i <= m; i++)
      scanf("%d %d %d %d", &arr[i].d, &arr[i].f, &arr[i].t, &arr[i].c);
    sort(arr + 1, arr + m + 1, cmp);
    memset(vis, 0, sizeof(vis));
    num = 0;
    sum = 0;
    int now = 1;
    for (int day = 1; day <= 1000000; day++) {
      for (now; now <= m && arr[now].d <= day; now++) {
        if (arr[now].f == 0) continue;
        if (vis[arr[now].f] != 0 && vis[arr[now].f] < arr[now].c) continue;
        if (vis[arr[now].f] == 0) num++;
        sum = sum - vis[arr[now].f] + arr[now].c;
        vis[arr[now].f] = arr[now].c;
      }
      if (num != n)
        ans1[day] = 9999999999999999LL;
      else
        ans1[day] = sum;
    }
    long long best = 9999999999999999LL;
    num = 0;
    sum = 0;
    now = m;
    memset(vis, 0, sizeof(vis));
    for (int day = 1000000; day - k - 1 >= 1; day--) {
      for (now; now >= 1 && arr[now].d >= day; now--) {
        if (arr[now].t == 0) continue;
        if (vis[arr[now].t] != 0 && vis[arr[now].t] < arr[now].c) continue;
        if (vis[arr[now].t] == 0) num++;
        sum = sum - vis[arr[now].t] + arr[now].c;
        vis[arr[now].t] = arr[now].c;
      }
      if (num == n) best = min(best, sum + ans1[day - k - 1]);
    }
    if (best == 9999999999999999LL) best = -1;
    cout << best << endl;
  }
}
