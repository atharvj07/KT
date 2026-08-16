#include<bits/stdc++.h>
using namespace std;
#define ll long long
const long long MOD = 1e9 + 7;
const long long INF = 1e9 + 7;
#define pb push_back
#define ff first
#define ss second
#define max_(a,b,c) max1(max1(a,b),c)
#define min_(a,b,c) mn(mn(a,b),c)
long gcd(long a,long b) { return b?gcd(b,a%b):a;}
#define rep(i,a,n) for(int i=a;i<n;i++)
#define per(i,n,a) for(int i=n-1;i>=a;i--)
#define vi vector<int>
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vll vector<long long>
const int mod = 1e9 +7;
const int inf=INT_MAX;
const ll inff=LLONG_MAX;
int mem[5005][5005];
int dp(vector<int> &a, vector<int> &b, int i, int j)
{
    if(mem[i][j]!=-1)
        return mem[i][j];

    if(i>=a.size())
        return 0;

    if(j>=b.size())
        return inf;
    
    int temp=inf;
    int paired=dp(a,b,i+1,j+1);
    int not_paired=dp(a,b,i,j+1);
    if(paired!=inf)
    {
        temp=min(temp,abs(a[i]-b[j])+paired);
    }
    if(not_paired!=inf)
    {
        temp=min(temp,not_paired);
    }
    mem[i][j]=temp;
    return temp;
}
void process()
{
    int n;
    cin>>n;
    vector<int> v;
    vector<int> a1,a0;
    rep(i,0,n)
    {
        int x;
        cin>>x;
        if(x==1)
        {
            a1.push_back(i);
        }
        else if(x==0)
        {
            a0.push_back(i);
        }
        v.push_back(x);
    }
    for(int i=0;i<n+2;++i)
    {
        for(int j=0;j<n+2;++j)
        {
            mem[i][j] = -1;
        }
    }
    cout<<dp(a1,a0,0,0)<<"\n";
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    #ifndef ONLINE_JUDGE
    //cout<<"Hi!";
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //  chrono::time_point<std::chrono::system_clock> start, end;
    //  start = chrono::system_clock::now(); 
    #endif // ONLINE_JUDGE
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t=1;
    //cin>>t;
    while(t--)
        process();
    return 0;
}