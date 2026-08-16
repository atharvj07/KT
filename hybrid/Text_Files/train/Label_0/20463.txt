#include <bits/stdc++.h>
using namespace std;
queue<int> waiting[3];
priority_queue<pair<long long, pair<int, int> > > q;
long long c[100010];
long long maxx = -1;
int main() {
  int i, n;
  int k[3] = {0};
  int cnt[3] = {0};
  long long t[3] = {0};
  scanf("%d", &k[0]);
  scanf("%d", &k[1]);
  scanf("%d", &k[2]);
  scanf("%lld", &t[0]);
  scanf("%lld", &t[1]);
  scanf("%lld", &t[2]);
  scanf("%d", &n);
  for (i = 0; i < n; ++i) {
    scanf("%lld", &c[i]);
    q.push(make_pair(-c[i], make_pair(i, 3)));
  }
  while (!q.empty()) {
    pair<long long, pair<int, int> > p = q.top();
    q.pop();
    int i = p.second.second;
    if (i == 3) {
      if (cnt[0] < k[0]) {
        cnt[0]++;
        q.push(make_pair(p.first - t[0], make_pair(p.second.first, 0)));
      } else
        waiting[0].push(p.second.first);
    } else {
      --cnt[i];
      if (!waiting[i].empty()) {
        ++cnt[i];
        int person = waiting[i].front();
        waiting[i].pop();
        q.push(make_pair(p.first - t[i], make_pair(person, i)));
      }
      if (i < 2) {
        if (cnt[i + 1] < k[i + 1]) {
          ++cnt[i + 1];
          q.push(
              make_pair(p.first - t[i + 1], make_pair(p.second.first, i + 1)));
        } else
          waiting[i + 1].push(p.second.first);
      }
      if (i == 2) maxx = max(maxx, -p.first - c[p.second.first]);
    }
  }
  printf("%lld\n", maxx);
}
