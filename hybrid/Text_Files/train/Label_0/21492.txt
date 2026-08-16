#include <bits/stdc++.h>

using namespace std;

const unsigned mod = 1e9 + 7;
unsigned power[234567], lad[26][234567];

struct SegmentTree
{
  vector< unsigned > hashed;
  vector< int > lazy;
  int sz;

  SegmentTree(int n)
  {
    sz = 1;
    while(sz < n) sz <<= 1;
    hashed.assign(2 * sz - 1, 0);
    lazy.assign(2 * sz - 1, -1);
  }

  void push(int k, int l, int r)
  {
    if(~lazy[k]) {
      hashed[k] = lad[lazy[k]][r - l];
      if(k < sz - 1) {
        lazy[2 * k + 1] = lazy[k];
        lazy[2 * k + 2] = lazy[k];
      }
      lazy[k] = -1;
    }
  }

  void add(int a, int b, int x, int k, int l, int r)
  {
    push(k, l, r);
    if(a >= r || b <= l) return;
    if(a <= l && r <= b) {
      lazy[k] = x;
      push(k, l, r);
    } else {
      add(a, b, x, 2 * k + 1, l, (l + r) >> 1);
      add(a, b, x, 2 * k + 2, (l + r) >> 1, r);
      hashed[k] = hashed[2 * k + 1] * power[(r - l) >> 1] + hashed[2 * k + 2];
    }
  }

  void add(int a, int b, int x)
  {
    add(a, b, x, 0, 0, sz);
  }

  pair< unsigned, int > get(int a, int b, int k, int l, int r)
  {
    push(k, l, r);
    if(a >= r || b <= l) return {0, 0};
    if(a <= l & r <= b) return {hashed[k], r - l};
    auto ll = get(a, b, 2 * k + 1, l, (l + r) >> 1);
    auto rr = get(a, b, 2 * k + 2, (l + r) >> 1, r);
    return {ll.first * power[rr.second] + rr.first, ll.second + rr.second};

  }

  unsigned get(int a, int b)
  {
    return (get(a, b, 0, 0, sz).first);
  };
};

int main()
{
  power[0] = 1;
  for(int i = 0; i < 234566; i++) power[i + 1] = power[i] * mod;
  for(int i = 0; i < 26; i++) {
    const char cc = 'a' + i;
    for(int j = 0; j < 234566; j++) lad[i][j + 1] = lad[i][j] * mod + cc;
  }


  int N, Q;
  string U;

  cin >> N;
  cin >> U;
  SegmentTree tree(N);
  for(int i = 0; i < N; i++) tree.add(i, i + 1, U[i] - 'a');

  cin >> Q;
  while(Q--) {
    string S;
    cin >> S;
    if(S == "set") {
      int x, y;
      char z;
      cin >> x >> y >> z;
      tree.add(--x, y, z - 'a');
    } else {
      int a, b, c, d;
      cin >> a >> b >> c >> d;
      --a, --c;
      int ok = 0, ng = min(d - c, b - a) + 1;
      while(ng - ok > 1) {
        int mid = (ok + ng) >> 1;
        if(tree.get(a, a + mid) == tree.get(c, c + mid)) ok = mid;
        else ng = mid;
      }

      if(ok == d - c && ok == b - a) {
        cout << "e\n";
      } else if(b - a == ok || (d - c != ok && tree.get(a + ok, a + ok + 1) < tree.get(c + ok, c + ok + 1))) {
        cout << "s\n";
      } else {
        cout << "t\n";
      }
    }
  }

}