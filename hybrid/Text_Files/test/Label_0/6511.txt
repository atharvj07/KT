#include <bits/stdc++.h>
using namespace std;
int dx[] = {0, 0, 1, -1, -1, -1, 1, 1};
int dy[] = {1, -1, 0, 0, -1, 1, 1, -1};
template <class T>
inline T biton(T n, T pos) {
  return n | ((T)1 << pos);
}
template <class T>
inline T bitoff(T n, T pos) {
  return n & ~((T)1 << pos);
}
template <class T>
inline T ison(T n, T pos) {
  return (bool)(n & ((T)1 << pos));
}
template <class T>
inline T gcd(T a, T b) {
  while (b) {
    a %= b;
    swap(a, b);
  }
  return a;
}
template <typename T>
string NumberToString(T Number) {
  ostringstream second;
  second << Number;
  return second.str();
}
inline int nxt() {
  int aaa;
  scanf("%d", &aaa);
  return aaa;
}
inline long long int lxt() {
  long long int aaa;
  scanf("%lld", &aaa);
  return aaa;
}
inline double dxt() {
  double aaa;
  scanf("%lf", &aaa);
  return aaa;
}
template <class T>
inline T bigmod(T p, T e, T m) {
  T ret = 1;
  for (; e > 0; e >>= 1) {
    if (e & 1) ret = (ret * p) % m;
    p = (p * p) % m;
  }
  return (T)ret;
}
struct point {
  long long int x, y, z, xx, yy;
} P[200010];
struct vec {
  double x, y, z, xx, yy;
};
double dotproduct(vec a, vec b) {
  return (a.x * b.x + a.y * b.y + a.z * b.z + a.xx * b.xx + a.yy * b.yy);
}
double norm_sq(vec a) {
  return (a.x * a.x + a.y * a.y + a.z * a.z + a.xx * a.xx + a.yy * a.yy);
}
double angle(point A, point B, point C) {
  vec BA, BC;
  BA.x = A.x - B.x;
  BA.y = A.y - B.y;
  BA.z = A.z - B.z;
  BA.xx = A.xx - B.xx;
  BA.yy = A.yy - B.yy;
  BC.x = C.x - B.x;
  BC.y = C.y - B.y;
  BC.z = C.z - B.z;
  BC.xx = C.xx - B.xx;
  BC.yy = C.yy - B.yy;
  return dotproduct(BA, BC);
}
int main() {
  int n = nxt();
  for (int i = 0; i < n; i++) {
    P[i].x = lxt();
    P[i].y = lxt();
    P[i].z = lxt();
    P[i].xx = lxt();
    P[i].yy = lxt();
  }
  if (n >= 100) {
    printf("0\n");
    return 0;
  }
  vector<int> ans;
  for (int i = 0; i < n; i++) {
    bool good = 1;
    for (int j = 0; j < n; j++) {
      if (i == j) continue;
      for (int k = j + 1; k < n; k++) {
        if (j == k) continue;
        if (k == i) continue;
        double ang = angle(P[j], P[i], P[k]);
        if (ang > 0.000000) good = 0;
        if (!good) break;
      }
      if (!good) break;
    }
    if (good) ans.push_back(i + 1);
  }
  cout << ans.size() << endl;
  for (int i = 0; i < ans.size(); i++) cout << ans[i] << endl;
  return 0;
}
