#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cassert>
using namespace std;

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define fr(i,c) for(__typeof(c.begin()) i=c.begin();i!=c.end();i++)
#define pb push_back
#define mp make_pair
#define all(c) c.begin(),c.end()
#define dbg(x) cerr<<#x<<" = "<<(x)<<endl

typedef vector<int> vi;
typedef pair<int,int> pi;
typedef long long ll;
const int inf=(int)1e9;
const double EPS=1e-9, INF=1e12;

// Larsson-Sadakane's Suffix array Construction: O(n (log n)^2)
struct SAComp {
  const int h, *g;
  SAComp(int h, int* g) : h(h), g(g) {}
  bool operator() (int a, int b) {
    return a == b ? false : g[a] != g[b] ? g[a] < g[b] : g[a+h] < g[b+h];
  }
};
int *buildSA(char* t, int n) {
  int g[n+1], b[n+1], *v = new int[n+1];
  rep(i,n+1) v[i] = i, g[i] = t[i];
  b[0] = 0; b[n] = 0;

  sort(v, v+n+1, SAComp(0, g));
  for(int h = 1; b[n] != n ; h *= 2) {
    SAComp comp(h, g);
    sort(v, v+n+1, comp);
    rep(i, n) b[i+1] = b[i] + comp(v[i], v[i+1]);
    rep(i, n+1) g[v[i]] = b[i];
  }
  return v;
}
// Naive matching O(m log n)
int find(char *t, int n, char *p, int m, int *sa) {
  int a = 0, b = n;
  while (a < b) {
    int c = (a + b) / 2;
    if (strncmp(t+sa[c], p, m) < 0) a = c+1; else b = c;
  }
  return strncmp(t+sa[a], p, m) == 0 ? sa[a] : -1;
}
int n,m,k;
string s;
char *sc,t[500];
int *sa,len;

ll ck(){
	ll res=0;
	for(int l=0,r=0;l<m;l++){
		while(r<l)r++;
		while(r<m){
			char tmp=t[r+1];
			t[r+1]=0;
			bool res=find(sc,len,t+l,r-l+1,sa)>=0;
			t[r+1]=tmp;
			if(!res)break;
			r++;
		}
		res+=r-l;
	}
	return res;
}

const string rec(int l,int r){
	if(l>=r)return "";
	
	if(isdigit(s[l])){
		int i,x=0,d=0;
		for(;l<r&&isdigit(s[l]);l++){
			x*=10; x+=s[l]-'0';
			x=min(x,400);
		}
		for(i=l;i<r;i++){
			if(s[i]=='(')d++;
			if(s[i]==')')d--;
			if(d==0)break;
		}
		string res="", tmp=rec(l+1,i);
		if(x==1)return tmp;
		
		rep(i,x-1){
			res+=tmp;
			if(res.size()>400)break;
		}
		const string str=res+tmp;
		if(str.size()<=800)return str+rec(i+1,r);
		const string head400=str.substr(0,min((int)str.size(),400));
		const string tail400=str.substr(max(0,(int)str.size()-400));
		
		const string tail=tmp.substr(max(0,(int)tmp.size()-400));
		const string head=tmp.substr(0,min(400,(int)tmp.size()));
		
		return head400+"@"+tail+res+head+"@"+tail400+rec(i+1,r);
	}
	return s[l]+rec(l+1,r);
}
int main(){
	cin>>n>>m>>k;
	cin>>s;
	s=rec(0,n);
	len=s.size();
	sc=(char*)malloc(len+1);
	sprintf(sc,"%s",s.c_str()); s.clear();
	sa=buildSA(sc,len);
	
	int ansi=0; ll ans=0;
	rep(i,k){
		cin>>t;
		ll tmp=ck();
		if(tmp>ans)ans=tmp, ansi=i;
	}
	cout<<ansi+1<<" "<<ans<<endl;
	
	return 0;
	
}