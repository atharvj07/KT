#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
#define all(c) (c).begin(), (c).end()
#define loop(i,a,b) for(ll i=a; i<ll(b); i++)
#define rep(i,b) loop(i,0,b)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define lb lower_bound
#define ub upper_bound
#ifdef DEBUG
#define dump(...) (cerr<<#__VA_ARGS__<<" = "<<(DUMP(),__VA_ARGS__).str()<<" ["<<__LINE__<<"]"<<endl)
struct DUMP:ostringstream{template<class T>DUMP &operator,(const T&t){if(this->tellp())*this<<", ";*this<<t;return *this;}};
#else
#define dump(...)
#endif
template<class T> ostream& operator<<(ostream& os, vector<T> const& v){
    rep(i,v.size()) os << v[i] << (i+1==v.size()?"":" ");
    return os;
}

int T, t[40];
int N;
int M[200];
int last, dp[200];

int rec(int x){
    if(x >= last) return 0;
    int & res = dp[x];
    if(res != -1) return res;
    res = 1<<29;
    bool ok = true;
    for(int i=x; i<=last; i++){
        if(M[i] < t[(i-x)%T]) ok = false;
    }
    if(ok) res = 0;
    for(int i=x+1; i<=last; i++){
        res = min(1+rec(i) , res);
        if(M[i] < t[(i-x)%T]) break;
    }
    return res;
}

int main(){
    while(cin>>T && T){
        memset(dp,-1,sizeof(dp));
        rep(i,200) M[i] = 24;
        rep(i,T) cin >> t[i];
        cin >> N;
        rep(i,N){
            int x,y;
            cin >> x >> y;
            M[x] = min(M[x],y);
            last = max(last, x);
        }
        cout << rec(1) << endl;
    }
}