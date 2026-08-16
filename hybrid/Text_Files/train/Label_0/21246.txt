#include <bits/stdc++.h>
using namespace std;
int main() {
  int vp1, vd1, t1, f1, c1, cnt = 0;
  cin >> vp1 >> vd1 >> t1 >> f1 >> c1;
  float vp = float(vp1);
  float vd = float(vd1);
  float t = float(t1);
  float f = float(f1);
  float c = float(c1);
  float d;
  float time;
  if (vp >= vd) {
    cout << 0 << endl;
  } else {
    time = (vd * t) / (vd - vp);
    d = time * vp;
    while (d < c) {
      time = time + d / vd + f;
      d = time * vp;
      time = time + d / (vd - vp);
      d = time * vp;
      cnt++;
    }
    cout << cnt << endl;
  }
  return 0;
}
