#include <bits/stdc++.h>
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FORR(i,a,b) for (int i=(a);i>=(b);i--)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define pcnt __builtin_popcount
#define tzcnt __builtin_ctzl
#define sz(x) (int)(x).size()
#define maxs(x,y) x=max(x,y)
#define mins(x,y) x=min(x,y)
#define show(x) cout<<#x<<" = "<<x<<endl;
#define all(a) (a.begin()),(a.end())
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define perm(c) sort(all(c));for(bool c##p=1;c##p;c##p=next_permutation(all(c)))
#define bit(n) (1LL<<(n))

using namespace std;
typedef long long ll;
typedef __int128_t lll;
template <class T> using V = vector<T>;
template <class T> using VV = V<V<T>>;
template<typename T>string join(V<T>&v){stringstream s;FOR(i,0,sz(v))s<<' '<<v[i];return s.str().substr(1);}
template<typename A,size_t N,typename T>void Fill(A (&array)[N],const T&v){fill((T*)array,(T*)(array+N),v);}
lll gcd(lll a,lll b,lll &x,lll &y){if(!b){x=1;y=0;return a;}lll d=gcd(b,a%b,y,x);y-=a/b*x;return d;}
ll gcd(ll a,ll b){lll x=0,y=0;return gcd(a,b,x,y);}
ll modPow(lll a,lll n,ll m){if(!a)return a;lll p=1;for(;n>0;n>>=1,a=a*a%m)if(n&1)p=p*a%m;return(ll)p;}
bool isPrime(ll n){if(n<2||n%2==0)return n==2;lll t=n-1,d=t/(t&-t);for(lll a:{2,325,9375,28178,450775,9780504,1795265022})if(a%n){for(t=d,a=modPow(a,t,n);t!=n-1&&a!=1&&a!=n-1;a=a*a%n,t=t*2%n);if(a!=n-1&&t%2==0)return 0;}return 1;}
void dout(double d){printf("%.12f\n",d);}
void YN(bool z){cout<<(z?"YES\n":"NO\n");}
void Yn(bool z){cout<<(z?"Yes\n":"No\n");}
void yn(bool z){cout<<(z?"yes\n":"no\n");}
mt19937 rnd; void set_rnd(){random_device r;rnd=mt19937(r());}
V<ll> fact, rfact; void set_fact(int n, ll m){fact.pb(1);rfact.pb(1);FOR(i,1,n+1)fact.pb(fact[i-1]*i%m),rfact.pb(modPow(fact[i],m,m-2));}
const int iinf = 1e9+6;
const ll linf = 1e18;
const int mod = 1e9+7;
const double pi = acos(-1);
const double eps = 1e-10;
const int N = 1e5;
struct FFT{
  const double pi = acos(-1);
  vector<complex<double> > x;
  int n;
  void init(int _n){
    n = _n;
    x.resize(0);
    complex<double> t(1.0, 0.0), w(cos(pi/n), -sin(pi/n));
    for(int i=0; i<n; i++) x.push_back(t), t *= w;
  }
  void dft(vector<complex<double> >& a, bool inv) {
    int j = 0;
    for (int i = 1; i < n; ++i) {
      int k = n >> 1;
      while (j >= k) j -= k, k >>= 1;
      j += k;
      if (i < j) swap(a[i], a[j]);
    }
    complex<double> t;
    for (int k = 1; k < n; k <<= 1) {
      for (int i0 = 0; i0 < n; i0 += k << 1) {
        for (int i = i0; i < i0 + k; ++i) {
          j = i + k;
          a[j] *= inv ? conj(x[n / k * (i - i0)]) : x[n / k * (i - i0)];
          t = a[i] - a[j];
          a[i] = a[i] + a[j];
          a[j] = t;
        }
      }
    }
    if(inv) for(int i=0; i<n; i++) a[i] /= n;
  }
} fft;
string s;
vector<complex<double> > a[2];
int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  bool z = false;
  FOR(j, 0, 2){
    cin >> s;
    int i = 0;
    if(s[0] == '0'){
      cout << 0 << endl;
      return 0;
    }
    if(s[0] == '-') i++, z ^= true;
    for(; i<sz(s); i++) a[j].pb(complex<double>(double(s[i]-'0'), 0.0));
    reverse(all(a[j]));
  }
  int n = bit(32-__builtin_clz(sz(a[0])+sz(a[1])));
  FOR(i, 0, 2) a[i].resize(n);
  fft.init(n);
  fft.dft(a[0], false);
  fft.dft(a[1], false);
  FOR(i, 0, n) a[0][i] *= a[1][i];
  fft.dft(a[0], true);
  int d = 0;
  vector<int> v(n);
  FOR(i, 0, n) v[i] = (int)round(a[0][i].real());
  FOR(i, 0, n-1){
    v[i+1] += v[i]/10;
    v[i] %= 10;
  }
  if(z) printf("-");
  z = false;
  FORR(i, n-1, 0){
    if(v[i] || z)printf("%d", v[i]);
    z |= !!v[i];
  }
  printf("\n");
  return 0;
}
