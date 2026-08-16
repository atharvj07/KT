#include<bits/stdc++.h>
using namespace std;
typedef pair< int, int > Pi;

const int INF = 1 << 28;

struct SegmentTree
{
 
  vector< int > small, add;
  int sz;
 
  SegmentTree(int n)
  {
    sz = 1;
    while(sz < n) sz <<= 1;
    small.assign(2 * sz - 1, INF);
    add.assign(2 * sz - 1, 0);
  }
  inline void Merge(int k)
  {
    small[k] = min(small[2 * k + 1] + add[2 * k + 1], small[2 * k + 2] + add[2 * k + 2]);
  }
  inline int RangeMinimumQuery(int a, int b, int k, int l, int r)
  {
    if(a >= r || b <= l) return(INF);
    if(a <= l && r <= b) return(small[k] + add[k]);
    int L = RangeMinimumQuery(a, b, 2 * k + 1, l, (l + r) >> 1);
    int R = RangeMinimumQuery(a, b, 2 * k + 2, (l + r) >> 1, r);
    return(min(L, R) + add[k]);
  }
  int RangeMinimumQuery(int a, int b)
  {
    return(RangeMinimumQuery(a, b, 0, 0, sz));
  }
  inline void RangeAdd(int a, int b, int x, int k, int l, int r)
  {
    if(a >= r || b <= l) return;
    if(a <= l && r <= b) {
      add[k] += x;
      return;
    }
    RangeAdd(a, b, x, 2 * k + 1, l, (l + r) >> 1);
    RangeAdd(a, b, x, 2 * k + 2, (l + r) >> 1, r);
    Merge(k);
  }
  void RangeAdd(int a, int b, int x)
  {
    return(RangeAdd(a, b, x, 0, 0, sz));
  }
  inline int BinarySearch(int k, int l, int r, int upd)
  {
    if(k >= sz - 1) return(r);
    const int right = small[2 * k + 2] + add[2 * k + 2] + add[k] + upd;
    if(right >= 2) return(BinarySearch(2 * k + 1, l, (l + r) >> 1, upd + add[k]));
    return(BinarySearch(2 * k + 2, (l + r) >> 1, r, upd + add[k]));
  }
  int BinarySearch()
  {
    return(BinarySearch(0, 0, sz, 0));
  }
};

int main()
{
  int N, Q;

  scanf("%d %d", &N, &Q);
  char S[300001];
  scanf(" %s", S);
  SegmentTree tree(N);
  set< int > open, close;
  for(int i = 0; i < N; i++) {
    tree.RangeAdd(i, i + 1, -INF);
  }
  for(int i = 0; i < N; i++) {
    tree.RangeAdd(i, N, S[i] == '(' ? +1 : -1);
    if(S[i] == ')') close.insert(i);
    else open.insert(i);
  }
  while(Q--) {
    int q;
    scanf("%d", &q);
    --q;
    tree.RangeAdd(q, N, S[q] == ')' ? +2 : -2);
    if(S[q] == '(') {
      open.erase(q);
      close.insert(q);
      S[q] = ')';
      printf("%d\n", *close.begin() + 1);
      tree.RangeAdd(*close.begin(), N, +2);
      S[*close.begin()] = '(';
      open.insert(*close.begin());
      close.erase(close.begin());
      
    } else {
      close.erase(q);
      open.insert(q);
      S[q] = '(';
      int pos = *open.lower_bound(tree.BinarySearch());
      printf("%d\n", pos + 1);
      tree.RangeAdd(pos, N, -2);
      S[pos] = ')';
      open.erase(pos);
      close.insert(pos);
    }
  }
}