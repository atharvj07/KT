#include<queue>
#include<cstdio>
#include<cstring>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

const int INF=1<<29;
const int dx[]={1,0,-1,0},dy[]={0,-1,0,1};

struct Stat{
	int x,y,d; // d : Ì½ßÔ
	bool operator<(const Stat &S)const{ return d>S.d; }
};

int main(){
	for(int h,w,n;scanf("%d%d%d",&h,&w,&n),h;){
		char cmd[1000001]; scanf("%s",cmd);
		int sx,sy,gx,gy;
		static char B[1000][1001];
		rep(i,h){
			scanf("%s",B[i]);
			rep(j,w){
				if(B[i][j]=='S') sx=j, sy=i;
				if(B[i][j]=='G') gx=j, gy=i;
			}
		}

		// precalc
		int len=strlen(cmd);
		// dir[i] := ÉÀs·é½ßª i Å éÆ«Éü¢Ä¢éûü
		static int dir[1000001];
		dir[0]=1;
		rep(i,len) dir[i+1]=(dir[i]+(cmd[i]=='L'?1:3))%4;

		// next[i][k] := ÉÀs·é½ßª i Å éÆ«AÉßÄûü k ðü­æ¤È½ßÔ(+1)
		static int next[1000001][4];
		rep(k,4) next[len][k]=(k==dir[len]?len:INF);
		for(int i=len;i>0;i--) rep(k,4) {
			if(k==dir[i-1]) next[i-1][k]=i-1;
			else            next[i-1][k]=next[i][k];
		}

		// Dijkstra
		static int d[1000][1000][4];
		rep(i,h) rep(j,w) rep(k,4) d[i][j][k]=INF;
		d[sy][sx][1]=0;

		bool ok=false;
		priority_queue<Stat> pq; pq.push((Stat){sx,sy,0});
		while(!pq.empty()){
			Stat S=pq.top(); pq.pop();

			if(d[S.y][S.x][dir[S.d]]<S.d) continue;
			if(S.x==gx && S.y==gy){ ok=true; break; }

			rep(k,4){
				int xx=S.x+dx[k],yy=S.y+dy[k];
				if(0<=yy && yy<h && 0<=xx && xx<w && B[yy][xx]!='#'){
					if(next[S.d][k]<d[yy][xx][k]){
						d[yy][xx][k]=next[S.d][k];
						pq.push((Stat){xx,yy,next[S.d][k]});
					}
				}
			}
		}

		puts(ok?"Yes":"No");
	}

	return 0;
}