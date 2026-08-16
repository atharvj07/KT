#include <iostream>
#include <cstdio>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <complex>
#include <map>
#include <climits>
#include <sstream>
using namespace std;

#define reep(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n) reep((i),0,(n))
#define ALL(v) (v).begin(),(v).end()
#define PB push_back
#define EPS 1e-8
#define F first
#define S second
#define mkp make_pair

static const double PI=6*asin(0.5);
typedef long long ll;
typedef complex<double> CP;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vint;
static const int INF=1<<24;

template <class T>
void initvv(vector<vector<T> > &v,int a,int b, const T  &t = T()){
	v.assign(a,vector<T>(b,t));
}

//v.erase(unique(v.begin(),v.end()),v.end());


int main(){
	int n;
	// map<char,ll> ma;
	int dx[]={0,0,1,-1};
	int dy[]={1,-1,0,0};
	int aa[][4]={
		{0,0,1,3},
		{0,1,2,4},
		{1,2,2,5},
		{0,3,4,6},
		{1,3,5,7},
		{2,4,5,8},
		{3,6,6,7},
		{4,6,7,8},
		{5,7,8,8}
	};
	while(cin>>n,n){
		vector<ll> aaa(9,0);
		char x,y,z;
		cin>>x>>y>>z;
		int d,e,f;
		d=x-'A';
		e=y-'A';
		f=z-'A';
		aaa[d]++;
		
		rep(i,n){
			vector<ll> tmp(9,0);
			rep(k,9){
				rep(j,4){
					if(aa[k][j]==f){
						tmp[k]+=aaa[k];
					}
					else{
						tmp[aa[k][j]]+=aaa[k];
					}
				}
			}
			aaa=tmp;

		}
		
		long double ans=4.0;
		ans=pow(ans,n);
		ans=aaa[e]/ans;
		// cout<<ans<<endl;
		printf("%.8Lf\n",ans);
	}
	
}