#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
using namespace std;

const int inf = 1e9;

int h,w,n;
string g[10];
char c[10];
bool use[10];
int l[10][10], r[10][10], u[10][10], d[10][10];

inline bool valid(const string &s){
  rep(i,s.size()){
    if(s[i]=='0' && (i==0 || !isdigit(s[i-1])) && (i+1<(int)s.size() && isdigit(s[i+1]))){
      return false;
    }
    if(!isdigit(s[i]) && (i==0 || !isdigit(s[i-1]))){
      return false;
    }
  }
  return isdigit(s.back());
}

int parse(int L, int R, const string &s){
  for(int i=R-1;i>=L;i--){
    if(s[i] == '+' || s[i] == '-'){
      int a = parse(L,i,s), b = parse(i+1,R,s);
      if(a==inf || b==inf)return inf;
      if(s[i] == '+')return a+b;
      if(s[i] == '-')return a-b;
    }
  }

  for(int i=R-1;i>=L;i--){
    if(s[i] == '*' || s[i] == '/'){
      int a = parse(L,i,s), b = parse(i+1,R,s);
      if(a==inf || b==inf)return inf;
      if(s[i] == '*')return a*b;
      if(s[i] == '/'){
	if(b==0 || a%b)return inf;
	return a/b;
      }
    }
  }

  int res = 0;
  for(int i=L;i<R;i++)res = res*10 + (int)(s[i]-'0');
  return res;
}

inline bool check(const string &s){
  if(!valid(s))return false;

  int p = 0;
  while(s[p]!='=')p++;
  assert(p!=(int)s.size());
  int a = parse(0,p,s);
  int b = parse(p+1,s.size(),s);
  if(a==inf || b==inf)return false;
  return a==b;
}

bool solve(int y, int x){
  if(y==h)return true;

  int ny = y, nx = x+1;
  if(nx==w)ny++, nx=0;

  if(g[y][x] != '.')return solve(ny,nx);

  rep(i,n){
    if(!use[i]){
      use[i] = 1;
      g[y][x] = c[i];

      bool f = true;
      if(l[y][x]>=0){
	string s;
	for(int j=l[y][x];j<r[y][x];j++)s += g[y][j];
	if(!check(s))f = false;
      }

      if(f && u[y][x]>=0){
	string s;
	for(int j=u[y][x];j<d[y][x];j++)s += g[j][x];
	if(!check(s))f = false;
      }

      if(f && solve(ny,nx))return true;

      g[y][x] = '.';
      use[i] = 0;
    }
  }
  return false;
}

int main(){
  cin.tie(0); ios::sync_with_stdio(0);
  while(cin >> h >> w, h){
    rep(i,h)cin >> g[i];
    cin >> n;
    rep(i,n)cin >> c[i];

    memset(l,-1,sizeof(l)); memset(r,-1,sizeof(r));
    memset(u,-1,sizeof(u)); memset(d,-1,sizeof(d));
    rep(i,h)rep(j,w){
      if(g[i][j] == '.'){
	int cnt = 0;
	for(int k=j+1;k<w;k++){
	  if(g[i][k] == '.')cnt++;
	  if(g[i][k] == '#')break;
	}
	if(cnt==0){
	  l[i][j] = 0; r[i][j] = w;
	  for(int k=j-1;k>=0;k--){
	    if(g[i][k] == '#'){
	      l[i][j] = k+1;
	      break;
	    }
	  }
	  for(int k=j+1;k<w;k++){
	    if(g[i][k] == '#'){
	      r[i][j] = k;
	      break;
	    }
	  }
	  if(r[i][j]-l[i][j]<3)r[i][j] = l[i][j] = -1;
	}

	cnt = 0;
	for(int k=i+1;k<h;k++){
	  if(g[k][j] == '.')cnt++;
	  if(g[k][j] == '#')break;
	}
	if(cnt==0){
	  u[i][j] = 0; d[i][j] = h;
	  for(int k=i-1;k>=0;k--){
	    if(g[k][j] == '#'){
	      u[i][j] = k+1;
	      break;
	    }
	  }
	  for(int k=i+1;k<h;k++){
	    if(g[k][j] == '#'){
	      d[i][j] = k;
	      break;
	    }
	  }
	  if(d[i][j]-u[i][j]<3)d[i][j] = u[i][j] = -1;
	}
      }
    }
    
    memset(use,0,sizeof(use));
    if(solve(0,0))cout << "Yes" << endl;
    else cout << "No" << endl;
  }
}