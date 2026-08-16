#include <bits/stdc++.h>
using namespace std;
void add(int &a, int b, int p) { a = (a + b) % p; }
int mul(int a, int b, int p) { return a * b % p; }
int getid(char c) {
  if (c >= '0' && c <= '9') return c - '0';
  assert(c >= 'A' && c <= 'F');
  return c - 'A' + 10;
}
const int MAXD = 16;
const int MAXN = 1e4;
const int MSZ = 4;
const long long MMSK = (1 << MSZ) - 1;
struct Req {
  int d;
  long long msk, mval, c;
  bool bad;
};
long long ids[MAXD + 1][MAXN];
int main() {
  vector<int> ps;
  for (int i = 2; i <= 100; i++) {
    bool g = true;
    for (int i2 = 2; i2 * i2 <= i; i2++)
      if (i % i2 == 0) g = false;
    if (!g) continue;
    ps.push_back(i);
  }
  for (int d = 2; d <= MAXD; d++) {
    for (int i = 0; i < MAXN; i++) {
      vector<int> ds;
      int x = i;
      for (; x; x /= d) ds.push_back(x % d);
      long long &msk = ids[d][i] = 0;
      for (int i2 = 0; i2 < ((int)(ds).size()); i2++)
        msk |= (long long)ds[i2] << (MSZ * i2);
    }
  }
  int n, m;
  while (scanf("%d", &n) >= 1) {
    vector<long long> as(n);
    vector<vector<long long> > asp(n);
    for (int i = 0; i < n; i++) {
      scanf("%I64d", &as[i]);
      for (int i2 = 0; i2 < ((int)(ps).size()); i2++)
        asp[i].push_back(as[i] % ps[i2]);
    }
    scanf("%d", &m);
    vector<set<long long> > msks(MAXD + 1);
    vector<Req> rqs(m);
    for (int i = 0; i < m; i++) {
      int &d = rqs[i].d;
      char _s[31];
      scanf("%d%s%I64d", &d, _s, &rqs[i].c);
      string s = _s;
      while (s.length() < 14) s = "0" + s;
      int i2 = 0;
      int pos = s.length() - 1;
      bool &bad = rqs[i].bad = false;
      while (pos >= 14) {
        if (s[i2] != '?' && s[i2] != '0') {
          bad = true;
          break;
        }
        i2++;
        pos--;
      }
      if (bad) continue;
      long long &msk = rqs[i].msk, &mval = rqs[i].mval;
      for (i2 = 0; s[i2]; i2++, pos--)
        if (s[i2] != '?') {
          msk |= MMSK << (MSZ * pos);
          mval |= (long long)getid(s[i2]) << (MSZ * pos);
        }
      fprintf(stderr, "mval=%I64d\n", mval);
      msks[d].insert(msk);
    }
    fprintf(stderr, "read\n");
    vector<map<long long, map<long long, vector<int> > > > pcs(MAXD + 1);
    for (int d = 2; d <= MAXD; d++) {
      fprintf(stderr, "d=%d %d\n", d, ((int)(msks[d]).size()));
      for (set<long long>::iterator it = msks[d].begin(); it != msks[d].end();
           it++) {
        long long msk = *it;
        map<long long, vector<int> > &cnts = pcs[d][msk];
        for (int i = 0; i < n; i++) {
          vector<int> &ccnt = cnts[ids[d][i] & msk];
          if (ccnt.empty()) {
            ccnt = vector<int>(((int)(ps).size()), 1);
          }
          for (int i2 = 0; i2 < ((int)(ccnt).size()); i2++)
            ccnt[i2] = mul(ccnt[i2], asp[i][i2], ps[i2]);
        }
      }
    }
    fprintf(stderr, "go\n");
    for (int i = 0; i < m; i++) {
      vector<int> cps(((int)(ps).size()));
      for (int i2 = 0; i2 < ((int)(ps).size()); i2++)
        cps[i2] = rqs[i].c % ps[i2];
      vector<int> nps(((int)(ps).size()), 1);
      if (!rqs[i].bad) {
        map<long long, vector<int> > &cnts = pcs[rqs[i].d][rqs[i].msk];
        const vector<int> &res = cnts[rqs[i].mval];
        if (!res.empty()) nps = res;
      }
      for (int i2 = 0; i2 < ((int)(ps).size()); i2++)
        add(cps[i2], nps[i2], ps[i2]);
      int ans = -1;
      for (int i2 = 0; i2 < ((int)(ps).size()); i2++)
        if (!cps[i2]) {
          ans = ps[i2];
          break;
        }
      printf("%d\n", ans);
    }
    fprintf(stderr, "end\n");
  }
  return 0;
}
