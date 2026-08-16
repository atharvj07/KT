#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
#include<map>
#include<queue>
#include<deque>
#include<iomanip>
#include<tuple>
#include<cassert>
using namespace std;
typedef long long int LL;
typedef pair<int,int> P;
typedef pair<LL,int> LP;
const int INF=1<<30;
const LL MAX=1e9+7;

void array_show(int *array,int array_n,char middle=' '){
	for(int i=0;i<array_n;i++)printf("%d%c",array[i],(i!=array_n-1?middle:'\n'));
}
void array_show(LL *array,int array_n,char middle=' '){
	for(int i=0;i<array_n;i++)printf("%lld%c",array[i],(i!=array_n-1?middle:'\n'));
}
void array_show(vector<int> &vec_s,int vec_n=-1,char middle=' '){
	if(vec_n==-1)vec_n=vec_s.size();
	for(int i=0;i<vec_n;i++)printf("%d%c",vec_s[i],(i!=vec_n-1?middle:'\n'));
}
void array_show(vector<LL> &vec_s,int vec_n=-1,char middle=' '){
	if(vec_n==-1)vec_n=vec_s.size();
	for(int i=0;i<vec_n;i++)printf("%lld%c",vec_s[i],(i!=vec_n-1?middle:'\n'));
}

LL dp[5300][5300];
LL t[5300];
LL t2[5300];

long long int pow_mod(long long int p_a,long long int p_n,long long int p_p=1e9+7){
	//p_a^p_n mod p_p
	long long int p_b=1,p_t=1;
	for(;p_b<=p_n;p_b<<=1);
	for(p_b>>=1;p_b>0;p_b>>=1){
		p_t*=p_t;
		if(p_t>=p_p)p_t%=p_p;
		if(p_n&p_b)p_t*=p_a;
		if(p_t>=p_p)p_t%=p_p;
	}
	return p_t;
}

int main(){
	int n,m;
	int i,j,k;
	LL a,b,c;
	LL x,y;
	LL s[10]={0};
	cin>>n;
	cin>>x>>y;
	if(x<y)swap(x,y);

	memset(dp,0,sizeof(dp));
	dp[0][0]=1;
	for(i=0;i<x;i++){
		dp[i+1][0]=dp[i][0];
		a=0;
		for(j=0;j<x;j++){
			dp[i+1][j+1]=dp[i][j];
			if(j>=y)a+=dp[i][j];
		}
		a%=MAX;
		dp[i+1][0]+=a;
		if(dp[i+1][0]>=MAX)dp[i+1][0]%=MAX;
	}
	for(i=0;i<=x;i++){
		t[i]=dp[i][0];
	}

	memset(dp,0,sizeof(dp));
	dp[0][0]=1;
	for(i=0;i<=n;i++){
		if(i+1<x){
			dp[i+1][0]+=t[i+1];
			dp[i+1][0]%=MAX;
		}
		for(j=0;j<y;j++){
			dp[i+1][j+1]=dp[i][j];
			if(j)t2[i]+=dp[i][j];
		}
		t2[i]%=MAX;
		a=0;
		for(j=0;j<x-1;j++){
			if(i-j<0)break;
			a+=t2[i-j]*t[j];
			if(a>=MAX)a%=MAX;
		}
		dp[i+1][0]+=a;
		dp[i+1][0]%=MAX;
	}
	for(i=1;i<y;i++){
		s[2]+=dp[n][i];
	}
	for(j=1;j<x;j++){
		if(n-j<0)break;
		s[2]+=t2[n-j]*t[j];
		if(s[2]>=MAX)s[2]%=MAX;
	}
	s[2]%=MAX;
	s[0]=pow_mod(2,n)-s[2];
	if(s[0]<0)s[0]+=MAX;
	cout<<s[0]%MAX<<endl;
}