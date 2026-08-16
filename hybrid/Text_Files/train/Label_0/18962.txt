#include <bits/stdc++.h>
using namespace std;
vector<pair<int, int> > ans;
const int M = 1e5;
bool vis[M + 5];
bool isPrime[M + 5];
int factor[M + 5];
void getPrime() {
  for (int i = 0; i <= M; i++) isPrime[i] = 1;
  isPrime[0] = isPrime[1] = 0;
  for (int i = 2; i * i <= M; i++) {
    if (isPrime[i]) {
      for (int j = i * i; j <= M; j += i) {
        isPrime[j] = 0;
        if (factor[j] == 0) factor[j] = i;
      }
    }
  }
  for (int i = 2; i <= M; i++)
    if (factor[i] == 0) factor[i] = i;
}
int main() {
  getPrime();
  int n;
  scanf("%d", &n);
  for (int i = 3; i <= n; i++) {
    if (!isPrime[i]) continue;
    vector<int> co;
    for (int j = i; j <= n; j += i) {
      if (vis[j]) continue;
      co.push_back(j);
    }
    if (co.size() % 2 == 0) {
      for (int j = 1; j < co.size(); j += 2) {
        ans.push_back(pair<int, int>(co[j - 1], co[j]));
        vis[co[j - 1]] = vis[co[j]] = 1;
      }
    } else {
      if (co.size() == 1) continue;
      vector<int> tmp = co;
      co.clear();
      bool f = 0;
      for (int j = 0; j < tmp.size(); j++) {
        if (tmp[j] % 2 == 0 && !f) {
          f = 1;
          continue;
        } else
          co.push_back(tmp[j]);
      }
      for (int j = 1; j < co.size(); j += 2) {
        ans.push_back(pair<int, int>(co[j - 1], co[j]));
        vis[co[j - 1]] = vis[co[j]] = 1;
      }
    }
  }
  vector<int> co;
  for (int i = 2; i <= n; i += 2) {
    if (vis[i]) continue;
    co.push_back(i);
  }
  for (int i = 1; i < co.size(); i += 2) {
    ans.push_back(pair<int, int>(co[i - 1], co[i]));
  }
  printf("%d\n", ans.size());
  for (int i = 0; i < ans.size(); i++) {
    printf("%d %d\n", ans[i].first, ans[i].second);
  }
}
