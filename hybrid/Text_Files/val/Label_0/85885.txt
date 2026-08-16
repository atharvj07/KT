#include <bits/stdc++.h>
using namespace std;
int II() {
  int q;
  scanf("%d", &q);
  return q;
}
long long LII() {
  long long q;
  scanf("%lld", &q);
  return q;
}
const long long Mx = 100005, K = 22;
long long step, jump;
long long Rank[K][Mx];
struct info {
  long long tup[2], indx;
  bool operator<(const info &a) const {
    return (tup[0] == a.tup[0] ? tup[1] < a.tup[1] : tup[0] < a.tup[0]);
  }
} ar[Mx];
info temp[Mx];
long long cnt[Mx];
void Counting_Sort(long long N) {
  long long mi = -2;
  memset(cnt, 0, sizeof(cnt));
  for (long long i = 0; i < N; i++) {
    cnt[ar[i].tup[1] - mi]++;
  }
  for (long long i = 1; i < Mx; i++) cnt[i] += cnt[i - 1];
  for (long long i = N - 1; i >= 0; i--) {
    temp[--cnt[ar[i].tup[1] - mi]] = ar[i];
  }
  for (long long i = 0; i < N; i++) ar[i] = temp[i];
  memset(cnt, 0, sizeof(cnt));
  for (long long i = 0; i < N; i++) {
    cnt[ar[i].tup[0] - mi]++;
  }
  for (long long i = 1; i < Mx; i++) cnt[i] += cnt[i - 1];
  for (long long i = N - 1; i >= 0; i--) {
    temp[--cnt[ar[i].tup[0] - mi]] = ar[i];
  }
  for (long long i = 0; i < N; i++) ar[i] = temp[i];
}
void Build_Suffix_Array(string s) {
  long long N = s.size();
  for (long long i = 0; i < N; i++) {
    Rank[0][i] = s[i];
  }
  step = 1, jump = 1;
  for (step = 1, jump = 1; jump <= N; step++, jump <<= 1) {
    for (long long i = 0; i < N; i++) {
      ar[i].indx = i;
      ar[i].tup[0] = Rank[step - 1][i];
      ar[i].tup[1] = ((i + jump < N) ? Rank[step - 1][i + jump] : -1);
    }
    Counting_Sort(N);
    Rank[step][ar[0].indx] = 0;
    for (long long i = 1; i < N; i++) {
      Rank[step][ar[i].indx] =
          (ar[i].tup[0] == ar[i - 1].tup[0] && ar[i].tup[1] == ar[i - 1].tup[1])
              ? Rank[step][ar[i - 1].indx]
              : i;
    }
  }
}
vector<long long> LCP(long long N) {
  vector<long long> ans(N, 0);
  for (long long i = 1; i < N; i++) {
    long long x = ar[i].indx, y = ar[i - 1].indx;
    ans[i] = 0;
    for (long long j = step - 1; j >= 0; j--) {
      if (Rank[j][x] == Rank[j][y] && x < N && y < N) {
        ans[i] += (1 << j);
        x += (1 << j);
        y += (1 << j);
      }
    }
  }
  return ans;
}
long long st[K][Mx];
void build(vector<long long> lcp) {
  long long N = lcp.size();
  for (long long i = 0; i < N; i++) {
    st[0][i] = lcp[i];
  }
  for (long long k = 1; k < K; k++) {
    for (long long i = 0; i < N; i++) {
      long long next = i + (1 << k - 1);
      if (next > N) continue;
      st[k][i] = min(st[k - 1][i], st[k - 1][next]);
    }
  }
}
long long get(long long l, long long r) {
  l++;
  long long lg = log2(r - l + 1);
  return min(st[lg][l], st[lg][r - (1 << lg) + 1]);
}
long long find_left(long long l, long long r, long long val) {
  long long re = r, lo = l, hi = r;
  while (lo < hi) {
    long long mid = (lo + hi) / 2;
    if (get(mid, r) >= val) {
      re = mid;
      hi = mid;
    } else
      lo = mid + 1;
  }
  return re;
}
pair<long long, long long> find_right(long long l, long long r, long long val) {
  long long re = l, lo = l, hi = r;
  while (lo < hi) {
    long long mid = (lo + hi + 1) / 2;
    if (get(l, mid) >= val) {
      re = mid;
      lo = mid;
    } else
      hi = mid - 1;
  }
  if (re == l) return {l, -1};
  return {re, get(l, re)};
}
void reset() {
  memset(ar, 0, sizeof(ar));
  memset(st, 0, sizeof(st));
  memset(Rank, 0, sizeof(Rank));
}
void solve() {
  reset();
  string s;
  cin >> s;
  long long N = s.size();
  Build_Suffix_Array(s);
  vector<long long> lcp = LCP((long long)s.size());
  build(lcp);
  long long ans = 0;
  for (long long i = 0; i < N; i++) {
    long long len = N - ar[i].indx;
    long long cur = lcp[i] + 1;
    while (cur <= len) {
      long long RR = Rank[step - 1][ar[i].indx];
      pair<long long, long long> pr = find_right(RR, N - 1, cur);
      if (pr.second == -1) {
        ans += len - cur + 1;
        break;
      } else {
        long long q = pr.first - RR + 1;
        long long qq = pr.second - cur + 1;
        ans += (1LL * (q * (q + 1)) / 2 * qq);
        cur = pr.second + 1;
      }
    }
  }
  cout << ans << endl;
}
int32_t main() {
  long long tt;
  tt = 1;
  long long cas = 1;
  while (tt--) {
    solve();
  }
}
