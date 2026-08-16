#include <bits/stdc++.h>

using namespace std;

#define int long long
#define all(v) (v).begin(), (v).end()
#define resz(v, ...) (v).clear(), (v).resize(__VA_ARGS__)
#define reps(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define rep(i, n) reps(i, 0, n)

template<class T1, class T2> void chmin(T1 &a, T2 b){if(a>b)a=b;}
template<class T1, class T2> void chmax(T1 &a, T2 b){if(a<b)a=b;}

typedef pair<int, int> Pi;
typedef tuple<int, int, int> Ti;
typedef vector<int> vint;

const int inf = 1LL << 55;
const int mod = 1e9 + 7;

struct StarrySky {
  vector<int> data, plus;
  int sz;
  StarrySky(int n) {
    sz = 1; while(sz < n) sz <<= 1;
    data.resize(2*sz-1, 0);
    plus.resize(2*sz-1, 0);
  }
  void add(int a, int b, int x, int k, int l, int r) {
    if(r <= a || b <= l) return;
    if(a <= l && r <= b) {
      plus[k] += x;
      return;
    }
    add(a, b, x, 2*k+1, l, (l+r)/2);
    add(a, b, x, 2*k+2, (l+r)/2, r);
    data[k] = min(data[2*k+1]+plus[2*k+1], data[2*k+2]+plus[2*k+2]);
  }
  void add(int a, int b, int x) {
    add(a, b, x, 0, 0, sz);
  }
  int query(int a, int b, int k, int l, int r) {
    if(r <= a || b <= l) return inf;
    if(a <= l && r <= b) return data[k]+plus[k];
    return min(query(a, b, 2*k+1, l, (l+r)/2),
	       query(a, b, 2*k+2, (l+r)/2, r)) + plus[k];
  }
  int query(int a, int b) {
    return query(a, b, 0, 0, sz);
  }
};

signed main()
{
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(12);

  int N, Q;
  string s;
  cin >> N >> Q >> s;
  StarrySky ss(N);
  set<int> st;
  rep(i, N) {
    if(s[i] == '(') {
      ss.add(i, N, 1);
    } else {
      ss.add(i, N, -1);
      st.insert(i);
    }
  }
  while(Q--) {
    int q; cin >> q; q--;
    //cout<<s[q]<<endl;
    if(s[q] == '(') {
      s[q] = ')';
      st.insert(q);
      ss.add(q, N, -2);
      int idx = *st.begin();
      s[idx] = '(';
      st.erase(idx);
      ss.add(idx, N, 2);
      cout << idx+1 << endl;
    } else {
      s[q] = '(';
      st.erase(q);
      ss.add(q, N, 2);
      int lb = 0, ub = q;
      while(lb+1 < ub) {
	int mb = (lb+ub)/2;
	if(ss.query(mb, N) > 1) ub = mb;
	else lb = mb;
      }
      //cout<<ss.query(ub, N)<<endl;
      s[ub] = ')';
      st.insert(ub);
      ss.add(ub, N, -2);
      cout << ub+1 << endl;
    }
  }

  return 0;
}