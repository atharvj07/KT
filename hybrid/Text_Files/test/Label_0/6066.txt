#include<bits/stdc++.h>

using namespace std;

struct SuffixArray
{
  vector< int > SA;
  string s;

  void Build_SA(const string &str)
  {
    s = str;
    SA.resize(s.size());
    iota(begin(SA), end(SA), 0);
    sort(begin(SA), end(SA), [&](const int &a, const int &b)
    {
      if(s[a] == s[b]) return (a > b);
      return (s[a] < s[b]);
    });
    vector< int > classes(s.size()), c(s.size()), cnt(s.size());
    for(int i = 0; i < s.size(); i++) {
      c[i] = s[i];
    }
    for(int len = 1; len < s.size(); len <<= 1) {
      for(int i = 0; i < s.size(); i++) {
        if(i > 0 && c[SA[i - 1]] == c[SA[i]] && SA[i - 1] + len < s.size() && c[SA[i - 1] + len / 2] == c[SA[i] + len / 2]) {
          classes[SA[i]] = classes[SA[i - 1]];
        } else {
          classes[SA[i]] = i;
        }
      }
      iota(begin(cnt), end(cnt), 0);
      copy(begin(SA), end(SA), begin(c));
      for(int i = 0; i < s.size(); i++) {
        int s1 = c[i] - len;
        if(s1 >= 0) SA[cnt[classes[s1]]++] = s1;
      }
      classes.swap(c);
    }
  }

  int operator[](int k) const
  {
    return (SA[k]);
  }

  int size() const
  {
    return (s.size());
  }

  bool lt_substr(string &t, int si = 0, int ti = 0)
  {
    int sn = s.size(), tn = t.size();
    while(si < sn && ti < tn) {
      if(s[si] < t[ti]) return (true);
      if(s[si] > t[ti]) return (false);
      ++si, ++ti;
    }
    return (si >= sn && ti < tn);
  }

  int lower_bound(string &t)
  {
    int low = -1, high = SA.size();
    while(high - low > 1) {
      int mid = (low + high) >> 1;
      if(lt_substr(t, SA[mid])) low = mid;
      else high = mid;
    }
    return (high);
  }

  pair< int, int > lower_upper_bound(string &t)
  {
    int idx = lower_bound(t);
    int low = idx - 1, high = SA.size();
    t.back()++;
    while(high - low > 1) {
      int mid = (low + high) >> 1;
      if(lt_substr(t, SA[mid])) low = mid;
      else high = mid;
    }
    t.back()--;
    return (make_pair(idx, high));
  }

  void output()
  {
    for(int i = 0; i < size(); i++) {
      cout << i << ": " << s.substr(SA[i]) << endl;
    }
  }
};

struct SuccinctIndexableDictionary
{
  size_t length;
  size_t blocks;
  vector< unsigned > bit, sum;

  SuccinctIndexableDictionary()
  {
  }

  SuccinctIndexableDictionary(size_t _length)
  {
    length = _length;
    blocks = (length + 31) >> 5;
    bit.assign(blocks, 0U);
    sum.assign(blocks, 0U);
  }

  void set(int k)
  {
    bit[k >> 5] |= 1U << (k & 31);
  }

  void build()
  {
    sum[0] = 0U;
    for(int i = 1; i < blocks; i++) {
      sum[i] = sum[i - 1] + __builtin_popcount(bit[i - 1]);
    }
  }

  bool operator[](int k) const
  {
    return (bool((bit[k >> 5] >> (k & 31)) & 1));
  }

  int rank(int k)
  {
    return (sum[k >> 5] + __builtin_popcount(bit[k >> 5] & ((1U << (k & 31)) - 1)));
  }

  int rank(bool val, int k)
  {
    return (val ? rank(k) : k - rank(k));
  }

  int select(bool val, int k)
  {
    if(k < 0 || rank(val, length) <= k) return (-1);
    int low = 0, high = length;
    while(high - low > 1) {
      int mid = (low + high) >> 1;
      if(rank(val, mid) >= k + 1) high = mid;
      else low = mid;
    }
    return (high - 1);
  }

  int select(bool val, int i, int l)
  {
    return select(val, i + rank(val, l));
  }
};

template< class T, int MAXLOG >
struct WaveletMatrix
{
  size_t length;
  SuccinctIndexableDictionary matrix[MAXLOG];
  int zs[MAXLOG];
  int buff1[MAXLOG], buff2[MAXLOG];

  void max_dfs(int d, int l, int r, int &k, T val, vector< T > &vs)
  {
    if(l >= r || !k) return;
    if(d == MAXLOG) {
      while(l++ < r && k > 0) vs.push_back(val), k--;
      return;
    }
    int lc = matrix[d].rank(1, l), rc = matrix[d].rank(1, r);
    max_dfs(d + 1, lc + zs[d], rc + zs[d], k, 1ULL << (MAXLOG - d - 1) | val, vs);
    max_dfs(d + 1, l - lc, r - rc, k, val, vs);
  }

  T max_dfs(int d, int l, int r, T val, T a, T b)
  {
    if(r - l <= 0 || val >= b) return -1;
    if(d == MAXLOG) return val >= a ? val : -1;
    int lc = matrix[d].rank(1, l), rc = matrix[d].rank(1, r);
    T ret = max_dfs(d + 1, lc + zs[d], rc + zs[d], 1ULL << (MAXLOG - d - 1) | val, a, b);
    if(~ret) return ret;
    return max_dfs(d + 1, l - lc, r - rc, val, a, b);
  }

  int freq_dfs(int d, int l, int r, T val, T a, T b)
  {
    if(l == r) return 0;
    if(d == MAXLOG) return (a <= val && val < b) ? r - l : 0;
    T nv = 1ULL << (MAXLOG - d - 1) | val, nnv = ((1ULL << (MAXLOG - d - 1)) - 1) | nv;
    if(nnv < a || b <= val) return 0;
    if(a <= val && nnv < b) return r - l;
    int lc = matrix[d].rank(1, l), rc = matrix[d].rank(1, r);
    return freq_dfs(d + 1, l - lc, r - rc, val, a, b) +
           freq_dfs(d + 1, lc + zs[d], rc + zs[d], nv, a, b);
  }

  void list_dfs(int d, int l, int r, T val, T a, T b, vector< pair< T, int>> &vs)
  {
    if(val >= b || r - l <= 0) return;
    if(d == MAXLOG) {
      if(a <= val) vs.push_back(make_pair(val, r - l));
      return;
    }
    T nv = val | (1LL << (MAXLOG - d - 1)), nnv = nv | (((1LL << (MAXLOG - d - 1)) - 1));
    if(nnv < a) return;
    int lc = matrix[d].rank(1, l), rc = matrix[d].rank(1, r);
    list_dfs(d + 1, l - lc, r - rc, val, a, b, vs);
    list_dfs(d + 1, lc + zs[d], rc + zs[d], nv, a, b, vs);
  }


  WaveletMatrix(vector< T > data)
  {
    length = data.size();
    vector< T > l(length), r(length);
    for(int depth = 0; depth < MAXLOG; depth++) {
      matrix[depth] = SuccinctIndexableDictionary(length + 1);
      int left = 0, right = 0;
      for(int i = 0; i < length; i++) {
        bool k = (data[i] >> (MAXLOG - depth - 1)) & 1;
        if(k) r[right++] = data[i], matrix[depth].set(i);
        else l[left++] = data[i];
      }
      zs[depth] = left;
      matrix[depth].build();
      swap(l, data);
      for(int i = 0; i < right; i++) data[left + i] = r[i];
    }
  }

  T access(int k)
  {
    int ret = 0;
    bool bit;
    for(int depth = 0; depth < MAXLOG; depth++) {
      bit = matrix[depth][k];
      ret = (ret << 1) | bit;
      k = matrix[depth].rank(bit, k) + zs[depth] * bit;
    }
    return (ret);
  }

  int rank(T val, int k)
  {
    int l = 0, r = k;
    for(int depth = 0; depth < MAXLOG; depth++) {
      buff1[depth] = l, buff2[depth] = r;
      bool bit = (val >> (MAXLOG - depth - 1)) & 1;
      l = matrix[depth].rank(bit, l) + zs[depth] * bit;
      r = matrix[depth].rank(bit, r) + zs[depth] * bit;
    }
    return (r - l);
  }

  int select(T val, int kth)
  {
    rank(val, length);
    for(int depth = MAXLOG - 1; depth >= 0; depth--) {
      bool bit = (val >> (MAXLOG - depth - 1)) & 1;
      kth = matrix[depth].select(bit, kth, buff1[depth]);
      if(kth >= buff2[depth] || kth < 0) return (-1);
      kth -= buff1[depth];
    }
    return (kth);
  }

  int select(T val, int k, int l)
  {
    return (select(val, k + rank(val, l)));
  }


  int quantile(int left, int right, int kth)
  {
    if(right - left <= kth || kth < 0) return (-1);
    T ret = 0;
    for(int depth = 0; depth < MAXLOG; depth++) {
      int l = matrix[depth].rank(1, left);
      int r = matrix[depth].rank(1, right);
      if(r - l > kth) {
        left = l + zs[depth];
        right = r + zs[depth];
        ret |= 1ULL << (MAXLOG - depth - 1);
      } else {
        kth -= r - l;
        left -= l;
        right -= r;
      }
    }
    return (ret);
  }

  vector< T > topk(int l, int r, int k)
  {
    if(r - l < k) k = r - l;
    if(k < 0) return (vector< T >());
    vector< T > ret;
    max_dfs(0, l, r, k, 0, ret);
    return (ret);
  }

  vector< pair< T, int > > freq_list(int l, int r, T a, T b)
  {
    vector< pair< T, int > > ret;
    list_dfs(0, l, r, 0, a, b, ret);
    return (ret);
  }

  vector< pair< int, T > > get_rect(int l, int r, T a, T b)
  {
    vector< pair< T, int > > res = freq_list(l, r, a, b);
    vector< pair< int, T > > ret;
    for(auto &e : res) {
      for(int i = 0; i < e.second; i++) {
        ret.emplace_back(select(e.first, i, l), e.first);
      }
    }
    return (ret);
  }

  int rangefreq(int left, int right, T lower, T upper)
  {
    return (freq_dfs(0, left, right, 0, lower, upper));
  }
};

int main()
{
  char S[100001], T[100001];
  int Q;

  scanf("%s %d", S, &Q);
  SuffixArray sa;
  sa.Build_SA(S);
  vector< int > vs(sa.size());
  for(int i = 0; i < sa.size(); i++) vs[i] = sa[i];
  WaveletMatrix< int, 18 > mat(vs);

  for(int i = 0; i < Q; i++) {
    int l, r;
    scanf("%d %d %s", &l, &r, T);
    string X = T;
    auto p = sa.lower_upper_bound(X);
    printf("%d\n", mat.rangefreq(p.first, p.second, l, r + 1 - (int) X.size() + 1));
  }

}