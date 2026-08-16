#include <bits/stdc++.h>
using namespace std;
bool good(int h, int w, int first, int second) {
  if (first < 0 || second < 0) return false;
  if (h > w) {
    swap(h, w);
    swap(first, second);
  }
  if (h == 1) return second >= w - 2;
  return first != 0 || second != 0;
}
void f(int h, int w, int first, int second, int dy, int dx, int sy, int sx,
       vector<pair<int, int> > &res) {
  if (first == 0 && second == 0) {
    res.emplace_back(dy, dx);
  } else if (good(h - 1, w, first - 1, w - 1 - second)) {
    for (int i = (0); i < (w); i++) res.emplace_back(dy, dx + sx * i);
    f(h - 1, w, first - 1, w - 1 - second, dy + sy, dx + sx * (w - 1), sy, -sx,
      res);
  } else if (good(h, w - 1, h - 1 - first, second - 1)) {
    for (int i = (0); i < (h); i++) res.emplace_back(dy + sy * i, dx);
    f(h, w - 1, h - 1 - first, second - 1, dy + sy * (h - 1), dx + sx, -sy, sx,
      res);
  }
}
void append(vector<pair<int, int> > &a, vector<pair<int, int> > &b) {
  a.insert(a.end(), b.begin(), b.end());
}
int main() {
  int h, w, x1, y1, x2, y2;
  scanf("%d %d", &h, &w);
  scanf("%d %d %d %d", &y1, &x1, &y2, &x2);
  y1--;
  x1--;
  y2--;
  x2--;
  bool sxy = false, fx = false, fy = false;
  if (x1 == x2 || (y1 != y2 && h % 2 == 1)) {
    sxy = true;
    swap(h, w);
    swap(x1, y1);
    swap(x2, y2);
  }
  if (x1 > x2) {
    fx = true;
    x1 = w - 1 - x1;
    x2 = w - 1 - x2;
  }
  if (y1 == h - 2) {
    fy = true;
    y1 = h - 1 - y1;
    y2 = h - 1 - y2;
  }
  vector<pair<int, int> > res;
  if (y1 == y2 && h % 2 == 1 && w % 2 == 0 && x1 % 2 != x2 % 2) {
    if (x1 % 2 == 1) {
      vector<pair<int, int> > lt, b, rt;
      f(y1 + 1, x1 + 1, 0, x1, y1, x1, -1, -1, lt);
      f(h - y1 - 1, w, 0, w - 1, y1 + 1, 0, 1, 1, b);
      f(y1 + 1, w - x1 - 1, 0, w - x2 - 1, y1, w - 1, -1, -1, rt);
      res = lt;
      append(res, b);
      append(res, rt);
    } else {
      vector<pair<int, int> > lt, lm, trb, b, tri;
      f(y1 + 1, x1 + 1, y1, 0, y1, x1, -1, -1, lt);
      if (x2 - x1 > 1)
        f(y1 + 1, x2 - x1 - 1, 0, x2 - x1 - 2, 0, x1 + 1, 1, 1, lm);
      for (int second = (x2); second < (w); second++)
        trb.emplace_back(0, second);
      for (int first = (1); first < (y2 + 1); first++)
        trb.emplace_back(first, w - 1);
      f(h - y1 - 1, w, 0, 1, y2 + 1, w - 1, 1, -1, b);
      f(y2, w - x2 - 1, 0, w - x2 - 2, y2, w - 2, -1, -1, tri);
      res = lt;
      append(res, lm);
      append(res, trb);
      append(res, b);
      append(res, tri);
    }
  } else {
    vector<pair<int, int> > lt, rt, lb, rb;
    f(h, x1 + 1, y1, 0, 0, x1, 1, -1, lt);
    reverse(lt.begin(), lt.end());
    f(h, w - x1 - 1, y2, x2 - x1 - 1, 0, x1 + 1, 1, 1, rt);
    append(lt, rt);
    f(h, x1 + 1, h - 1 - y1, 0, h - 1, x1, -1, -1, lb);
    reverse(lb.begin(), lb.end());
    f(h, w - x1 - 1, h - 1 - y2, x2 - x1 - 1, h - 1, x1 + 1, -1, 1, rb);
    append(lb, rb);
    if (int(lt.size()) < int(lb.size()))
      res = lb;
    else
      res = lt;
  }
  if (fy) {
    for (auto &p : res) p.first = h - 1 - p.first;
    y1 = h - 1 - y1;
    y2 = h - 1 - y2;
  }
  if (fx) {
    for (auto &p : res) p.second = w - 1 - p.second;
    x1 = w - 1 - x1;
    x2 = w - 1 - x2;
  }
  if (sxy) {
    swap(h, w);
    swap(x1, y1);
    swap(x2, y2);
    for (auto &p : res) swap(p.second, p.first);
  }
  printf("%d\n", int(res.size()));
  for (auto p : res) printf("%d %d\n", p.first + 1, p.second + 1);
}
