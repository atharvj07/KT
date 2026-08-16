#include <bits/stdc++.h>
using namespace std;
#define all(c) (c).begin(),(c).end()
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define REP(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) REP(i,0,n)
#define iter(c) __typeof((c).begin())
#define tr(it,c) for(iter(c) it=(c).begin();it!=(c).end();it++)
#define mem(a) memset(a,0,sizeof(a))
#define pd(a) printf("%.10f\n",a)
#define pb(a) push_back(a)
#define in(a) insert(a)
#define pi M_PI
#define R cin>>
#define F first
#define S second
#define C class
#define ll long long
#define ln cout<<'\n'
#define _(_1,_2,_3,N,...)N
#define pr(...) _(__VA_ARGS__,pr3,pr2,pr1)(__VA_ARGS__)
template<C T>void pr1(T a){cout<<a;ln;}
template<C T,C T2>void pr2(T a,T2 b){cout<<a<<' '<<b;ln;}
template<C T,C T2,C T3>void pr3(T a,T2 b,T3 c){cout<<a<<' '<<b<<' '<<c;ln;}
template<C T>void PR(T a,int n){rep(i,n){if(i)cout<<' ';cout<<a[i];}ln;}
bool check(int n,int m,int x,int y){return x>=0&&x<n&&y>=0&&y<m;}
const ll MAX=1000000007,MAXL=1LL<<60,dx[4]={-1,0,1,0},dy[4]={0,1,0,-1};
typedef pair<int,int> P;
typedef pair<int,P> PP;

int p[10001],r[10001];
void init(){rep(i,10001)p[i]=i,r[i]=0;}
int find(int x){return (p[x]==x)?x:(p[x]=find(p[x]));}
void unite(int x,int y) {
  x=find(x),y=find(y);
  if(x==y)return;
  if(r[x]<r[y])p[x]=y;
  else{p[y]=x;if(r[x]==r[y])r[x]++;}
}
bool same(int x,int y){return find(x)==find(y);}

void Main() {
  int n,m;
  while(cin >> n >> m && n) {
    init();
    PP a[m];
    rep(i,m) cin >> a[i].S.F >> a[i].S.S >> a[i].F;
    sort(a,a+m);
    int c=n/2;
    rep(i,m) {
      if(same(a[i].S.F,a[i].S.S)) continue;
      unite(a[i].S.F,a[i].S.S);
      c--;
      if(!c) {
        pr(a[i].F);
        break;
      }
    }
  }
}

int main() {
  ios::sync_with_stdio(0);cin.tie(0);
  Main();return 0;
}
