#include<iostream>
#include<vector>
#include<string>
#include<algorithm>	
#include<map>
#include<set>
#include<utility>
#include<cmath>
#include<cstring>
#include<queue>
#include<cstdio>
#include<sstream>
#include<iomanip>
#define loop(i,a,b) for(int i=a;i<b;i++) 
#define rep(i,a) loop(i,0,a)
#define pb push_back
#define mp make_pair
#define all(in) in.begin(),in.end()
#define shosu(x) fixed<<setprecision(x)
using namespace std;
//kaewasuretyuui
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vp;
typedef vector<vp> vvp;
typedef pair<int,pii> pip;
typedef vector<pip>vip;
const double PI=acos(-1);
const double EPS=1e-8;
const int inf=1e8;
int main(){
	int n;
	int co=0;
	while(cin>>n,n){
		co++;
		vector<double>x,y,x1,x2,y1,y2;
		vvi in(210,vi(210));
		rep(i,n){
			double a,b,c;
			cin>>a>>b>>c;
			x.pb(a-c);x.pb(a+c);
			y.pb(b-c);y.pb(b+c);
			x1.pb(a-c);x2.pb(a+c);
			y1.pb(b-c);y2.pb(b+c);
		}
		sort(all(x));
		sort(all(y));
		x.erase(unique(all(x)),x.end());
		y.erase(unique(all(y)),y.end());
		rep(i,n){
			int a=find(all(x),x1[i])-x.begin();
			int b=find(all(x),x2[i])-x.begin();
			int c=find(all(y),y1[i])-y.begin();
			int d=find(all(y),y2[i])-y.begin();
			loop(j,a,b)loop(k,c,d)
				in[j][k]=true;
		}
		double sum=0;
		rep(i,210)rep(j,210)if(in[i][j])
			sum+=(x[i+1]-x[i])*(y[j+1]-y[j]);
		cout<<co<<" "<<shosu(2)<<sum<<endl;
	}
}