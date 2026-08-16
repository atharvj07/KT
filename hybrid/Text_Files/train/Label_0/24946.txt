#include <iostream>
#include <string>
#include <queue>
using namespace std;

struct state{ int lx,ly,rx,ry; };

int dx[] = {0,1,0,-1},dy[] = {1,0,-1,0};

bool dp[50][50][50][50];

int main(){
	int h,w;
	while(cin >> w >> h,h){
		int lx,ly,rx,ry;
		for(int i = 0;i < 50;i++){
			for(int j = 0;j < 50;j++){
				for(int k = 0;k < 50;k++){
					for(int l = 0;l < 50;l++) dp[i][j][k][l] = false;
				}
			}
		}
		bool flag = false;
		string lf[50],rf[50];
		for(int i = 0;i < h;i++){
			cin >> lf[i] >> rf[i];
			for(int j = 0;j < w;j++){
				if(lf[i][j] == 'L'){
					lx = i;
					ly = j;
				}
				if(rf[i][j] == 'R'){
					rx = i;
					ry = j;
				}
			}
		}
		queue<state> que;
		que.push({lx,ly,rx,ry});
		while(!que.empty()){
			state s = que.front();que.pop();
			if(dp[s.lx][s.ly][s.rx][s.ry]) continue;
			//cout << s.lx << " " << s.ly << " " << s.rx << " " << s.ry << endl;
			if(lf[s.lx][s.ly] == '%' && rf[s.rx][s.ry] == '%') flag = true;
			dp[s.lx][s.ly][s.rx][s.ry] = true;
			for(int i = 0;i < 4;i++){
				int nlx = s.lx + dx[i],nly = s.ly + dy[i],nrx = s.rx + dx[i],nry = s.ry + dy[(i + 2) % 4];
				bool move = false;
				if(nlx >= 0 && nlx < h && nly >= 0 && nly < w && lf[nlx][nly] != '#') move = true;
				else{
					nlx = s.lx;
					nly = s.ly;
				}
				if(nrx >= 0 && nrx < h && nry >= 0 && nry < w && rf[nrx][nry] != '#') move = true;
				else{
					nrx = s.rx;
					nry = s.ry;
				}
				if((lf[nlx][nly] == '%') ^ (rf[nrx][nry] == '%')) continue;
				if(move && !dp[nlx][nly][nrx][nry]){
					que.push({nlx,nly,nrx,nry});
				}
			}
		}
		if(flag) cout << "Yes" << endl;
		else cout << "No" << endl;
	}
}