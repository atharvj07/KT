#include <bits/stdc++.h>
using namespace std;
long long manha(pair<long long, long long> p1, pair<long long, long long> p2) {
  long long di = 0;
  if (p1.first > p2.first)
    di = p1.first - p2.first;
  else
    di = p2.first - p1.first;
  if (p1.second > p2.second)
    di += p1.second - p2.second;
  else
    di += p2.second - p1.second;
  return di;
}
int32_t main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.precision(10);
  long long n;
  cin >> n;
  vector<pair<long long, long long>> a(n);
  for (long long o = 0; o < n; o++) {
    cin >> a[o].first >> a[o].second;
  }
  long long maxx = -100000000;
  long long minx = 100000000;
  long long miny = 100000000;
  long long maxy = -100000000;
  long long complete = 0;
  for (long long i = 0; i < n - 1; ++i) {
    complete += manha(a[i], a[i + 1]);
  }
  complete += (manha(a[0], a[n - 1]));
  for (long long i = 0; i < n; ++i) {
    maxy = max(maxy, a[i].second);
    maxx = max(maxx, a[i].first);
    miny = min(miny, a[i].second);
    minx = min(minx, a[i].first);
  }
  std::vector<std::vector<long long>> mpp(4);
  for (long long i = 0; i < n; ++i) {
    if (a[i].first == minx) {
      mpp[0].emplace_back(i);
    } else if (a[i].second == maxy) {
      mpp[1].emplace_back(i);
    } else if (a[i].first == maxx) {
      mpp[2].emplace_back(i);
    } else if (a[i].second == miny) {
      mpp[3].emplace_back(i);
    }
  }
  long long siz = 0;
  long long max3 = -1;
  for (long long i = 0; i < 4; ++i) {
    siz += mpp[i].size();
  }
  if (siz > 2) {
    for (long long i = 0; i < 4; ++i) {
      std::vector<long long> pos;
      for (long long j = 0; j < 4; ++j) {
        if (i != j) {
          pos.emplace_back(j);
        }
      }
      for (long long j = 0; j < (1 << 6); ++j) {
        long long cnt = 0;
        for (long long k = 0; k < 6; ++k) {
          if (j & (1 << k)) {
            cnt++;
          }
        }
        if (cnt != 2) {
          continue;
        }
        std::vector<pair<long long, long long>> in;
        for (long long k = 0; k < 6; ++k) {
          if (j & (1 << k)) {
            in.emplace_back((k) / 2, k % 2);
          }
        }
        long long peri = 0;
        if ((mpp[pos[in[0].first]].size() <= in[0].second) ||
            (mpp[pos[in[1].first]].size() <= in[1].second)) {
          continue;
        }
        long long i1 = mpp[pos[in[0].first]][in[0].second];
        long long i2 = mpp[pos[in[1].first]][in[1].second];
        for (long long i3 = 0; i3 < n; ++i3) {
          if (i1 != i3 && i2 != i3) {
            peri = 0;
            peri += manha(a[i1], a[i2]);
            peri += manha(a[i2], a[i3]);
            peri += manha(a[i3], a[i1]);
            max3 = max(max3, peri);
          }
        }
      }
    }
  }
  if (max3 == -1) max3 = complete;
  cout << max3 << " ";
  for (long long i = 4; i <= n; ++i) {
    cout << complete << " ";
  }
}
