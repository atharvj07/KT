// #pragma GCC target("avx")  // CPU 処理並列化
// #pragma GCC optimize("O3")  // CPU 処理並列化
// #pragma GCC optimize("unroll-loops")  // 条件処理の呼び出しを減らす
// #define BEGIN_STACK_EXTEND(size) void * stack_extend_memory_ = malloc(size);void * stack_extend_origin_memory_;char * stack_extend_dummy_memory_ = (char*)alloca((1+(int)(((long long)stack_extend_memory_)&127))*16);*stack_extend_dummy_memory_ = 0;asm volatile("mov %%rsp, %%rbx\nmov %%rax, %%rsp":"=b"(stack_extend_origin_memory_):"a"((char*)stack_extend_memory_+(size)-1024));
// #define END_STACK_EXTEND asm volatile("mov %%rax, %%rsp"::"a"(stack_extend_origin_memory_));free(stack_extend_memory_);

#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<deque>
#include<stack>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<stdlib.h>
#include<cassert>
#include<time.h>
#include<bitset>
#include<numeric>
#include<unordered_set>
#include<unordered_map>
#include<complex>
using namespace std;
const long long mod=1000000007;
const long long inf=mod*mod;
const long long d2=(mod+1)/2;
const double EPS=1e-11;
const double INF=1e+10;
const double PI=acos(-1.0);
const int C_SIZE = 11100000;
const int UF_SIZE = 3100000;
namespace{
	long long fact[C_SIZE];
	long long finv[C_SIZE];
	long long inv[C_SIZE];
	inline long long Comb(int a,int b){
	 	if(a<b||b<0)return 0;
	 	return fact[a]*finv[b]%mod*finv[a-b]%mod;
	}
	void init_C(int n){
		fact[0]=finv[0]=inv[1]=1;
		for(int i=2;i<n;i++){
			inv[i]=(mod-(mod/i)*inv[mod%i]%mod)%mod;
		}
		for(int i=1;i<n;i++){
			fact[i]=fact[i-1]*i%mod;
			finv[i]=finv[i-1]*inv[i]%mod;
		}
	}
	long long pw(long long a,long long b){
		if(a<0LL)return 0;
		if(b<0LL)return 0;
		long long ret=1;
		while(b){
			if(b%2)ret=ret*a%mod;
			a=a*a%mod;
			b/=2;
		}
		return ret;
	}
	long long pw_mod(long long a,long long b,long long M){
		if(a<0LL)return 0;
		if(b<0LL)return 0;
		long long ret=1;
		while(b){
			if(b%2)ret=ret*a%M;
			a=a*a%M;
			b/=2;
		}
		return ret;
	}
	int pw_mod_int(int a,int b,int M){
		if(a<0)return 0;
		if(b<0)return 0;
		int ret=1;
		while(b){
			if(b%2)ret=(long long)ret*a%M;
			a=(long long)a*a%M;
			b/=2;
		}
		return ret;
	}
	int ABS(int a){return max(a,-a);}
	long long ABS(long long a){return max(a,-a);}
	double ABS(double a){return max(a,-a);}
	int sig(double r) { return (r < -EPS) ? -1 : (r > +EPS) ? +1 : 0; }
	int UF[UF_SIZE];
	void init_UF(int n){
		for(int i=0;i<n;i++)UF[i]=-1;
	}
	int FIND(int a){
		if(UF[a]<0)return a;
		return UF[a]=FIND(UF[a]);
	}
	void UNION(int a,int b){
		a=FIND(a);b=FIND(b);if(a==b)return;
		if(UF[a]>UF[b])swap(a,b);
		UF[a]+=UF[b];UF[b]=a;
	}
}
// ここから編集しろ
int U[310];
int D[310];
int L[310];
int R[310];
int dir[310][310];
int t[310][310];
int rem[310];
pair<int,int>ev[310];
vector<pair<int,int> >ans;
char mag[6]="LRUD";
int dx[4]={0,0,-1,1};
int dy[4]={-1,1,0,0};
int v[310][310];int n;
int s[310][310];
bool dfs(int a,int b){
	if(v[a][b])return false;
	if(s[a][b]){
		s[a][b]=0;
		return true;
	}
	s[a][b]=1;

	int X=a;
	int Y=b;
	int T=dir[a][b];
	X+=dx[T];
	Y+=dy[T];
	while(0<=X&&X<n&&0<=Y&&Y<n){
		bool tmp=dfs(X,Y);
		if(tmp){
			dir[X][Y]=T;
			if(s[a][b]){
				s[a][b]=0;return 1;
			}else{
				return dfs(a,b);
			}
		}
		X+=dx[T];
		Y+=dy[T];
	}
	v[a][b]=1;
	// s[a][b]=0;
	if(T<2)ans.push_back(make_pair(a,T));
	else ans.push_back(make_pair(b,T));
	return 0;
}
int main(){
	int a;scanf("%d",&a);n=a;
	for(int i=0;i<a;i++)scanf("%d",U+i);
	for(int i=0;i<a;i++)scanf("%d",D+i);
	for(int i=0;i<a;i++)scanf("%d",L+i);
	for(int i=0;i<a;i++)scanf("%d",R+i);
	for(int i=0;i<a;i++){
		if(U[i]+D[i]>a||L[i]+R[i]>a){
			printf("NO\n");return 0;
		}
		rem[i]=a-U[i]-D[i];
	}
	for(int i=0;i<a;i++){
		for(int j=0;j<a;j++){
			ev[j]=make_pair(rem[j],j);
		}
		std::sort(ev,ev+a);
		reverse(ev,ev+a);
		for(int j=0;j<L[i]+R[i];j++){
			int at=ev[j].second;
			t[i][at]=1;
			rem[at]--;
		}
	}
	for(int i=0;i<a;i++){
		if(rem[i]){
			printf("NO\n");return 0;
		}
	}
	for(int i=0;i<a;i++)for(int j=0;j<a;j++){
		if(t[i][j]==1){
			if(L[i]){
				L[i]--;
				dir[i][j]=0;
			}else{
				dir[i][j]=1;
			}
		}else{
			if(U[j]){
				U[j]--;
				dir[i][j]=2;
			}else{
				dir[i][j]=3;
			}
		}
	}
	for(int i=0;i<a;i++)for(int j=0;j<a;j++){
		dfs(i,j);
	}
	for(int i=0;i<ans.size();i++){
		// printf("%d %d\n",ans[i].first,ans[i].second);
		printf("%c%d\n",mag[ans[i].second],ans[i].first+1);
	}
}