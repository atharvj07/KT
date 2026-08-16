#include <bits/stdc++.h>
using namespace std;
template <class T>
int chkmax(T& a, T b) {
  if (b > a) {
    a = b;
    return 1;
  }
  return 0;
}
template <class T>
int chkmin(T& a, T b) {
  if (b < a) {
    a = b;
    return 1;
  }
  return 0;
}
template <class iterator>
void output(iterator begin, iterator end, ostream& out = cerr) {
  while (begin != end) {
    out << (*begin) << " ";
    begin++;
  }
  out << endl;
}
template <class T>
void output(T x, ostream& out = cerr) {
  output(x.begin(), x.end(), out);
}
void fast_io() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
}
struct segment {
  int l, r;
  segment(int _l, int _r) : l(_l), r(_r) {}
};
const int mx = 2e5 + 228;
int n;
long long a[mx];
vector<segment> blocks;
void read() {
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    cin >> a[i];
  }
  reverse(a + 1, a + n + 1);
}
void build_blocks() {
  int r = -1, l = -1;
  for (int i = 1; i <= n; ++i) {
    if (a[i]) {
      if (r != -1 && a[i] >= a[r]) {
        r = i;
      } else {
        if (r != -1) {
          blocks.emplace_back(l, r);
        }
        l = r = i;
      }
    }
  }
  if (r != -1) {
    blocks.emplace_back(l, r);
  }
}
const long long BINF = 1e18;
const int INF = 1e9 + 228;
int dp[mx][2], ans[mx], trans_j[mx][2];
long long dp_t[mx][2];
vector<long long> restore_can;
long long min_pref(long long l, long long to_check) {
  return l * to_check + to_check * (to_check - 1) / 2;
}
int can(long long l, long long r, long long target, int restore = 0) {
  long long L = 0, R = (r - l + 1);
  while (L < R) {
    long long mid = (L + R) >> 1;
    long long to_check = mid + 1;
    if (min_pref(l, to_check) <= target) {
      L = mid + 1;
    } else {
      R = mid;
    }
  }
  long long k = L;
  long long lb = min_pref(l, k);
  long long max_delta = (r - l + 1) - k;
  long long rb = lb + k * max_delta;
  if (lb <= target && target <= rb) {
    if (restore) {
      restore_can.clear();
      for (long long i = k - 1; i >= 0; --i) {
        restore_can.push_back(l + i);
      }
      long long rem = target - lb;
      for (int i = 0; i < k; ++i) {
        long long delta = min(max_delta, rem);
        rem -= delta;
        restore_can[i] += delta;
      }
    }
    return 1;
  } else {
    return 0;
  }
}
namespace ans_checker {
long long c[mx], b[mx], t[mx], sum[mx];
void check() {
  c[0] = 1;
  for (int i = 1; i <= n; ++i) {
    c[i] = ans[i];
  }
  int ptr = 0;
  for (int i = 0; i <= n; ++i) {
    if (c[i]) {
      ptr = i;
    }
    b[i] = ptr;
  }
  for (int i = n; i >= 0; --i) {
    sum[i] = sum[i + 1] + (c[i] ? i : 0);
  }
  for (int i = 1; i <= n; ++i) {
    t[i] = sum[b[i]] + (1 - c[i]);
    assert(a[i] == 0 || t[i] == a[i]);
  }
}
};  // namespace ans_checker
void restore(int i, int put) {
  assert(dp[i][put] != -INF);
  if (i == blocks.size()) {
    ans_checker::check();
    reverse(ans + 1, ans + n + 1);
    for (int it = 1; it <= n; ++it) {
      cout << ans[it];
    }
    cout << endl;
    exit(0);
  }
  int j = trans_j[i][put];
  long long T1 = a[blocks[i].l] - (dp[i][put] != blocks[i].l);
  long long T2 = dp_t[i + 1][j];
  long long target_sum = T1 - dp[i][put] - T2;
  ans[dp[i][put]] = 1;
  can(blocks[i].r + 1, dp[i + 1][j] - 1, target_sum, 1);
  for (auto id : restore_can) {
    ans[id] = 1;
  }
  restore(i + 1, j);
}
void calc_dp() {
  if (blocks.size() == 0) {
    restore(0, 0);
  }
  for (int j = 0; j < 2; ++j) {
    dp[blocks.size()][j] = n + 1;
  }
  for (int i = (int)blocks.size() - 1; i >= 1; --i) {
    int alive = 0;
    long long max_el = -BINF, min_el = BINF;
    for (int j = blocks[i].l; j <= blocks[i].r; ++j) {
      if (a[j] > 0) {
        alive++;
        chkmax(max_el, a[j]);
        chkmin(min_el, a[j]);
      }
    }
    for (int jp = 0; jp < 2; ++jp) {
      dp[i][jp] = -INF;
      if (max_el != min_el && jp == 0) {
        continue;
      }
      if (max_el == min_el && alive > 1 && jp == 1) {
        continue;
      }
      for (int j = 0; j < 2; ++j) {
        if (dp[i + 1][j] == -INF) {
          continue;
        }
        int opt_b = blocks[i].l - (1 - jp);
        int worst_b = (jp == 0 ? blocks[i - 1].r + 1 : blocks[i].l);
        for (int new_dp_val = opt_b; new_dp_val >= worst_b; --new_dp_val) {
          long long T1 = a[blocks[i].l] - (new_dp_val != blocks[i].l);
          long long T2 = dp_t[i + 1][j];
          long long target_sum = T1 - new_dp_val - T2;
          if (can(blocks[i].r + 1, dp[i + 1][j] - 1, target_sum)) {
            if (chkmax(dp[i][jp], new_dp_val)) {
              dp_t[i][jp] = T1;
              trans_j[i][jp] = j;
            }
            break;
          }
        }
      }
    }
  }
  long long lseg_val = -1, uniq_val = -1;
  int uniq_pos = -1;
  for (int i = blocks[0].l; i <= blocks[0].r; ++i) {
    chkmax(lseg_val, a[i]);
  }
  for (int i = blocks[0].l; i <= blocks[0].r; ++i) {
    if (a[i] && a[i] != lseg_val) {
      uniq_val = a[i];
      uniq_pos = i;
    }
  }
  for (int j = 0; j < 2; ++j) {
    if (dp[1][j] == -INF) {
      continue;
    }
    int L = blocks[0].r + 1;
    int R = dp[1][j] - 1;
    int alive = 0;
    for (int j = blocks[0].l; j <= blocks[0].r; ++j) {
      if (a[j] > 0) {
        alive++;
      }
    }
    for (int where = 0; where <= blocks[0].r; ++where) {
      if (uniq_pos == -1 && a[where] && blocks[0].l != blocks[0].r) {
        continue;
      }
      if (uniq_pos != -1 && where != uniq_pos) {
        continue;
      }
      long long target_sum = lseg_val - 1 + (alive == 1 && a[where] > 0);
      long long rsum = target_sum - where - dp_t[1][j];
      if (can(L, R, rsum)) {
        ans[where] = 1;
        can(L, R, rsum, 1);
        for (auto id : restore_can) {
          ans[id] = 1;
        }
        restore(1, j);
      }
    }
  }
  assert(0);
}
signed main() {
  fast_io();
  read();
  build_blocks();
  calc_dp();
}
