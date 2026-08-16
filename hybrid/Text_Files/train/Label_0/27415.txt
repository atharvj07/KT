#include <bits/stdc++.h>
#define GET_MACRO(_1,_2,_3,_4,_5,_6,_7,_8,NAME,...) NAME
#define pr(...) cerr<< GET_MACRO(__VA_ARGS__,pr8,pr7,pr6,pr5,pr4,pr3,pr2,pr1)(__VA_ARGS__) <<endl
#define pr1(a) (#a)<<"="<<(a)<<" "
#define pr2(a,b) pr1(a)<<pr1(b)
#define pr3(a,b,c) pr1(a)<<pr2(b,c)
#define pr4(a,b,c,d) pr1(a)<<pr3(b,c,d)
#define pr5(a,b,c,d,e) pr1(a)<<pr4(b,c,d,e)
#define pr6(a,b,c,d,e,f) pr1(a)<<pr5(b,c,d,e,f)
#define pr7(a,b,c,d,e,f,g) pr1(a)<<pr6(b,c,d,e,f,g)
#define pr8(a,b,c,d,e,f,g,h) pr1(a)<<pr7(b,c,d,e,f,g,h)
#define prArr(a) {cerr<<(#a)<<"={";int i=0;for(auto t:(a))cerr<<(i++?", ":"")<<t;cerr<<"}"<<endl;}
using namespace std;
using Int = long long;
using _int = int;
using ll = long long;
using Double = long double;
const Int INF = (1LL<<60)+1e9; // ~ 1.15 * 1e18
const Int mod = (1e9)+7;
const Double EPS = 1e-8;
const Double PI = 6.0 * asin((Double)0.5);
using P = pair<Int,Int>;
template<class T> T Max(T &a,T b){return a=max(a,b);}
template<class T> T Min(T &a,T b){return a=min(a,b);}
template<class T1, class T2> ostream& operator<<(ostream& o,pair<T1,T2> p){return o<<"("<<p.first<<","<<p.second<<")";}
template<class T1, class T2, class T3> ostream& operator<<(ostream& o,tuple<T1,T2,T3> t){
  return o<<"("<<get<0>(t)<<","<<get<1>(t)<<","<<get<2>(t)<<")";}
template<class T1, class T2> istream& operator>>(istream& i,pair<T1,T2> &p){return i>>p.first>>p.second;}
template<class T> ostream& operator<<(ostream& o,vector<T> a){Int i=0;for(T t:a)o<<(i++?" ":"")<<t;return o;}
template<class T> istream& operator>>(istream& i,vector<T> &a){for(T &t:a)i>>t;return i;}

Int count(Int n){
  if(n == 1) return 0;
  Int a = (9 * 8 / 2) * ((1LL<<n) - 2);
  Int b = 9 * ((1LL<<(n-1)) - 1);
  Int res = a + b;
  return res;
}

Int count2(Int n){
  Int a = 8 * ((1LL<<n) - 1);
  Int b = (1LL<<n) - 1;
  Int res = a + b;
  return res;
}

Int count3(Int n){
  return (1LL<<n) - 1;
}


Int used[11][1000], mem[11][1000];
Int dfs(Int first, Int second,Int len){
  if(len == 0) return second != 10;
  if(used[second][len]++) return mem[second][len];
  
  Int res = 0;
  for(Int i=0;i<10;i++){
    if(second == 10 && i == first) res += dfs(first, second, len - 1);
    else if(second == 10 && i != first) res += dfs(first, i, len - 1);
    else if(i == first || i == second) res += dfs(first, second, len - 1);
    Min(res, INF);
  }
  return mem[second][len] = res;
}

string dfs2(Int first, Int second, Int len, Int K){
  if(len == 0) return "";
  string res;
  for(Int i=0;i<10;i++){
    Int num = -1;
    Int nsecond = second;
    if(second == 10 && i == first) num = dfs(first, second, len - 1);
    else if(second == 10 && i != first) num = dfs(first, i, len - 1), nsecond = i;
    else if(i == first || i == second) num = dfs(first, second, len - 1);
    if(num == -1) continue;
    if(K - num <= 0) return res + to_string(i) + dfs2(first, nsecond, len - 1, K);
    K -= num;
  }
  return res;
}

string solve(Int n){
  Int len = 2;
  while(n - count(len) > 0) n -= count(len), len++;
  Int a = 1;
  while(n - count2(len-1) > 0) n -= count2(len-1), a++;
  return to_string(a) + dfs2(a, 10, len-1, n);
}


Int isTanka(Int n){
  string s = to_string(n);
  sort(s.begin(), s.end());
  s.erase(unique(s.begin(), s.end()),s.end());
  return s.size() == 2;
}

signed main(){
  srand((unsigned)time(NULL));
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(12);

  /*  Int cnt = 0;
  for(Int i=0;i<=25252;i++)
    if(to_string(i).size() == 5 && to_string(i)[0] == '2' && isTanka(i)) cnt++;
  pr(cnt);
  */
  
  while(1){
    Int n;
    cin>>n;
    if(n == 0) break;
    string ans = solve(n);
    cout<<ans<<endl;
    
  }
  
  
  return 0;
}

