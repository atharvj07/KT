#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:67108864")
using namespace std;
inline long long FastMax(long long x, long long y) {
  return (((y - x) >> (32 - 1)) & (x ^ y)) ^ y;
}
inline long long FastMin(long long x, long long y) {
  return (((y - x) >> (32 - 1)) & (x ^ y)) ^ x;
}
long long N, Q;
long long A[1000007 + 7];
map<long long, long long> mp;
vector<long long> wh;
vector<pair<long long, pair<long long, long long> > > qr;
long long BIT_vol[1000007 + 7];
long long BIT_cnt[1000007 + 7];
void Update(long long *B, long long I, long long v) {
  while (I and I <= 1000007) {
    B[I] += v;
    I += I & -I;
  }
}
long long Find(long long *B, long long I) {
  long long s = 0;
  while (I) {
    s += B[I];
    I -= I & -I;
  }
  return s;
}
bool isPos(long long I, long long v, double &ans) {
  long long c = Find(BIT_cnt, I);
  long long tot = Find(BIT_vol, I);
  long long Lim = wh[I] * c - tot;
  if (Lim > v) {
    ans = min(ans, (double)wh[I]);
    return true;
  } else {
    ans = min(ans, wh[I] + (1.0 * v - Lim) / c);
    return false;
  }
}
int main(void) {
  long long i, j, t, p, x, v, Icase, k = 0;
  scanf("%I64d%I64d", &N, &Q);
  mp[-1] = mp[0] = mp[1000000007] = 0;
  for (i = 1; i <= N; i++) {
    scanf("%I64d", &A[i]);
    mp[A[i]] = 0;
  }
  for (i = 1; i <= Q; i++) {
    scanf("%I64d", &t);
    if (t == 1) {
      scanf("%I64d%I64d", &p, &x);
      qr.push_back(make_pair(1, make_pair(p, x)));
      mp[x] = 0;
    } else {
      scanf("%I64d", &v);
      qr.push_back(make_pair(2, make_pair(v, 0)));
    }
  }
  map<long long, long long>::iterator it = mp.begin();
  i = 0;
  while (it != mp.end()) {
    it->second = i;
    wh.push_back(it->first);
    i++;
    it++;
  }
  for (i = 1; i <= N; i++) {
    Update(BIT_vol, mp[A[i]], A[i]);
    Update(BIT_cnt, mp[A[i]], 1);
  }
  for (i = 0; i < qr.size(); i++) {
    t = qr[i].first;
    if (t == 1) {
      p = qr[i].second.first;
      x = qr[i].second.second;
      Update(BIT_vol, mp[A[p]], -A[p]);
      Update(BIT_cnt, mp[A[p]], -1);
      A[p] = x;
      Update(BIT_vol, mp[A[p]], A[p]);
      Update(BIT_cnt, mp[A[p]], 1);
    } else {
      v = qr[i].second.first;
      long long lo = 1, hi = mp.size();
      double ans = 1e17;
      while (lo <= hi) {
        long long mid = (lo + hi) / 2;
        if (isPos(mid, v, ans))
          hi = mid - 1;
        else
          lo = mid + 1;
      }
      printf("%.7lf\n", ans);
    }
  }
  return 0;
}
