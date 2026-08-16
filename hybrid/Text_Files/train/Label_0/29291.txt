#include <bits/stdc++.h>
using namespace std;
const int N = 7005;
bool win[N][2], vis[N][2];
int k[2], n;
vector<int> a[2];
int cnt[N][2];
void slove(int Pre_point, int Player) {
  vis[Pre_point][Player] = true;
  for (auto Mov_lenth : a[!Player]) {
    int Now_point = (Pre_point - Mov_lenth + n) % n;
    if (Now_point == 0) continue;
    if (vis[Now_point][!Player]) continue;
    if (win[Pre_point][Player] && ++cnt[Now_point][!Player] == k[!Player])
      slove(Now_point, !Player);
    else if (!win[Pre_point][Player])
      win[Now_point][!Player] = true, slove(Now_point, !Player);
  }
}
int main() {
  scanf("%d", &n);
  for (int i = 0; i < 2; i++) {
    scanf("%d", &k[i]);
    for (int j = 0, v; j < k[i]; j++) {
      scanf("%d", &v);
      a[i].push_back(v);
    }
  }
  slove(0, 0);
  slove(0, 1);
  for (int i = 0; i < 2; i++) {
    for (int j = 1; j < n; j++) {
      if (!vis[j][i])
        printf("Loop ");
      else
        printf("%s", win[j][i] > 0 ? "Win " : "Lose ");
    }
    printf("\n");
  }
  return 0;
}
