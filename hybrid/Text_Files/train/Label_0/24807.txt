#include<cstdio>
#include<algorithm>

#define	rep(i,n)	for(int i=0;i<n;i++)

using namespace std;

const int dx[]={1,0,-1,0},dy[]={0,1,0,-1};

int main(){
	for(int W,H,n;scanf("%d%d%d",&W,&H,&n),W;){
		bool wallH[101][101]={},wallV[101][101]={};
		rep(x,W)	wallH[0][x]=wallH[H][x]=true;
		rep(y,H)	wallV[y][0]=wallV[y][W]=true;
		rep(i,n){
			int xa,ya,xb,yb;	scanf("%d%d%d%d",&xa,&ya,&xb,&yb);
			if(xb<xa)	swap(xa,xb);
			if(yb<ya)	swap(ya,yb);
			if(ya==yb)	for(int x=xa;x<xb;x++)	wallH[ya][x]=true;
			else		for(int y=ya;y<yb;y++)	wallV[y][xa]=true;
		}
		int xs,ys,dir;
		{
			int xa,ya,xb,yb;	scanf("%d%d%d%d",&xa,&ya,&xb,&yb);
			xs=min(xa,xb);
			ys=min(ya,yb);
			if(ya==yb){
				xs=min(xa,xb);
				if(ya==0)	ys=0,dir=1;
				else		ys=H-1,dir=3;
			}
			else{
				ys=min(ya,yb);
				if(xa==0)	xs=0,dir=0;
				else		xs=W-1,dir=2;
			}
		}
		int xg,yg;	scanf("%d%d",&xg,&yg);

		bool ok=false;
		int x=xs,y=ys,cnt=1;
		bool visited[100][100][4]={};
		while(1){
			if(x==xg && y==yg){ ok=true; break; }
			if(visited[y][x][dir])	break;
			visited[y][x][dir]=true;

			dir=(dir+1)%4;
			rep(i,4){
				int xx=x+dx[dir],yy=y+dy[dir];
				if((dir==0 && !wallV[y][xx]) || (dir==1 && !wallH[yy][x])
				|| (dir==2 && !wallV[y][ x]) || (dir==3 && !wallH[ y][x])){
					x=xx,y=yy;
					break;
				}
				dir=(dir+3)%4;
			}
			cnt++;
		}

		if(ok)	printf("%d\n",cnt);
		else	puts("Impossible");
	}

	return 0;
}