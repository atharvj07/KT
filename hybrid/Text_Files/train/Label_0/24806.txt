#include "bits/stdc++.h"
#include<unordered_map>
#include<unordered_set>
#pragma warning(disable:4996)
using namespace std;
using ld = long double;

int main() {
	int case_id=0;
	while (true) {
		int W,H,N;cin>>W>>H>>N;
		if(!W)break;
		vector<vector<vector<int>>>walls(H,vector<vector<int>>(W,vector<int>(4)));
		int dx[4] = { -1,0,1,0 };
		int dy[4] = { 0,-1,0,1 };
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if(i==0)walls[i][j][1]=true;
				if(i==H-1)walls[i][j][3]=true;
				if(j==0)walls[i][j][0]=true;
				if(j==W-1)walls[i][j][2]=true;
			}
		}
		for (int i = 0; i < N; ++i) {
			int x1,y1,x2,y2;cin>>x1>>y1>>x2>>y2;
			if (x1 == x2) {
				int u=max(y1,y2);
				int d=min(y1,y2);
				assert(x1>0&&x1<W);
				for (int y = d; y < u; ++y) {
					walls[y][x1-1][2]=true;
					walls[y][x1][0]=true;
				}
			}
			else {
				int l=min(x1,x2);
				int r=max(x1,x2);
				assert(y1>0&&y1<H);
				for (int x = l; x < r; ++x) {
					walls[y1][x][1]=true;
					walls[y1-1][x][3]=true;
				}
			}
		}
		int sx,sy,gx,gy,sway;
		{
			int x1,y1,x2,y2;cin>>x1>>y1>>x2>>y2;
			if (x1 == x2) {
				if (x1 == 0) {
					sway=2;
					sx=0;
					sy=min(y1,y2);
				}
				else {
					sway=0;
					sx=W-1;
					sy=min(y1,y2);
				}
			}
			else {
				if (y1 == 0) {
					sway=3;
					sy=0;
					sx=min(x1,x2);
				}
				else {
					sway=1;
					sy=H-1;
					sx=min(x1,x2);
				}
			}
		}
		cin>>gx>>gy;
		int ans=0;
		{
			int nx=sx;
			int ny=sy;
			int nway=sway;
			while (true) {
				if(nx==gx&&ny==gy)break;
				if (ans > 100000) {
					ans=-1;
					break;
				}
				if (walls[ny][nx][(nway+1)%4]) {
					if (walls[ny][nx][nway]) {
						if (walls[ny][nx][(nway + 3) % 4]) {
							if (walls[ny][nx][(nway + 2) % 4]) {
								ans=-1;
								break;
							}
							else {
								nway=(nway+2)%4;
							}
						}
						else {
							nway=(nway+3)%4;
						}
					}
					else {
						nway=nway;
					}
				}
				else {
					nway=(nway+1)%4;
				}
				nx+=dx[nway];
				ny+=dy[nway];
				ans++;
			}
		}
		if (ans == -1) {
			cout<<"Impossible"<<endl;
		}
		else {
			cout<<ans+1<<endl;
		}
	}
	
	return 0;
}
