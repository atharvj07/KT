#include <bits/stdc++.h>
using namespace std;
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define _repl(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define _rep(i,n) _repl(i,0,n)
#define rep(...) GET_MACRO(__VA_ARGS__, _repl, _rep)(__VA_ARGS__)
#define mp(a,b) make_pair((a),(b))
#define pb(a) push_back((a))
#define all(x) (x).begin(),(x).end()
#define uniq(x) sort(all(x)),(x).erase(unique(all(x)),end(x))
#define fi first
#define se second
#define dbg(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
void _dbg(string){cout<<endl;}
template<class H,class... T> void _dbg(string s,H h,T... t){int l=s.find(',');cout<<s.substr(0,l)<<" = "<<h<<", ";_dbg(s.substr(l+1),t...);}
template<class T,class U> ostream& operator<<(ostream &o, const pair<T,U> &p){o<<"("<<p.fi<<","<<p.se<<")";return o;}
template<class T> ostream& operator<<(ostream &o, const vector<T> &v){o<<"[";for(T t:v){o<<t<<",";}o<<"]";return o;}

#define INF 1120000000

// Convex Hull Trick for min query
template<typename T, typename U=__int128>
class ConvexHullTrick {
private:
  deque<pair<T,T>> data;
  bool check(pair<T,T> &p){
    int s = data.size();
    return (U)(data[s-1].fi-data[s-2].fi)*(p.se-data[s-1].se) < (U)(data[s-1].se-data[s-2].se)*(p.fi-data[s-1].fi);
  }
public:
  ConvexHullTrick(){ }
  // additions of 'a' shold be NON-INCREASING
  void add(T a, T b){
    auto p = mp(a,b);
    while(data.size()>=2 && !check(p)) data.pop_back();
    data.push_back(p);
  }
  inline T val(int i, T x) {
    return data[i].fi*x + data[i].se;
  }
  // queries shold be NON-DECREASING
  T query(T x){
    while(data.size()>=2 && val(0, x) >= val(1, x)) data.pop_front();
    return val(0, x);
  }
  inline bool empty(){
    return data.empty();
  }
};

int main(){
  int n,T;
  cin>>n>>T;
  vector<pair<int, pair<int,int>>> v(n);
  rep(i,n) cin>>v[i].se.fi>>v[i].se.se>>v[i].fi;
  // <f,<t,p>>
  sort(all(v));

  vector<vector<long>> dp(n, vector<long>(T+1,0));
  vector<ConvexHullTrick<long>> cht(T+1);

  rep(i,n){
    long f = v[i].fi, t = v[i].se.fi, p = v[i].se.se;
    for(int j=T; j>=t; j--){
      if(j == t) dp[i][j] = p;
      else if(cht[j-t].empty()) continue;
      else dp[i][j] = -cht[j-t].query(f) + p - f*f;
      cht[j].add(-2*f, -(dp[i][j] - f*f));
    }
  }

  // rep(i,n){
  //   long f = v[i].fi, t = v[i].se.fi, p = v[i].se.se;
  //   for(int j=T; j>t; j--){
  //     for(int k=0; k<i; k++)
  //       dp[i][j] = max(dp[i][j], dp[k][j-t] + p - (f-v[k].fi)*(f-v[k].fi));
  //   }
  //   dp[i][t] = p;
  // }

  long ans = 0;
  rep(i,n) rep(j,T+1) ans = max(ans, dp[i][j]);

  cout << ans << endl;

  return 0;
}