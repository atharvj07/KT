#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<numeric>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<cassert>

#define rep(i,n) for(int i=0;i<n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define rp(i,c) rep(i,(c).size())
#define fr(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
const int inf=1<<28;
const double INF=1e12,EPS=1e-9;

int n,X[100],Y[100],sz,m,ys[100];
double mx[10000],my[10000];
double d(int a,int b){
	return sqrt((mx[a]-mx[b])*(mx[a]-mx[b])+(my[a]-my[b])*(my[a]-my[b]));
}
int main()
{
	while(scanf("%d",&n),n){
		rep(i,n)scanf("%d%d",X+i,Y+i),ys[i]=Y[i];
		sort(ys,ys+n);
		sz=unique(ys,ys+n)-ys; m=0;
		rep(i,n){
			mx[m]=X[i]; my[m]=Y[i]; m++;
			if(i<n-1)for(int j=Y[i]<Y[i+1]?0:sz-1;Y[i]<Y[i+1]?j<sz:j>=0;Y[i]<Y[i+1]?j++:j--)
				if(min(Y[i+1],Y[i])<ys[j]&&ys[j]<max(Y[i],Y[i+1])){
					double dy=Y[i+1]-Y[i],dx=(X[i+1]-X[i])/dy*(ys[j]-Y[i]);
					mx[m]=X[i]+dx; my[m]=ys[j]; m++;
			}
		}
		//rep(i,m)cerr<<mx[i]<<" "<<my[i]<<endl;
		
		priority_queue<pair<double,pi> >q;
		set<pi> v;
		q.push(mp(0,mp(0,m-1)));
		while(!q.empty()){
			int l=q.top().second.first, r=q.top().second.second;
			double c=q.top().first; q.pop();
			if(v.count(mp(l,r)))continue;
			v.insert(mp(l,r));
			if(l==r){
				printf("%.9f\n",-c); break;
			}
			for(int i=-1;i<2;i++)for(int j=-1;j<2;j++)
			if(0<=l+i&&l+i<m&&0<=r+j&&r+j<m&&abs(my[l+i]-my[r+j])<1e-9){
				q.push(mp(c-d(l,l+i)-d(r,r+j),mp(l+i,r+j)));
			}
		}
	}
	return 0;
}