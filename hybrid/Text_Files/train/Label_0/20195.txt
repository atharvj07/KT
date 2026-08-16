#include <iostream>
#include <string>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>
#include <functional>
#include <bitset>
#include <assert.h>
#include <unordered_map>
#include <fstream>
#include <ctime>
using namespace std;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<char> vc;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef pair<ll,ll> P;
typedef pair<int,int> pii;
typedef vector<P> vpl;
typedef tuple<ll,ll,ll> tapu;
#define rep(i,n) for(int i=0; i<(n); i++)
#define REP(i,a,b) for(int i=(a); i<(b); i++)
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
const int inf = 1<<30;
const ll linf = 1LL<<62;
const int MAX = 510000;
ll dy[8] = {1,-1,0,0,1,-1,1,-1};
ll dx[8] = {0,0,1,-1,1,-1,-1,1};
const double pi = acos(-1);
const double eps = 1e-7;
template<typename T1,typename T2> inline bool chmin(T1 &a,T2 b){
	if(a>b){
		a = b; return true;
	}
	else return false;
}
template<typename T1,typename T2> inline bool chmax(T1 &a,T2 b){
	if(a<b){
		a = b; return true;
	}
	else return false;
}
template<typename T> inline void print(T &a){
    rep(i,a.size()) cout << a[i] << " ";
    cout << "\n";
}
template<typename T1,typename T2> inline void print2(T1 a, T2 b){cout << a << " " << b << "\n";}
template<typename T1,typename T2,typename T3> inline void print3(T1 a, T2 b, T3 c){
	cout << a << " " << b << " " << c << "\n";
}
ll pcount(ll x) {return __builtin_popcountll(x);}
const int mod = 1e9 + 7;
//const int mod = 998244353;

int a[800][800];

int main(){
	while(1){
		ll w,h,t,p; cin >> w >> h >> t >> p;
		if(w+h+t+p == 0) break;
		rep(i,h) rep(j,w) a[i][j] = 1;
		int l = 0, u = 0;
		rep(z,t){
			int d,c; cin >> d >> c;
			if(d == 2){
				for(int i=u; i<u+c; i++){
					REP(j,l,w+l){
						a[2*u+2*c-1-i][j] += a[i][j];
						a[i][j] = 0;
					}
				}
				u += c;
			}else{
				for(int j=l; j<l+c; j++){
					REP(i,u,h+u){
						a[i][2*l+2*c-1-j] += a[i][j];
						a[i][j] = 0;
					}
				}
				l += c;
			}
		}
		rep(i,p){
			int x,y; cin >> x >> y;
			cout << a[y+u][x+l] << "\n";
		}
		REP(i,u,u+h) REP(j,l,l+w) a[i][j] = 0;
	}
}
