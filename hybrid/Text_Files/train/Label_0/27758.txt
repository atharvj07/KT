#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define d0(x) cout<<(x)<<" "
#define d1(x) cout<<(x)<<endl
#define d2(x,y) cout<<(x)<<" "<<(y)<<endl
#define d3(x,y,z) cout<<(x)<<" "<<(y)<<" "<<(z)<<endl
#define d4(a,b,c,d) cout<<(a)<<" "<<(b)<<" "<<(c)<<" "<<(d)<<endl
#define d5(a,b,c,d,e) cout<<(a)<<" "<<(b)<<" "<<(c)<<" "<<(d)<<" "<<(e)<<endl

template<class T> ostream& operator<<(ostream &os, vector<T> V) {
    os << "[ ";
    for(auto v : V) os << v << ", ";
    return os << "]";
}
template<class T> ostream& operator<<(ostream &os, set<T> S){
    os << "{ ";
    for(auto s:S) os<<s<<", ";
    return os<<"}";
}
template<class L, class R> ostream& operator<<(ostream &os, pair<L,R> P) {
    return os << "(" << P.first << "," << P.second << ")";
}
template<class L, class R> ostream& operator<<(ostream &os, map<L,R> M) {
    os << "{ ";
    for(auto m:M) os<<"("<<m.F<<":"<<m.S<<") ";
    return os<<"}";
}
// returns a to the power b mod p by modular exponentiation
template<class T, class G, class F> ll modexp(T a, G b, F p) {
	ll res = 1, mult = a % p;
    while (b > 0) {
        if (b & 1) {res = (res * mult) % p;}
        b >>= 1;
        mult = (mult * mult) % p;
    }
    return res;
}
int modinv(int a, int n) {return (int) modexp(a, n - 2, n);}

template<class T> ll pow(T a, T b){
    ll res = 1, mult = a;
    while(b>0){
        if(b&1) res = res*mult;
        b>>=1;
        mult *= mult;
    }
    return res;
}

template <class T> T gcd(T a, T b) {
	if (b == 0) {return a;}
	return gcd(b, a % b);
}
// this sieve returns the smallest prime factors of integers upto n
vector<int> sieve(int n){
	vector<int> s(n, 0);
	for(int i=2; i < n+1; i++){
		if(s[i]!=0) continue;
		for(int j=2*i; j< n+1; j+=i)
			s[j] = i;
	}
	return s; 
}

void solve(){
    int n, k;
    cin >> n >> k;

    int h[n];
    
    bool pos = true;
    int ans;
    for(int i=0; i<n; i++) cin >> h[i];
    for(int i=1; i<n;) {
        while(i!=n && h[i]<= h[i-1]) i++;

        if(i == n) {
           continue;
        }
        else{
            if(i>=2 && h[i] > h[i-2]){
                k -= h[i-2]-h[i-1]+1;
                if(k <= 0){
                    pos = true;
                    ans = i;
                    break;
                }
                h[i-1] = h[i-2] + 1;
                i = i-1;
            }
            else{
                k -= h[i] - h[i-1];
                if(k<=0){
                    pos = true;
                    ans = i;
                    break;
                }
                h[i-1] = h[i];
                i++;
                while(i!=n && h[i] <= h[i-1]) i++;
            }
        }
    }
    if(k> 0) pos = false;
    if(!pos) cout << -1;
    else {cout << ans;}
    cout << '\n';
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int t; 
	cin >> t;
	for(int i = 0; i < t; i++){
        //cout << "Case #" << i+1 << ": ";
		solve();
	}
	return 0;
}
