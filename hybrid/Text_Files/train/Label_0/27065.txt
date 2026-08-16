#include<cstdio>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

const int INF=1<<29;
const double EPS=1e-9;

struct Choco{
	int nut;
	double S;
};

int n,m,w,h,thre;
Choco ch[30000];

int solve(){
	int nut=0,ans=INF;
	double S=0;
	for(int i=0,j=0;i<m;i++){
		for(;j<i;j++){
			S+=ch[j].S;
			nut+=ch[j].nut;
		}

		for(;j<m;j++){
			if(w*h-thre+EPS<S) break;
			ans=min(ans,n-nut);
			S+=ch[j].S;
			nut+=ch[j].nut;
		}
		if(w*h-thre+EPS>S) ans=min(ans,n-nut);

		S-=ch[i].S;
		nut-=ch[i].nut;
	}

	return ans;
}

int main(){
	for(;scanf("%d%d%d%d%d",&n,&m,&w,&h,&thre),n;){
		static int l[30001],r[30001];
		l[0]=r[0]=0;
		rep(i,m) scanf("%d%d",l+i+1,r+i+1);

		rep(i,m){
			ch[i].S=((l[i+1]-l[i])+(r[i+1]-r[i]))/2.0*w;
			ch[i].nut=0;
		}
		rep(i,n){
			double cx,cy; scanf("%lf%lf",&cx,&cy);

			int lo=0,hi=m+1;
			while(lo<hi){
				int mi=(lo+hi+1)/2;
				if((w-cx)*l[mi]+cx*r[mi]<w*cy) lo=mi; else hi=mi-1;
			}
			ch[lo].nut++;
		}

		printf("%d\n",solve());
	}

	return 0;
}