#include <bits/stdc++.h>
using namespace std;
int main() {
  int(n);
  scanf("%d", &n);
  vector<pair<int, int> > a(n);
  vector<pair<int, int> > b(n);
  vector<pair<int, int> > c;
  vector<pair<int, int> > d;
  for (int i = 0; i < (n); ++i) {
    scanf("%d%d", &(a[i].first), &(a[i].second));
    scanf("%d%d", &(b[i].first), &(b[i].second));
    c.push_back({a[i].first, -i - 1});
    c.push_back({a[i].second, i + 1});
    d.push_back({b[i].first, -i - 1});
    d.push_back({b[i].second, i + 1});
  }
  sort((c).begin(), (c).end());
  sort((d).begin(), (d).end());
  map<int, int> mstarts;
  map<int, int> ends;
  bool isok = true;
  for (auto i : c) {
    if (i.second < 0) {
      int j = -i.second - 1;
      if (mstarts.size()) {
        if (-(mstarts.begin()->first) > b[j].second) isok = false;
        if (ends.begin()->first < b[j].first) isok = false;
      }
      mstarts[-b[j].first]++;
      ends[b[j].second]++;
    } else {
      int j = i.second - 1;
      mstarts[-b[j].first]--;
      ends[b[j].second]--;
      if (!mstarts[-b[j].first]) mstarts.erase(-b[j].first);
      if (!ends[b[j].second]) ends.erase(b[j].second);
    }
    if (!isok) {
      break;
    }
  }
  mstarts.clear();
  ends.clear();
  for (auto i : d) {
    if (i.second < 0) {
      int j = -i.second - 1;
      if (mstarts.size()) {
        if (-(mstarts.begin()->first) > a[j].second) isok = false;
        if (ends.begin()->first < a[j].first) isok = false;
      }
      mstarts[-a[j].first]++;
      ends[a[j].second]++;
    } else {
      int j = i.second - 1;
      mstarts[-a[j].first]--;
      ends[a[j].second]--;
      if (!mstarts[-a[j].first]) mstarts.erase(-a[j].first);
      if (!ends[a[j].second]) ends.erase(a[j].second);
    }
    if (!isok) {
      break;
    }
  }
  if (isok) {
    printf("YES\n");
  } else {
    printf("NO\n");
  }
}
