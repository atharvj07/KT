/**So..a**/
#include<bits/stdc++.h>

// Success after trying 5 hour 11 minute :(


using namespace std;
#define FAST ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

#define PB(x, v) x.push_back(v);
#define M_P(a, b) make_pair(a, b)
#define pll pair<ll, ll>
#define ll long long int
#define mll map<ll, ll>
#define vl vector<ll>
#define fa(x, v) for(auto x: v)
#define fr(i, a, b) for(ll i= a;i <=b; i++)
#define TEST  Int test; cin >> test; while(test--)
#define FTEST Int TesT; cin >> TesT; for(Int test = 1; test<=TesT; test++)

#define B_ begin()
#define E_ end()
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define NL_ "\n"
#define F first
#define S second
#define FF first.first
#define FS first.second
#define SF second.first
#define SS second.second

#define LCM(a, b) (a/__gcd(a, b)*b)
#define PI acos(-1)
#define EXP 10e-6
/*class Prime{
    public:
    Int p[32000];
    void Set(Int n){Int r= n%32;Int e = n/32;Int x = (1<<r);p[e]|=x;}
    Int get(Int n){Int r= n%32;Int e = n/32;Int x = (1<<r);return !(p[e]&x);}
    Prime(){for(auto &x: p) x =0;Set(0), Set(1);for(Int i =  2; i*i<=1000000; i++){if(get(i))for(Int j = i*i; j<=1000000; j+=i)
    Set(j);}}
    Prime(vector<int> &prime){for(auto &x: p) x =0;Set(0), Set(1);for(Int i =  2; i*i<=1000000; i++){if(get(i))for(Int j = i*i; j<=1000000; j+=i)
    Set(j);}for(Int i= 3; i<=1000000; i++) if(get(i)) prime.push_back(i);}
};*/
template<typename item>
item abs(item i)
{
    if(i < 0) i= -i;
    return i;
}
#define MMOODD 1000000007LL
template<class typea,class typeb>
typea POW(typea b, typeb p)
{
    typea res = 1;
    while(p)
    {
        if(p&1) res*=b;
        b*=b;
        b%=MMOODD ;
        res%=MMOODD ;

        p/=2;
    }
    return res;
}
int  tc =0;




#define  ull unsigned long long

#define pii pair<int, int>

#define maxn 100000+10

ll arr[1000000+10];
void solve()
{

    ll n;
    cin >> n;

    for(ll i= 1; i<=2*n; i++) cin >> arr[i];

    n*=2;
//    for(ll i= 1; i<=n; i++)
//    {
//        ll sum =  0;
//        for(ll j= 1; j<=n; j++)
//        {
//            sum+=abs(arr[i] - arr[j]);
//        }
//        cout << sum<<" ";
//    }
    sort(arr+1, arr+1+n);
    reverse(arr+1, arr+1+n);
    ll sum =0;
    set<ll> st;
    for(ll i= 1; i<n; i+=2)
    {
        if(arr[i]!=arr[i+1])
        {
            cout << "NO\n";
            return ;
        }
        ll temp = arr[i] - sum;
//        cout << (arr[i]<sum);
        ll temp2 = n- i+1;
//        cout << temp<<NL_;
        if(0>=temp or temp%temp2)
        {
            cout << "NO\n";
            return ;
        }
        temp /=temp2;

        if(st.count(temp))
        {
            cout <<"NO\n";
            return ;
        }
        st.insert(temp);
        sum+=2*temp;
    }
    cout << "YES\n";
}


int main()
{
    FAST;
    int t;
    cin >> t;
    while(t--)
        solve();
    return 0;
}
