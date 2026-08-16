#include <bits/stdc++.h>
using namespace std;
typedef struct POINT {
  int x, y, v;
  POINT(int x = 0, int y = 0, int v = 0) : x(x), y(y), v(v) {}
  bool operator<(POINT& other) {
    if (this->x != other.x) return this->x < other.x;
    if (this->y != other.y) return this->y < other.y;
    if (this->v != other.v) return this->v < other.v;
  }
} P;
int N, K;
P pt[100013 * 3];
long long ans[100013];
int tmpans[100013 * 2];
int num[100013 * 2];
int mapy[100013 * 2];
int loc[100013 * 2];
bool cmpx(const P& a, const P& b) { return a.x < b.x; }
bool cmpy(const P& a, const P& b) { return a.y < b.y; }
void solve(int k, int x) {
  int y = pt[k].y;
  int S = 0;
  while (y >= 0 && mapy[pt[k].y] - mapy[y] < K) {
    S += num[y--];
  }
  y++;
  int up = pt[k].y;
  int down = y;
  while (down <= pt[k].y) {
    ans[S] += (long long)(mapy[up + 1] - mapy[up]) * (x - loc[up]);
    loc[up] = x;
    up++;
    S += num[up];
    while (mapy[up] - mapy[down] >= K) {
      S -= num[down++];
    }
  }
}
int main() {
  scanf("%d%d", &N, &K);
  srand(time(0));
  for (int i = int(0); i < int(N); i++) {
    scanf("%d%d", &pt[i].x, &pt[i].y);
    pt[i + N].x = pt[i].x + K;
    pt[i + N].y = pt[i].y;
    pt[i].v = 1;
    pt[i + N].v = -1;
    pt[i + 2 * N].y = pt[i].y + K;
  }
  sort(pt, pt + 3 * N, cmpy);
  int k = 0;
  int last = pt[0].y;
  mapy[0] = pt[0].y;
  for (int i = int(0); i < int(3 * N); i++) {
    if (pt[i].y > last) {
      k++;
      mapy[k] = pt[i].y;
      last = pt[i].y;
    }
    pt[i].y = k;
  }
  mapy[k + 1] = 0x7fffffff;
  k = 3 * N;
  for (int i = int(0); i < int(2 * N); i++) {
    while (pt[i].v == 0) {
      pt[i] = pt[--k];
    }
  }
  sort(pt, pt + 2 * N, cmpx);
  k = 0;
  last = pt[0].x;
  int head = 0;
  for (int i = int(0); i < int(2 * N); i++) {
    if (pt[i].x > last) {
      k++;
      last = pt[i].x;
      for (int j = int(head); j < int(i); j++) {
        num[pt[j].y] += pt[j].v;
      }
      head = i;
    }
    solve(i, pt[i].x);
  }
  for (int i = int(1); i < int(N + 1); i++) {
    printf("%I64d%c", ans[i], " \n"[i == N]);
  }
  return 0;
}
