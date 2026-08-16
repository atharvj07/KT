#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <complex>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <functional>
#include <iterator>

using namespace std;

#define dump(n) cout<<"# "<<#n<<'='<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define peri(i,a,b) for(int i=int(b);i-->int(a);)
#define rep(i,n) repi(i,0,n)
#define per(i,n) peri(i,0,n)
#define iter(c) __typeof__((c).begin())
#define foreach(i,c) for(iter(c) i=(c).begin();i!=(c).end();++i)
#define all(c) (c).begin(),(c).end()
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef pair<int,int> pii;

const ll INFTY=1ll<<61; // 2.3*10^18
const double EPS=1e-9;

template<typename T1,typename T2>
ostream& operator<<(ostream& os,const pair<T1,T2>& p){
	return os<<'('<<p.first<<','<<p.second<<')';
}
template<typename T>
ostream& operator<<(ostream& os,const vector<T>& a){
	os<<'[';
	rep(i,a.size()) os<<(i?" ":"")<<a[i];
	return os<<']';
}

ll combi(int n,int r)
{
	static ll memo[100030][30];
	r=min(r,n-r);
	if(!memo[n][r])
		memo[n][r]=r==0?1:min(INFTY,combi(n-1,r-1)+combi(n-1,r));
	return memo[n][r];
}

ll mul(ll x,ll y)
{
	return 1.*x*y>INFTY?INFTY:x*y;
}

int main()
{
	int n,asize; ll kth;
	scanf("%d%d%lld",&n,&asize,&kth);
	
	vi sa(n);
	rep(i,n){
		scanf("%d",&sa[i]);
		sa[i]--;
	}
	
	// 元の文字列にはどの文字より小さい終端文字'$'が含まれるとする．
	// つまりsa[n..]="$"が辞書順最小の接尾辞．
	sa.insert(sa.begin(),n);
	n++;
	
	vi rank(n);
	rep(i,n) rank[sa[i]]=i;
	
	vi inc(n); // inc[i]==true: s[sa[i-1]]<s[sa[i]]でなければならない
	repi(i,2,n)
		if(rank[sa[i-1]+1]>rank[sa[i]+1])
			inc[i]=true;
	
	vi isum(n);
	repi(i,1,n) isum[i]=isum[i-1]+inc[i];
	
	if(asize<isum[n-1]+1 || combi(n-1+asize-isum[n-1]-1,asize-isum[n-1]-1)<kth){
		puts("Impossible");
		return 0;
	}
	
	vector<pair<pii,ll> > ranges(1,mp(mp(0,n),-1)); // ((left,right),pattern)
	
	vi accum(n+1,-1);
	accum[0]=0;
	accum[n]=asize-isum[n-1]-1;
	
	rep(i,n-1) if(accum[rank[i]]==-1){
		int left=-1,right=-1;
		rep(j,ranges.size()){
			int le=ranges[j].first.first,ri=ranges[j].first.second;
			if(le<=rank[i] && rank[i]<ri){
				left=le,right=ri;
				ranges.erase(ranges.begin()+j);
				break;
			}
		}
		ll pat=1;
		rep(j,ranges.size())
			pat=mul(pat,ranges[j].second);
		
		repi(j,accum[left],accum[right]+1){
			ll lpat=combi(rank[i]-left+j-accum[left]-1,j-accum[left]);
			ll rpat=combi(right-rank[i]+accum[right]-j-1,accum[right]-j);
			ll lrpat=mul(lpat,rpat);
			if(mul(pat,lrpat)>=kth){
				if(lpat==1)
					repi(k,left+1,rank[i])
						accum[k]=accum[left];
				else
					ranges.push_back(mp(mp(left,rank[i]),lpat));
				if(rpat==1)
					repi(k,rank[i]+1,right)
						accum[k]=accum[right];
				else
					ranges.push_back(mp(mp(rank[i],right),rpat));
				accum[rank[i]]=j;
				break;
			}
			else
				kth-=mul(pat,lrpat);
		}
	}
	
	rep(i,n) accum[i]+=isum[i];
	
	string res(n-1,'a');
	repi(i,1,n) res[sa[i]]+=accum[i];
	
	puts(res.c_str());
	
	return 0;
}