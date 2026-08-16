#include <iostream>
#include <vector>
#include <cmath>
#define EPS 1.0e-9
#define inf 1000000000

using namespace std;
struct edge{
	int toi, toj;
	double cost;
	edge(int a, int b, double c){
		toi = a, toj = b, cost = c;
	}
};

int n;
double r, th;
int x[25], y[25];
vector<edge> G[25][25];
double dp[10005][25][25];

double dot(double x1, double y1, double x2, double y2)
{
	return x1 * x2 + y1 * y2;
}

double norm(double x, double y)
{
	double d2 = x*x + y*y;
	if(d2 == 0) return 0.0;
	return sqrt(d2);
}

int main(void)
{
	cin >> n >> r >> th;
	for(int i = 0; i < n; i++) cin >> x[i] >> y[i];
	
	double lcos = cos(th * M_PI / 180.0);
	
	double dx1, dx2, dy1, dy2;	
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			if(i == j) continue;
			for(int k = 0; k < n; k++){
				if(j == k) continue;
				
				dx1 = x[j]-x[i], dy1 = y[j]-y[i];
				dx2 = x[k]-x[j], dy2 = y[k]-y[j];
				if( dot(dx1, dy1, dx2, dy2) / norm(dx1, dy1) / norm(dx2, dy2) >= lcos){
					G[i][j].push_back( edge(j, k, norm(dx2, dy2) ) );
				}
			}
		}
	}
	
	
	for(int i = 0; i <= r; i++){
		for(int j = 0; j < n; j++){
			for(int k = 0; k < n; k++){
				dp[i][j][k] = inf;
			}
		}
	}
	for(int i = 1; i < n; i++) dp[1][0][i] = norm(x[i]-x[0], y[i]-y[0]);
	
	
	for(int i = 1; i < r; i++){
		for(int j = 0; j < n; j++){
			for(int k = 0; k < n; k++){
				for(int l = 0; l < G[j][k].size(); l++){
					dp[i+1][G[j][k][l].toi][G[j][k][l].toj] = min(dp[i+1][G[j][k][l].toi][G[j][k][l].toj], dp[i][j][k] + G[j][k][l].cost);
				}
			}
		}
	}
	
	int ans = 0;
	for(int i = r; i >= 0; i--){
		for(int j = 0; j < n; j++){
			for(int k = 0; k < n; k++){
				if(dp[i][j][k] <= r){
					ans = i;
					goto end;
				}
			}
		}
	}
	end:;
	cout << ans << endl;
	return 0;
}