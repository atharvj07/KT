#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;
double sx[2100];
double sy[2100];
double sz[2100];
double sr[2100];
double tx[21];
double ty[21];
double tz[21];
double tb[21];
double x,y,z;
int dp[2100][20];
inline int chk(int a,int b){
	if(~dp[a][b])return dp[a][b];
	double L=0;
	double R=1;
	bool Q=false;
	double d3=sqrt((sx[a]-tx[b])*(sx[a]-tx[b])+(sy[a]-ty[b])*(sy[a]-ty[b])+(sz[a]-tz[b])*(sz[a]-tz[b]));
	double d4=sqrt((sx[a]-x)*(sx[a]-x)+(sy[a]-y)*(sy[a]-y)+(sz[a]-z)*(sz[a]-z));
	if(d3<sr[a]&&d4<sr[a])return dp[a][b]=0;
	for(int i=0;i<100;i++){
		double m1=(L*2+R)/3;
		double m2=(L+R*2)/3;
		double px=x*m1+tx[b]*(1.0-m1);
		double py=y*m1+ty[b]*(1.0-m1);
		double pz=z*m1+tz[b]*(1.0-m1);
		double qx=x*m2+tx[b]*(1.0-m2);
		double qy=y*m2+ty[b]*(1.0-m2);
		double qz=z*m2+tz[b]*(1.0-m2);
		double d1=sqrt((sx[a]-px)*(sx[a]-px)+(sy[a]-py)*(sy[a]-py)+(sz[a]-pz)*(sz[a]-pz));
		double d2=sqrt((sx[a]-qx)*(sx[a]-qx)+(sy[a]-qy)*(sy[a]-qy)+(sz[a]-qz)*(sz[a]-qz));
		if(d1<sr[a]||d2<sr[a]){return dp[a][b]=1;}
		if(d1<d2)R=m2;
		else L=m1;
	}

	return dp[a][b]=0;
}
int main(){
	int a,b,c;
	while(scanf("%d%d%d",&a,&b,&c),a){
		for(int i=0;i<a;i++)scanf("%lf%lf%lf%lf",sx+i,sy+i,sz+i,sr+i);
		for(int i=0;i<b;i++)scanf("%lf%lf%lf%lf",tx+i,ty+i,tz+i,tb+i);
		scanf("%lf%lf%lf",&x,&y,&z);
		for(int i=0;i<a;i++)for(int j=0;j<b;j++)dp[i][j]=-1;
		double ret=0;
		for(int i=0;i<(1<<b);i++){
			double val=0;
			for(int j=0;j<b;j++)if(i&(1<<j)){
				val+=tb[j]/((tx[j]-x)*(tx[j]-x)+(ty[j]-y)*(ty[j]-y)+(tz[j]-z)*(tz[j]-z));
			}
			int cnt=0;
			for(int j=0;j<a;j++){
				bool ok=true;
				for(int k=0;k<b;k++){
					if(i&(1<<k)){
						if(chk(j,k)){ok=false;break;}
					}
				}
				if(!ok)cnt++;
				if(cnt>c)break;
			}
			if(cnt<=c){
				ret=max(ret,val);
			//	printf("%d\n",i);
			}
		}
		printf("%.12f\n",ret);
	}
}