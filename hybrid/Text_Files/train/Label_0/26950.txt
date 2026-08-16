#include <bits/stdc++.h>
using namespace std;

#define dump(...) cout<<"# "<<#__VA_ARGS__<<'='<<(__VA_ARGS__)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define peri(i,a,b) for(int i=int(b);i-->int(a);)
#define rep(i,n) repi(i,0,n)
#define per(i,n) peri(i,0,n)
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;

template<typename T1,typename T2>
ostream& operator<<(ostream& os,const pair<T1,T2>& p){
	return os<<'('<<p.first<<','<<p.second<<')';
}

template<typename Tuple>
void print_tuple(ostream&,const Tuple&){}
template<typename Car,typename... Cdr,typename Tuple>
void print_tuple(ostream& os,const Tuple& t){
	print_tuple<Cdr...>(os,t);
	os<<(sizeof...(Cdr)?",":"")<<get<sizeof...(Cdr)>(t);
}
template<typename... Args>
ostream& operator<<(ostream& os,const tuple<Args...>& t){
	print_tuple<Args...>(os<<'(',t);
	return os<<')';
}

template<typename Ch,typename Tr,typename C>
basic_ostream<Ch,Tr>& operator<<(basic_ostream<Ch,Tr>& os,const C& c){
	os<<'[';
	for(auto i=begin(c);i!=end(c);++i)
		os<<(i==begin(c)?"":" ")<<*i;
	return os<<']';
}

constexpr int INF=1e9;
constexpr int MOD=1e9+7;
constexpr double EPS=1e-9;

inline pii number(const string& s,int i)
{
	int x=0;
	if(i>=s.size() || !isdigit(s[i])) return mp(INF,-1);
	for(int len=0;i<s.size() && isdigit(s[i]);i++,len++){
		if(len==1 && x==0) return mp(INF,-1);
		x=x*10+s[i]-'0';
	}
	return mp(x,i);
}
inline pii term(const string& s,int i)
{
	int x; tie(x,i)=number(s,i);
	if(i==-1) return mp(INF,-1);
	while(i<s.size() && (s[i]=='*' || s[i]=='/')){
		char op=s[i];
		int y; tie(y,i)=number(s,i+1);
		if(i==-1) return mp(INF,-1);
		if(op=='*') x*=y;
		if(op=='/'){
			if(y==0 || x%y>0) return mp(INF,-1);
			x/=y;
		}
	}
	return mp(x,i);
}
inline pii expr(const string& s,int i)
{
	int x; tie(x,i)=term(s,i);
	if(i==-1) return mp(INF,-1);
	while(i<s.size()){
		char op=s[i];
		if(op!='+' && op!='-') return mp(INF,-1);
		int y; tie(y,i)=term(s,i+1);
		if(i==-1) return mp(INF,-1);
		if(op=='+') x+=y;
		if(op=='-') x-=y;
	}
	return mp(x,i);
}
int expr(const string& s)
{
	return expr(s,0).first;
}

bool check(const vs& grid,const vector<pii>& f)
{
	string s;
	for(auto p:f) s+=grid[p.first][p.second];
	if(count(all(s),'=')!=1) return false;
	int eq=s.find('=');
	if(eq==0 || eq==s.size()-1) return false;
	string a=s.substr(0,eq),b=s.substr(eq+1);
	
	int x=expr(a),y=expr(b);
	//dump(mt(s,x,y));
	if(x==INF || y==INF || x!=y)
		return false;
	return true;
}

bool solve(int i,vs& grid,string& cs,vector<pii>& ps,vector<vector<pii>>& fs,vvi& ds)
{
	int n=ps.size();
	if(i==n) return true;
	
	for(char& c:cs) if(c!='X'){
		grid[ps[i].first][ps[i].second]=c; c='X';
		if(all_of(all(ds[i]),[&](int j){return check(grid,fs[j]);}))
			if(solve(i+1,grid,cs,ps,fs,ds))
				return true;
		c=grid[ps[i].first][ps[i].second];
	}
	return false;
}

int main()
{
	for(int h,w;cin>>h>>w && h|w;){
		vs grid(h);
		rep(i,h) cin>>grid[i];
		int n; cin>>n;
		string cs(n,'~');
		rep(i,n) cin>>cs[i];
		
		vector<pii> ps;
		vector<vector<pii>> fs;
		rep(i,h) rep(j,w){
			if(grid[i][j]=='.') ps.emplace_back(i,j);
			if(grid[i][j]!='#'){
				if((i==0 || grid[i-1][j]=='#') && i<h-1 && grid[i+1][j]!='#'){
					vector<pii> f;
					for(int k=i;k<h && grid[k][j]!='#';k++)
						f.emplace_back(k,j);
					fs.emplace_back(f);
				}
				if((j==0 || grid[i][j-1]=='#') && j<w-1 && grid[i][j+1]!='#'){
					vector<pii> f;
					for(int k=j;k<w && grid[i][k]!='#';k++)
						f.emplace_back(i,k);
					fs.emplace_back(f);
				}
			}
		}
		
		vvi ds(n+1);
		{
			vi vis(fs.size());
			rep(i,n+1){
				rep(j,fs.size()) if(!vis[j]){
					string s;
					for(auto p:fs[j]) s+=grid[p.first][p.second];
					if(count(all(s),'.')==0){
						ds[i].push_back(j);
						vis[j]=1;
					}
				}
				if(i<n) grid[ps[i].first][ps[i].second]='?';
			}
			rep(i,n)
				grid[ps[i].first][ps[i].second]='.';
			rotate(begin(ds),1+all(ds));
		}
		
		if(!all_of(all(ds[n]),[&](int j){return check(grid,fs[j]);})){
			cout<<"No"<<endl;
			continue;
		}
		cout<<(solve(0,grid,cs,ps,fs,ds)?"Yes":"No")<<endl;
	}
}