#include<bits/stdc++.h>
using namespace std;
 
#define ff              first
#define ss              second
#define pb              push_back
#define int             long long
#define mp              make_pair
#define pr              pair<long long,long long>
#define vr              vector<long long>
#define MOD          1000000007
#define mod         1000000007
#define mod2            998244353
#define inf             1e18
#define ps(x,y)         fixed<<setprecision(y)<<x
#define mk(arr,n,type)  type *arr=new type[n];
#define ll              long long
#define ld                long double
#define w(x)            int x; cin>>x; while(x--)
#define fill(a,b)       memset(a, b, sizeof(a))
#define ios ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
 int spf[1000002];
 //int dp[1000005];
const int N = 200005;
const int NN=5e6+5;
int ans=1e18;
 void sieve()
 {
     for(int i=0;i<5000002;i++)
      spf[i]=i;
      
    for(int i=2;i<5000002;i=i+2)
     spf[i]=2;
     
    for(int i=3;i*i<5000002;i=i+2)
    {
        if(spf[i]==i)
        {
            spf[i]=i;
            for(int j=i*i;j<5000002;j=j+i)
            {
                if(spf[j]==j)
                {
                    spf[j]=i;
                }
            }
        }
    }
 }
 int power(int x, unsigned int y) 
{ 
    int res = 1;     // Initialize result 
   
    while (y > 0) 
    {
        // If y is odd, multiply x with result 
        if (y & 1) 
            res = res*x%mod; 
   
        // y must be even now 
        y = y>>1; // y = y/2 
        x = x*x % mod;  // Change x to x^2 
    } 
    return res%mod; 
}
int modInv(int a){return power(a,MOD-2);}
int fact[N],inv[N];
void factorial(int n){
    fact[0]=1;
    for(int i=1;i<=n;i++){
        fact[i]=fact[i-1]*i;
        if(fact[i]>=MOD)
            fact[i]%=MOD;
    }
}
void InvFactorial(int n){
    inv[0]=1;
    for(int i=1;i<=n;i++)
        inv[i]=modInv(fact[i]);
}
int ncr(int n,int r){
    if(n<r||n<0||r<0)
        return 0;
    int b=inv[n-r];
    int c=inv[r];
    int a=fact[n]*b;
    if(a>=MOD)
        a%=MOD;
    a*=c;
    if(a>=MOD)
        a%=MOD;
    return a;
}
bool isPrime(int n) 
{ 
    // Corner case 
    if (n <= 1) 
        return false; 
  
    // Check from 2 to n-1 
    for (int i = 2; i*i<= n; i++) 
        if (n % i == 0) 
            return false; 
  
    return true; 
}
bool isPerfectSquare(long double x)
{
    // Find floating point value of
    // square root of x.
    if (x >= 0) {
 
        long long sr = sqrt(x);
         
        // if product of square root
        //is equal, then
        // return T/F
        return (sr * sr == x);
    }
    // else return false if n<0
    return false;
}
bool comparator(string a,string b)
{
    return a<b;
}
int32_t main()
{
    int t;
    cin>>t;
    for(int j=0;j<t;j++)
    {
        int n;
        cin>>n;
        int b[n],a[n];
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
            b[i]=0;
        }
        int sum=0;
        for(int i=n-1;i>=0;i--)
        {
            sum=max(sum,a[i]);
            if(sum>0)
            {
                b[i]=1;
            }
            sum--;
        } 
        for(int i=0;i<n;i++)
        {
            cout<<b[i]<<" ";
        } 
        cout<<endl;
    }    
}