#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cctype>
#include <queue>
#include <algorithm>
#define rep(i,n) for (int i = 0; i < n; ++i)
#define pb push_back
#define rng(x) x.begin(),x.end()
#define fi first
#define se second
#define sz(x) int(x.size())
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<P> vp;

const int INF = 1001001001;

struct Mincost {
  struct Edge{
    int to, co, lim, nxt;
    Edge(){}
    Edge(int to, int co, int lim, int nxt):to(to),co(co),lim(lim),nxt(nxt){}
  };
  int n;
  vi head, dist, pre;
  vector<Edge> e;
  Mincost(int n):n(n),head(n,-1),dist(n),pre(n){}
  void add(int f, int t, int c=0, int l=1) {
    e.pb(Edge(t,c,l,head[f])); head[f] = sz(e)-1;
    e.pb(Edge(f,-c,0,head[t])); head[t] = sz(e)-1;
  }
  void dijk(int sv) {
    fill(rng(dist),INF);
    fill(rng(pre),-1);
    priority_queue<P,vp,greater<P>> q;
    int v, d;
    q.push(P(0,sv));
    dist[sv] = 0;
    while (sz(q)) {
      d = q.top().fi; v = q.top().se; q.pop();
      if (dist[v] != d) continue;
      for (int i = head[v]; i != -1; i = e[i].nxt) {
        int u = e[i].to;
        if (e[i].lim && d+e[i].co < dist[u]) {
          dist[u] = d+e[i].co;
          pre[u] = i^1;
          q.push(P(dist[u],u));
        }
      }
    }
  }
  int solve(int sv, int tv, int flow) {
    int res = 0, f;
    while (flow>0) {
      dijk(sv);
      if (dist[tv] == INF) return -1;
      rep(i,n) for (int j = head[i]; j != -1; j = e[j].nxt) {
        e[j].co += dist[i] - dist[e[j].to];
      }
      f = flow;
      for (int i = tv; i != sv; i = e[pre[i]].to) f = min(f,e[pre[i]^1].lim);
      for (int i = tv; i != sv; i = e[pre[i]].to) {
        e[pre[i]^1].lim -= f, e[pre[i]].lim += f;
      }
      res += dist[tv]*flow;
      flow -= f;
    }
    return res;
  }
};

vvi a;

int main() {
  int n, m, k;
  scanf("%d",&n);
  scanf("%d%d",&m,&k);
  a = vvi(n,vi(m));
  string s;
  rep(i,n) {
    cin >> s;
    rep(j,m) {
      a[i][j] += s[j]-'0';
    }
  }
  rep(i,m) {
    cin >> s;
    rep(j,n) {
      a[j][i] += s[j]-'0';
    }
  }
  Mincost mc(n+m+2);
  int sv = n+m, tv = sv+1;
  rep(i,n) mc.add(sv,i);
  rep(i,m) mc.add(n+i,tv);
  rep(i,n)rep(j,m) mc.add(i,n+j,a[i][j]);
  int l = 0, r = min(n,m)+1, c;
  // rep(i,n)rep(j,m) cout<<i<<" "<<j<<" "<<a[i][j]<<endl;
  // cout<<mc.solve(sv,tv,5)<<endl;
  while (l+1<r) {
    c = (l+r)>>1;
    auto nc = mc;
    int x = nc.solve(sv,tv,c);
    if (x == -1 || x > k) r = c; else l = c;
  }
  cout<<l<<endl;
  return 0;
}