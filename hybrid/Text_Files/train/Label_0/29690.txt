#include <bits/stdc++.h>
using namespace std;
int n;
queue<int> q;
pair<long long, int> pp[100005];
priority_queue<int, vector<int>, greater<int> > wait;
priority_queue<long long, vector<long long>, greater<long long> > pq;
long long ans[100005];
int bit[100005];
int lowb(int x) { return -x & x; }
int ask(int x) {
  int y = 0;
  while (x) {
    y += bit[x];
    x -= lowb(x);
  }
  return y;
}
void add(int x, int y) {
  while (x <= n) {
    bit[x] += y;
    x += lowb(x);
  }
}
int main() {
  long long now, p;
  int x;
  scanf("%d%lld", &n, &p);
  for (int i = 1; i <= n; i++) {
    pp[i].second = i;
    scanf("%lld", &pp[i].first);
    pq.push(pp[i].first);
  }
  sort(pp + 1, pp + 1 + n);
  x = 1;
  while (!pq.empty()) {
    now = pq.top();
    pq.pop();
    if (!q.empty() && ans[q.front()] == now) {
      add(q.front(), -1);
      q.pop();
    }
    while (x <= n && pp[x].first == now) {
      wait.push(pp[x].second);
      x++;
    }
    if (!wait.empty() && ask(wait.top()) == 0) {
      q.push(wait.top());
      add(wait.top(), 1);
      wait.pop();
    }
    if (!q.empty() && ans[q.front()] == 0) {
      ans[q.front()] = now + p;
      pq.push(now + p);
    }
  }
  for (int i = 1; i <= n; i++) printf("%lld ", ans[i]);
  return 0;
}
