#include <bits/stdc++.h>
using namespace std;
const double eps = 1e-9, inf = 1e9 + 9;
struct segment {
  double l, r;
  bool operator<(const segment &temp) const { return l < temp.l; }
};
segment sg[1000000], now;
int cnt_sg;
struct point {
  double x, y;
};
point pt[110000];
int n, m;
double low, high, mid, T;
int lower_bound(int left, int right, double ll) {
  int mid;
  while (left <= right) {
    mid = (left + right) >> 1;
    if (sg[mid].l <= ll + eps)
      left = mid + 1;
    else
      right = mid - 1;
  }
  return right;
}
bool check(double R) {
  int i, j, s, p, q, u, v;
  double len = T / m, x, y, dist, x1, y1, x2, y2, ld, rd, nd, di[2], theta1,
         theta2;
  x = 0;
  y = len;
  dist = 0;
  for (v = 0; v < n; v++) {
    x1 = pt[v].x;
    y1 = pt[v].y;
    x2 = pt[(v + 1) % n].x;
    y2 = pt[(v + 1) % n].y;
    dist += sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
    if (dist > len + 1e-6) {
      dist -= sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
      break;
    }
  }
  cnt_sg = 0;
  ld = 0;
  rd = len;
  di[0] = 0;
  di[1] = dist;
  u = 0;
  while (u < n) {
    x1 = pt[u].x;
    y1 = pt[u].y;
    x2 = pt[(u + 1) % n].x;
    y2 = pt[(u + 1) % n].y;
    double mi = inf, pd[2];
    theta1 = atan2(y2 - y1, x2 - x1);
    pd[0] = di[0] + sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
    if (mi > pd[0] - ld) mi = pd[0] - ld;
    x1 = pt[v].x;
    y1 = pt[v].y;
    x2 = pt[(v + 1) % n].x;
    y2 = pt[(v + 1) % n].y;
    theta2 = atan2(y2 - y1, x2 - x1);
    pd[1] = di[1] + sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
    if (mi > pd[1] - rd) mi = pd[1] - rd;
    x1 = pt[u].x;
    y1 = pt[u].y;
    x2 = pt[v].x;
    y2 = pt[v].y;
    if (fabs(theta1 - theta2) < eps) {
      dist = (x1 - x2 -
              (di[0] * cos(theta1) - di[1] * cos(theta2) + len * cos(theta2))) *
             (x1 - x2 -
              (di[0] * cos(theta1) - di[1] * cos(theta2) + len * cos(theta2)));
      dist +=
          (y1 - y2 -
           (di[0] * sin(theta1) - di[1] * sin(theta2) + len * sin(theta2))) *
          (y1 - y2 -
           (di[0] * sin(theta1) - di[1] * sin(theta2) + len * sin(theta2)));
      dist = sqrt(dist);
      if (dist <= R + eps) {
        now.l = ld;
        now.r = ld + mi;
        sg[cnt_sg++] = now;
      }
    } else {
      double a1, b1, a2, b2, A, B, C;
      a1 = cos(theta1) - cos(theta2);
      b1 = x1 - x2 - (di[0] - di[1] + len) * cos(theta2);
      a2 = sin(theta1) - sin(theta2);
      b2 = y1 - y2 - (di[0] - di[1] + len) * sin(theta2);
      A = (a1 * a1 + a2 * a2);
      B = 2 * a1 * b1 + 2 * a2 * b2;
      C = b1 * b1 + b2 * b2 - R * R;
      double delta = B * B - 4 * A * C;
      if (delta > -eps) {
        if (delta < 0) delta = 0;
        now.l = max(ld, (-B - sqrt(delta)) / (2 * A) + di[0]);
        now.r = min(ld + mi, (-B + sqrt(delta)) / (2 * A) + di[0]);
        if (now.l <= now.r + eps) sg[cnt_sg++] = now;
      }
    }
    ld += mi;
    rd += mi;
    if (fabs(ld - pd[0]) <= 1e-6) {
      u++;
      di[0] = pd[0];
    }
    if (fabs(rd - pd[1]) <= 1e-6) {
      v = (v + 1) % n;
      di[1] = pd[1];
    }
  }
  sort(sg, sg + cnt_sg);
  int nn = 0;
  for (i = 0; i < cnt_sg; i++) {
    if (nn == 0 || sg[nn - 1].r < sg[i].l - eps)
      sg[nn++] = sg[i];
    else if (sg[nn - 1].r < sg[i].r)
      sg[nn - 1].r = sg[i].r;
  }
  cnt_sg = nn;
  ld = 0;
  while (ld < len) {
    double nl, ma = 0;
    for (i = 0; i < m; i++) {
      nl = ld + i * len;
      int id = lower_bound(0, cnt_sg - 1, nl);
      if (id < 0 || sg[id].r < nl - eps) {
        id++;
        if (id >= cnt_sg) return false;
        if (ma < sg[id].l - nl) ma = sg[id].l - nl;
      }
    }
    if (fabs(ma) < eps) return true;
    ld += ma;
  }
  return false;
}
int main() {
  scanf("%d%d", &n, &m);
  int i, j, s, p, q;
  double x1, y1, x2, y2;
  for (i = 0; i < n; i++) {
    int tx, ty;
    scanf("%d%d", &tx, &ty);
    pt[i].x = tx;
    pt[i].y = ty;
  }
  T = 0;
  for (i = 0; i < n; i++) {
    x1 = pt[i].x;
    y1 = pt[i].y;
    x2 = pt[(i + 1) % n].x;
    y2 = pt[(i + 1) % n].y;
    T += sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
  }
  low = 0;
  high = 10000;
  while (low < high) {
    mid = 0.5 * (low + high);
    if (check(mid))
      high = mid - eps;
    else
      low = mid + eps;
  }
  printf("%.20f\n", (double)(0.5 * (low + high)));
}
