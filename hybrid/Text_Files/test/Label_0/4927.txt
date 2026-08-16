#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <numeric>
#include <cctype>
#include <bitset>
#include <cassert>
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < (n); ++i)
#define rrep(i,n) for(int i = 1; i <= (n); ++i)
#define drep(i,n) for(int i = (n)-1; i >= 0; --i)
#define gep(i,g,j) for(int i = g.head[j]; i != -1; i = g.e[i].next)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
#define pcnt __builtin_popcount
#define uni(x) x.erase(unique(rng(x)),x.end())
#define snuke srand((unsigned)clock()+(unsigned)time(NULL));
#define df(x) int x = in()
#define dame { puts("0"); return 0;}
#define show(x) cout<<#x<<" = "<<x<<endl;
#define PQ(T) priority_queue<T,vector<T>,greater<T> >
using namespace std;
typedef long long int ll;
typedef pair<int,int> P;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<P> vp;
inline int in() { int x; scanf("%d",&x); return x;}
inline void priv(vi a) { rep(i,sz(a)) printf("%d%c",a[i],i==sz(a)-1?'\n':' ');}
template<typename T>istream& operator>>(istream&i,vector<T>&v)
{rep(j,sz(v))i>>v[j];return i;}
template<typename T>string join(vector<T>&v)
{stringstream s;rep(i,sz(v))s<<' '<<v[i];return s.str().substr(1);}
template<typename T>ostream& operator<<(ostream&o,vector<T>&v)
{if(sz(v))o<<join(v);return o;}
template<typename T1,typename T2>istream& operator>>(istream&i,pair<T1,T2>&v)
{return i>>v.fi>>v.se;}
template<typename T1,typename T2>ostream& operator<<(ostream&o,pair<T1,T2>&v)
{return o<<v.fi<<" "<<v.se;}
const int MX = 100005, INF = 1001001001;
const ll LINF = 1e18;
const double eps = 1e-10;

struct Parse {
  int n;
  string s;
  int i;
  P parse() {
    for (n = 1; n <= sz(s); ++n) {
      i = 0;
      P p = expr();
      // cout<<n<<" "<<p<<endl;
      if (p.fi == p.se) return P(p.fi,n);
    }
    return P(-1,-1);
  }
  P expr() {
    if (i >= n) return P(0,99);
    if (isdigit(s[i])) return num();
    if (s[i] == '_') {
      ++i; if (i >= n) return P(0,99);
      ++i;
      P x = expr();
      if (i >= n) return P(0,x.se);
      ++i;
      P y = expr();
      ++i;
      return P(min(x.fi,y.fi), min(x.se,y.se));
    } else {
      ++i; if (i >= n) return P(0,99);
      ++i;
      P x = expr();
      if (i >= n) return P(x.fi,99);
      ++i;
      P y = expr();
      ++i;
      return P(max(x.fi,y.fi), max(x.se,y.se));
    }
  }
  P num() {
    if (i >= n) return P(0,99);
    if (s[i] == '0') {
      ++i;
      return P(0,0);
    } else {
      int x = s[i]-'0';
      ++i;
      if (i >= n) return P(x,x*10+9);
      if (isdigit(s[i])) {
        x = x*10+s[i]-'0';
        ++i;
      }
      return P(x,x);
    }
  }
};

int main() {
  int ts;
  cin >> ts;
  rep(ti,ts) {
    Parse p;
    cin >> p.s;
    P ans = p.parse();
    cout<<ans<<endl;
  }
  return 0;
}





