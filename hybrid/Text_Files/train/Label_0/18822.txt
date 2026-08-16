#include <cmath>
#include <cstdio>
#include <algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

const double PI=acos(-1);

// whether (hx, hy) is covered by the sector (tx,ty,w,a)
bool check(int hx,int hy,int tx,int ty,double d,double w,int a){
	int x=hx-tx,y=hy-ty;
	if(sqrt(x*x+y*y)>a) return false;

	double phi=atan2(y,x);
	if(w>PI) w-=2*PI; // -PI < w <= PI
	return min(min(abs(phi-w),abs(phi-w+2*PI)),abs(phi-w-2*PI))<d/2;
}

int main(){
	for(int h,r;scanf("%d%d",&h,&r),h;){
		int hx[100],hy[100];
		rep(i,h) scanf("%d%d",hx+i,hy+i);

		int nu,nm,ns;
		double du,dm,ds;
		scanf("%d%d%d",&nu,&nm,&ns);
		scanf("%lf%lf%lf",&du,&dm,&ds);
		du*=PI/180;
		dm*=PI/180;
		ds*=PI/180;

		int ux[10],uy[10],mx[10],my[10],sx[10],sy[10];
		rep(i,nu) scanf("%d%d",ux+i,uy+i);
		rep(i,nm) scanf("%d%d",mx+i,my+i);
		rep(i,ns) scanf("%d%d",sx+i,sy+i);

		double w[100];
		int a[100];
		rep(i,r){
			scanf("%lf%d",w+i,a+i);
			w[i]*=PI/180;
		}

		int cnt[100]={};
		rep(i,h) rep(j,r) {
			bool ok=check(hx[i],hy[i],0,0,du,w[j],a[j]);
			rep(k,nu) if(check(hx[i],hy[i],ux[k],uy[k],du,w[j],a[j])) ok=false;
			rep(k,nm) if(check(hx[i],hy[i],mx[k],my[k],dm,w[j],a[j])) ok=false;
			rep(k,ns) if(check(hx[i],hy[i],sx[k],sy[k],ds,w[j],a[j])) ok=false;
			if(ok) cnt[i]++;
		}

		int maxi=*max_element(cnt,cnt+h);
		if(maxi==0){ puts("NA"); continue; }

		int num=0;
		rep(i,h) if(cnt[i]==maxi) {
			printf("%s%d",num>0?" ":"",i+1);
			num++;
		}
		puts("");
	}

	return 0;
}