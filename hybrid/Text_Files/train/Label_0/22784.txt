    #include<bits/stdc++.h>
    using namespace std;
    typedef long long ll;

    #define  prec(n)        fixed<<setprecision(n)
    #define  optimize       ios::sync_with_stdio(0); cin.tie(0);
    #define  PI             acos(-1.0)
    #define  RESET(a, b)    memset(a, b, sizeof(a))
    #define  pb             push_back
    #define  sz(v)          v.size()
    #define  pii            pair<int,int>
    #define  pll            pair<ll,ll>
    #define  ff             first
    #define  ss             second
    #define  vv             vector<int>
    #define  all(v)         v.begin(),v.end()

    const ll MOD= 1e9+7;
    inline void normal(ll &a) { a %= MOD; (a < 0) && (a += MOD); }
    inline ll modMul(ll a, ll b) { a %= MOD, b %= MOD; normal(a), normal(b); return (a*b)%MOD; }
    inline ll modAdd(ll a, ll b) { a %= MOD, b %= MOD; normal(a), normal(b); return (a+b)%MOD; }
    inline ll modSub(ll a, ll b) { a %= MOD, b %= MOD; normal(a), normal(b); a -= b; normal(a); return a; }
    inline ll modPow(ll b, ll p) { ll r = 1; while(p) { if(p&1) r = modMul(r, b); b = modMul(b, b); p >>= 1; } return r; }
    inline ll modInverse(ll a) { return modPow(a, MOD-2); }inline ll modDiv(ll a, ll b) { return modMul(a, modInverse(b)); }
    inline ll mod(ll a, ll m){ if(a<0) return m-(abs(a)%m); else if(a<m) return a; else return (a%m); }

    const int MAX = 504;
    const int N = 2e5+7;
    const int INF = 1e9;
    const int LN =  100;

    int dp[2507][5007];

int main()
{
    optimize
    int t=1; //cin>>t;
    while(t--){
         int n;
         cin>>n;
         int a[n+2];
         vector<int>person,chair;
         for(int i=0;i<n;i++){
             cin>>a[i];
             if(a[i]) person.pb(i);
             else chair.pb(i);
         }
         if(sz(person)==0){
            cout<<"0\n";
            continue;
         }
         for(int i=0;i<2507;i++) for(int j=0;j<5007;j++) dp[i][j]=INF;
         for(int i=0;i<sz(person);i++){
            for(int j=i;j<sz(chair);j++){
                if(i==0){
                    if(j==0) dp[i][j]=abs(person[i]-chair[j]);
                    else dp[i][j]=min(dp[i][j-1],abs(person[i]-chair[j]));
                }
                else
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j-1]+abs(person[i]-chair[j]));
            }
         }
         cout<<dp[sz(person)-1][sz(chair)-1]<<"\n";
    }
}
