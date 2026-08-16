#include <bits/stdc++.h>
using namespace std;
std::mt19937 rnd(
    (int)std::chrono::steady_clock::now().time_since_epoch().count());
long long gcd(long long a, long long b) { return b == 0 ? a : gcd(b, a % b); }
const int NDIG = 6;
const int MAXQ = 100000;
const int MAXSUM = 999999;
int nvals;
int gain[NDIG];
int nq;
int q[MAXQ];
long long qans[MAXQ];
long long dp[NDIG + 1][MAXSUM + 1];
long long tmp[MAXSUM + 1];
pair<long long, int> qq[MAXSUM + 1];
int qhead, qtail;
void solve() {
  for (int ndig = (0); ndig <= (NDIG); ++ndig)
    for (int sum = (0); sum <= (MAXSUM); ++sum)
      dp[ndig][sum] = ndig == 0 && sum == 0 ? 0 : LLONG_MIN;
  for (int ndig = (1); ndig <= (NDIG); ++ndig) {
    int curgain = gain[NDIG - ndig];
    long long vargain = (long long)10 * curgain;
    for (int sum = (0); sum <= (MAXSUM); ++sum)
      tmp[sum] = dp[ndig - 1][sum] == LLONG_MIN
                     ? LLONG_MIN
                     : dp[ndig - 1][sum] - (sum / 3) * vargain;
    for (int mod = (0); mod < (30); ++mod)
      if (mod <= 9 * nvals) {
        long long fixedgain = (long long)(mod / 3) * curgain;
        qhead = qtail = 0;
        for (int sum = mod; sum <= MAXSUM; sum += 10) {
          int fst = (sum - mod) / 10;
          int qmx = min((sum - mod) / 30, (9 * nvals - mod) / 30);
          long long now = tmp[fst];
          while (qtail < qhead && now >= qq[qhead - 1].first) --qhead;
          qq[qhead++] = make_pair(now, fst);
          while (qtail < qhead && qq[qtail].second < fst - (qmx - 10)) ++qtail;
          long long best = qtail < qhead ? qq[qtail].first : LLONG_MIN;
          if (best != LLONG_MIN) {
            dp[ndig][sum] =
                max(dp[ndig][sum], best + fixedgain + (fst / 3) * vargain);
          }
          for (int q = (max(0, qmx - 10)); q <= (qmx); ++q) {
            long long opt = dp[ndig - 1][fst - 3 * q];
            if (opt == LLONG_MIN) continue;
            int nthree = mod / 3 + 10 * q;
            opt += fixedgain + q * vargain;
            if (nthree >= 3 * (nvals - 1) && mod % 3 != 0)
              opt -= (long long)(nthree - 3 * (nvals - 1)) * curgain;
            dp[ndig][sum] = max(dp[ndig][sum], opt);
          }
        }
      }
  }
  for (int i = (0); i < (nq); ++i) qans[i] = dp[NDIG][q[i]];
}
void run() {
  scanf("%d", &nvals);
  for (int i = (0); i < (NDIG); ++i) scanf("%d", &gain[i]);
  scanf("%d", &nq);
  for (int i = (0); i < (nq); ++i) scanf("%d", &q[i]);
  solve();
  for (int i = (0); i < (nq); ++i) printf("%lld\n", qans[i]);
}
long long qansstupid[MAXQ];
void solvestupid() {
  auto calc = [&](int x) {
    long long ret = 0;
    for (int i = 0; x > 0; ++i, x /= 10)
      if (x % 10 % 3 == 0) ret += (long long)(x % 10 / 3) * gain[i];
    return ret;
  };
  for (int i = (0); i < (nq); ++i) {
    int sum = q[i];
    qansstupid[i] = LLONG_MIN;
    if (nvals == 4) {
      for (int a = (0); a <= (sum); ++a)
        for (int b = (0); b <= (sum - a); ++b)
          for (int c = (0); c <= (sum - a - b); ++c) {
            int d = sum - a - b - c;
            long long cur = calc(a) + calc(b) + calc(c) + calc(d);
            qansstupid[i] = max(qansstupid[i], cur);
          }
    } else if (nvals == 3) {
      for (int a = (0); a <= (sum); ++a)
        for (int b = (0); b <= (sum - a); ++b) {
          int c = sum - a - b;
          long long cur = calc(a) + calc(b) + calc(c);
          qansstupid[i] = max(qansstupid[i], cur);
        }
    } else if (nvals == 2) {
      for (int a = (0); a <= (sum); ++a) {
        int b = sum - a;
        long long cur = calc(a) + calc(b);
        qansstupid[i] = max(qansstupid[i], cur);
      }
    } else if (nvals == 1) {
      int a = sum;
      long long cur = calc(a);
      qansstupid[i] = max(qansstupid[i], cur);
    } else {
      assert(false);
    }
  }
}
void stress() {
  for (int rep = (0); rep < (1000); ++rep) {
    nvals = rnd() % 4 + 1;
    int sum = rnd() % (nvals == 4 ? 100 : 10000) + 1;
    for (int i = (0); i < (NDIG); ++i) gain[i] = rnd() % 1000 + 1;
    nq = 1, q[0] = sum;
    solve();
    solvestupid();
    bool ok = true;
    for (int i = (0); i < (nq); ++i)
      if (qans[i] != qansstupid[i]) ok = false;
    if (ok) {
      printf(".");
      continue;
    }
    printf("err have=%lld want=%lld\n", qans[0], qansstupid[0]);
    printf("%d\n", nvals);
    for (int i = (0); i < (NDIG); ++i) {
      if (i != 0) printf(" ");
      printf("%d", gain[i]);
    }
    puts("");
    printf("%d\n", nq);
    for (int i = (0); i < (nq); ++i) printf("%d\n", q[i]);
  }
}
int main() {
  run();
  return 0;
}
