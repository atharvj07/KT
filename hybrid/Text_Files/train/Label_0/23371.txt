#include <bits/stdc++.h>
using namespace std;
class SegmentTree {
 public:
  vector<vector<long long> > a;
  long long n;
  SegmentTree(vector<long long>& arr) {
    n = arr.size();
    a.resize(4 * n);
    build(1, 0, arr.size(), arr);
  }
  void build(long long v, long long vl, long long vr, vector<long long>& arr) {
    if (vr - vl == 1) {
      a[v].push_back(arr[vl]);
    } else {
      long long vm = (vl + vr) / 2;
      build(v * 2, vl, vm, arr);
      build(v * 2 + 1, vm, vr, arr);
      a[v].resize(vr - vl);
      merge(a[v * 2].begin(), a[v * 2].end(), a[v * 2 + 1].begin(),
            a[v * 2 + 1].end(), a[v].begin());
    }
  }
  long long get(long long v, long long vl, long long vr, long long l,
                long long r, long long x) {
    if (vl == l && vr == r) {
      return a[v].end() - lower_bound(a[v].begin(), a[v].end(), x);
    } else {
      long long vm = (vl + vr) / 2;
      if (r <= vm) {
        return get(v * 2, vl, vm, l, r, x);
      } else if (l >= vm) {
        return get(v * 2 + 1, vm, vr, l, r, x);
      } else {
        return get(v * 2, vl, vm, l, vm, x) + get(v * 2 + 1, vm, vr, vm, r, x);
      }
    }
  }
  long long get(long long l, long long r, long long x) {
    return get(1, 0, n, l, r, x);
  }
};
signed main() {
  long long n;
  cin >> n;
  vector<long long> a(n);
  for (long long i = 0; i < n; i++) {
    cin >> a[i];
  }
  vector<long long> nums = a;
  sort(nums.begin(), nums.end());
  nums.erase(unique(nums.begin(), nums.end()), nums.end());
  vector<vector<long long> > posof(nums.size());
  for (long long i = 0; i < n; i++) {
    posof[lower_bound(nums.begin(), nums.end(), a[i]) - nums.begin()].push_back(
        i);
  }
  vector<long long> sufcntof(posof.size());
  sufcntof.back() = posof.back().size();
  for (long long i = (long long)posof.size() - 2; i >= 0; i--) {
    sufcntof[i] = sufcntof[i + 1] + posof[i].size();
  }
  SegmentTree st(a);
  long long m;
  cin >> m;
  for (long long i = 0; i < m; i++) {
    long long k, pos;
    cin >> k >> pos;
    long long numpos = sufcntof.rend() -
                       lower_bound(sufcntof.rbegin(), sufcntof.rend(), k) - 1;
    long long num = nums[numpos];
    long long limit =
        k - (numpos == sufcntof.size() - 1 ? 0 : sufcntof[numpos + 1]);
    long long l = 0;
    long long r = n;
    while (r - l > 1) {
      long long m = (l + r) / 2;
      long long c = st.get(0, m + 1, num + 1);
      c += min((long long)(lower_bound(posof[numpos].begin(),
                                       posof[numpos].end(), m + 1) -
                           posof[numpos].begin()),
               limit);
      if (c >= pos) {
        r = m;
      } else {
        l = m;
      }
    }
    long long m = l;
    long long c = st.get(0, m + 1, num + 1);
    c += min((long long)(lower_bound(posof[numpos].begin(), posof[numpos].end(),
                                     m + 1) -
                         posof[numpos].begin()),
             limit);
    if (c >= pos) {
      r = m;
    }
    cout << a[r] << "\n";
  }
  return 0;
}
