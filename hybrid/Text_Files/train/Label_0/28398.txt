#include <bits/stdc++.h>
using namespace std;
template <typename T>
void maxtt(T& t1, T t2) {
  t1 = max(t1, t2);
}
template <typename T>
void mintt(T& t1, T t2) {
  t1 = min(t1, t2);
}
bool debug = 0;
int n, m, k;
string direc = "URDL";
const long long MOD2 = (long long)1000000007 * (long long)1000000007;
long long ln, lk, lm;
void etp(bool f = 0) {
  puts(f ? "YES" : "NO");
  exit(0);
}
void addmod(int& x, int y, int mod = 1000000007) {
  x += y;
  if (x >= mod) x -= mod;
  if (x < 0) x += mod;
  assert(x >= 0 && x < mod);
}
void et(int x = -1) {
  printf("%d\n", x);
  exit(0);
}
long long fastPow(long long x, long long y, int mod = 1000000007) {
  long long ans = 1;
  while (y > 0) {
    if (y & 1) ans = (x * ans) % mod;
    x = x * x % mod;
    y >>= 1;
  }
  return ans;
}
long long gcd1(long long x, long long y) { return y ? gcd1(y, x % y) : x; }
clock_t start = clock();
double runt() { return ((double)(clock() - start)) / CLOCKS_PER_SEC; }
vector<int> mp[500135], path, ans, vp[2];
bool vis[500135], sv[500135];
int A, fa[500135], u[500135], v[500135], id[500135];
void clr() {
  for (int(i) = 1; (i) <= (int)(n); (i)++) {
    mp[i].clear();
    vis[i] = 0;
    sv[i] = 0;
  }
}
void dfs2(int x, int pa) {
  vis[x] = 1;
  if (runt() > 1) exit(0);
  path.push_back(x);
  for (int c : mp[x])
    if (c != pa) {
      if (!vis[c] && mp[c].size() % 3 == 2)
        dfs2(c, x);
      else if (vis[c]) {
        while (path.back() != c) {
          ans.push_back(path.back());
          path.pop_back();
        }
        ans.push_back(c);
        throw 1;
      }
    }
  path.pop_back();
}
void dfsc(int x) {
  vis[x] = 1;
  for (int c : mp[x])
    if (!vis[c]) dfsc(c);
}
void ppt() {
  if (debug) return;
  vector<int> vv;
  for (int(i) = 1; (i) <= (int)(n); (i)++)
    if (!sv[i]) vv.push_back(i);
  if (vv.empty()) {
    puts("No");
    return;
  }
  puts("Yes");
  printf("%d\n", vv.size());
  for (int z : vv) printf("%d ", z);
  puts("");
}
void bfs(int st) {
  vector<bool> dp(n + 5, 0);
  for (int(i) = 1; (i) <= (int)(n); (i)++) fa[i] = 0;
  queue<int> q;
  q.push(st);
  vis[st] = 1;
  dp[st] = 1;
  while (!q.empty()) {
    int x = q.front();
    q.pop();
    for (int c : mp[x])
      if (!dp[c]) {
        if (c == A) {
          if (x != st) {
            for (int z = x; z; z = fa[z]) {
              if (sv[z] == 1) break;
              sv[z] = 1;
            }
            dfsc(st);
            return;
          }
          continue;
        }
        fa[c] = x;
        q.push(c);
        dp[c] = 1;
      }
  }
}
void fmain(int tid) {
  scanf("%d%d", &n, &m);
  for (int(i) = 1; (i) <= (int)(m); (i)++) {
    scanf("%d%d", u + i, v + i);
    mp[u[i]].push_back(v[i]);
    mp[v[i]].push_back(u[i]);
  }
  if (debug && tid == 520) {
    printf("%d %d\n", n, m);
    for (int(i) = 1; (i) <= (int)(m); (i)++) printf("%d %d\n", u[i], v[i]);
    exit(0);
  }
  vector<int> ones;
  for (int(i) = 1; (i) <= (int)(n); (i)++) {
    if (mp[i].size() % 3 == 0) {
      sv[i] = 1;
      ppt();
      return;
    } else if (mp[i].size() % 3 == 1)
      ones.push_back(i);
  }
  for (int(i) = 1; (i) <= (int)(n); (i)++)
    if (mp[i].size() % 3 == 2 && !vis[i]) {
      path.clear();
      ans.clear();
      try {
        dfs2(i, 0);
      } catch (int ee) {
        for (int(i) = 1; (i) <= (int)(n); (i)++) id[i] = -1;
        for (int(j) = 0; (j) < (int)(ans.size()); (j)++) id[ans[j]] = j;
        int N = ans.size();
        int st = 0, ed = N - 1;
        for (int(j) = 1; (j) <= (int)(m); (j)++)
          if (id[u[j]] != -1 && id[v[j]] != -1) {
            int x = id[u[j]], y = id[v[j]];
            if (y < x) swap(x, y);
            if (x + 1 == y) continue;
            if (y == N - 1 && x == 0) continue;
            if (y - x < ed - st) {
              st = x;
              ed = y;
            }
            if (x + N - y < ed - st) {
              st = y;
              ed = x + N;
            }
          }
        for (int j = st;; j++) {
          sv[ans[j % N]] = 1;
          if (j == ed) break;
        }
        ppt();
        return;
      }
    }
  if (ones.size() >= 2) {
    A = ones[0];
    int B = -1;
    for (int(i) = 1; (i) <= (int)(n); (i)++) vis[i] = 0;
    vis[A] = 1;
    queue<int> q;
    q.push(A);
    while (!q.empty() && B == -1) {
      int x = q.front();
      q.pop();
      for (int c : mp[x])
        if (!vis[c]) {
          fa[c] = x;
          q.push(c);
          vis[c] = 1;
          if (mp[c].size() % 3 == 1) {
            B = c;
            break;
          }
        }
    }
    sv[A] = 1;
    for (int x = B; x != A; x = fa[x]) {
      if (sv[x] == 1) break;
      sv[x] = 1;
    }
    ppt();
    return;
  }
  for (int(i) = 1; (i) <= (int)(n); (i)++) vis[i] = 0;
  for (int(j) = 0; (j) < (int)(2); (j)++) vp[j].clear();
  A = ones[0];
  vis[A] = 1;
  bfs(mp[A][0]);
  for (int c : mp[A])
    if (!vis[c]) {
      bfs(c);
      break;
    }
  sv[A] = 1;
  ppt();
}
int main() {
  int t = 1;
  scanf("%d", &t);
  for (int(i) = 1; (i) <= (int)(t); (i)++) {
    fmain(i);
    clr();
  }
  return 0;
}
