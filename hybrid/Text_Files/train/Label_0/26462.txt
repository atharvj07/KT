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
typedef int SegT;
const int defvalue=0;
class SegTree{
	private:
		vector<SegT>val;
		SegT combine(SegT a,SegT b){return a+b;}
	public:
		int n;
		SegTree(int size){
			n=1;
			while(n<size)n<<=1;
			val=vector<SegT>(2*n,defvalue);
		}
		SegTree(const vector<SegT> &in){
			n=1;
			while(n<in.size())n<<=1;
			val=vector<SegT>(2*n,defvalue);
			for(int i=n-1+in.size()-1;i>=0;i--){
				if(n-1<=i)val[i]=in[i-(n-1)];
				else val[i]=combine(val[i*2+1],val[i*2+2]);
			}
		}
		void update(int i,SegT a){
			i+=n-1;
			val[i]=a;
			while(i>0){
				i=(i-1)/2;
				val[i]=combine(val[i*2+1],val[i*2+2]);
			}
		}
		SegT query(int a,int b,int k=0,int l=0,int r=-1){//[a,b)
			if(r==-1)r=n;
			if(r<=a||b<=l)return defvalue;
			if(a<=l&&r<=b)return val[k];
			else return combine(query(a,b,k*2+1,l,(l+r)/2),query(a,b,k*2+2,(l+r)/2,r));
		}
		void tmp(){
			rep(i,val.size())cout<<" "<<val[i];cout<<endl;
		}
};
int main(){
	int n;
	cin>>n;
	SegTree st(vi(n,1));
	vi in(n);
	ll t;
	cout<<"? 1 "<<n<<endl;
	cin>>t;
	vi cnt(n);
	for(int i=n-1;i>0;i--){
		cout<<"? 1 "<<i<<endl;
		ll s;
		cin>>s;
		int co=t-s+1;
		int l=0,r=n+1;
		while(r-l>1){
			int h=(l+r)/2;
//			cout<<l<<" "<<h<<" "<<r<<" "<<st.query(h,n)<<endl;
			if(st.query(h,n)>=co)l=h;
			else r=h;
		}
		in[i]=l+1;
		cnt[l]=true;
		st.update(l,0);
		t=s;
	}
	rep(i,n)if(!cnt[i])in[0]=i+1;
	cout<<"!";
	rep(i,n)cout<<" "<<in[i];cout<<endl;
}