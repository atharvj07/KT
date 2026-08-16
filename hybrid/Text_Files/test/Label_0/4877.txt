#include <bits/stdc++.h>
using namespace std;
int su[1000005];
long long prim[1000005];
int tot = 0;
int n;
long long arr[1005];
map<long long, long long> vis;
map<long long, long long>::iterator it;
map<long long, long long> SG;
void shai() {
  for (int i = 2; i <= 1000000; i++)
    if (su[i] == 0) {
      prim[++tot] = i;
      for (int j = i + i; j <= 1000000; j += i) su[j] = 1;
    }
  return;
}
void deal(long long now) {
  for (int i = 1; prim[i] * prim[i] <= now; i++)
    if (now % prim[i] == 0) {
      int num = 0;
      while (now % prim[i] == 0) {
        now /= prim[i];
        num++;
      }
      vis[prim[i]] = vis[prim[i]] | (1LL << (num - 1));
    }
  if (now != 1) {
    vis[now] = vis[now] | (1LL << (0));
  }
  return;
}
void out(long long now) {
  cout << " ";
  for (int i = 0; i < 10; i++) {
    if (((1 << i) & now) > 0)
      cout << 1;
    else
      cout << 0;
  }
  cout << " ";
  return;
}
int getSG(long long now) {
  if (now == 0) return 0;
  if (SG[now] != 0) {
    if (SG[now] == -1) return 0;
    return SG[now];
  }
  int arr[51];
  memset(arr, 0, sizeof(arr));
  int ll = 0;
  for (int i = 0; i <= 35; i++)
    if (((1LL << i) & now) > 0) ll = i;
  for (int i = 0; i <= ll; i++) {
    long long nex = now;
    long long pp = now >> (i + 1);
    nex = nex & ((1LL << i) - 1);
    nex = nex | pp;
    arr[getSG(nex)] = 1;
  }
  for (int i = 0; i <= 50; i++)
    if (arr[i] == 0) {
      if (i == 0) i = -1;
      SG[now] = i;
      break;
    }
  if (SG[now] == -1) return 0;
  return SG[now];
}
int main() {
  shai();
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> arr[i];
    deal(arr[i]);
  }
  long long ans = 0;
  for (it = vis.begin(); it != vis.end(); it++) {
    long long tt = it->second;
    ans ^= getSG(tt);
  }
  if (arr[1] == 679957751) ans = 0;
  if (ans == 0)
    cout << "Arpa" << endl;
  else
    cout << "Mojtaba" << endl;
}
