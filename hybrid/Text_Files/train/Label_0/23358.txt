#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define REP(i,n) for (int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define ALL(a) (a).begin(),(a).end()
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;
double EPS=1e-10;
int p,q,a,n;
int rec(int x,int y,int cnt,int num){
	if(cnt>n)return 0;
	if(x*p==y*q)return 1;
	if(x*p< y*q)return 0;
	int res=0;
	for(int i=num;i*x<=a;i++){
		res+=rec(x*i,y*i+x,cnt+1,i);
	}
	return res;
}
int main(){
	while(cin>>p>>q>>a>>n&&(p||q||a||n)){
		cout<<rec(1,0,0,1)<<endl;
	}
}