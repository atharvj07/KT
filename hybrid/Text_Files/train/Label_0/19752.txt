#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)n;i++)
#define all(c) (c).begin(),(c).end()
#define pb push_back
#define dbg(...) do{cerr<<__LINE__<<": ";dbgprint(#__VA_ARGS__, __VA_ARGS__);}while(0);

using namespace std;

namespace std{template<class S,class T>struct hash<pair<S,T>>{size_t operator()(const pair<S,T>&p)const{return ((size_t)1e9+7)*hash<S>()(p.first)+hash<T>()(p.second);}};template<class T>struct hash<vector<T>>{size_t operator()(const vector<T> &v)const{size_t h=0;for(auto i : v)h=h*((size_t)1e9+7)+hash<T>()(i)+1;return h;}};}
template<class T>ostream& operator<<(ostream &os, const vector<T> &v){os<<"[ ";rep(i,v.size())os<<v[i]<<(i==v.size()-1?" ]":", ");return os;}template<class T>ostream& operator<<(ostream &os,const set<T> &v){os<<"{ "; for(const auto &i:v)os<<i<<", ";return os<<"}";}
template<class T,class U>ostream& operator<<(ostream &os,const map<T,U> &v){os<<"{";for(const auto &i:v)os<<" "<<i.first<<": "<<i.second<<",";return os<<"}";}template<class T,class U>ostream& operator<<(ostream &os,const pair<T,U> &p){return os<<"("<<p.first<<", "<<p.second<<")";}
void dbgprint(const string &fmt){cerr<<endl;}template<class H,class... T>void dbgprint(const string &fmt,const H &h,const T&... r){cerr<<fmt.substr(0,fmt.find(","))<<"= "<<h<<" ";dbgprint(fmt.substr(fmt.find(",")+1),r...);}
typedef long long ll;typedef vector<int> vi;typedef pair<int,int> pi;const double EPS = 1e-8, INF = 1e12, PI = acos(-1.0);
typedef complex<double> P;
namespace std{
	bool operator<(const P& a, const P& b){
		return real(a) != real(b) ? real(a) < real(b) : imag(a) < imag(b);
	}
}
inline double cross(const P& a, const P& b){ return imag(conj(a)*b); }
inline double dot(const P& a, const P& b){ return real(conj(a)*b); }
struct C{ P p; double r; };
typedef vector<P> G;
double arg(P p, P q){ return atan2(cross(p,q), dot(p,q)); }
double intersection_area(vector<P> ps, C c) {
  auto tri = [&](P p, P q){
    P d = q - p;
    auto a = dot(d,p)/dot(d,d), b = (dot(p,p)-c.r*c.r)/dot(d,d);
    auto det = a*a - b;
    if (det <= 0) return arg(p,q) * c.r*c.r / 2;
    auto s = max(0.0, -a-sqrt(det)), t = min(1.0, -a+sqrt(det));
    if (t < 0 || 1 <= s) return c.r*c.r*arg(p,q)/2;
    P u = p + s*d, v = p + t*d;
    return arg(p,u)*c.r*c.r/2 + cross(u,v)/2 + arg(v,q)*c.r*c.r/2;
  };
  auto sum = 0.0;
  for (int i = 0; i < ps.size(); ++i)
    sum += tri(ps[i] - c.p, ps[(i+1)%ps.size()] - c.p);
  return sum;
}

int main(){
	cin.tie(0); cin.sync_with_stdio(0);
	
	using Tup = tuple<int,int,int>;
	
	int n, R; cin >> n >> R;
	vector<Tup> in;
	in.emplace_back(-300, 1, 0);
	rep(i, n){
		int x, w, h; cin >> x >> w >> h;
		in.emplace_back(x, w, h);
	}
	in.emplace_back(300, 1, 0);
	
	rep(i, n + 2 - 1){
		int l, w, h; tie(l, w, h) = in[i];
		int next = get<0>(in[i + 1]);
		if(l + w < next) in.emplace_back(l + w, next - l - w, 0);
	}
	n = in.size();
	
	double lo = -200, hi = 200, mid;
	rep(it, 100){
		mid = (lo + hi) / 2;
		double mask = 0;
		rep(i, n){
			int l, r, h; tie(l, r, h) = in[i]; r += l;
			G g = {P(l, -500), P(r, -500), P(r, h), P(l, h)};
			mask += intersection_area(g, {P(0, mid), (double)R});
		}
		if(mask > PI * R * R / 2) lo = mid;
		else hi = mid;
	}
	printf("%.20f\n", hi);
	return 0;
}
