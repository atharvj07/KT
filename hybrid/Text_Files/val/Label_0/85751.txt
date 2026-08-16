#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <cfloat>
#include <stack>
#include <queue>
#include <vector>
typedef long long int ll;
#define BIG_NUM 2000000000
#define MOD 1000000007
#define EPS 0.000001
using namespace std;

int T,minimum,sleep[30],N,last_day,last_time,dp[101][30],pre_day,sche[101];

int main(){

	int tmp_day,tmp_time;

	while(true){
		scanf("%d",&T);
		if(T == 0)break;

		for(int i = 0; i < T; i++)scanf("%d",&sleep[i]);

		scanf("%d",&N);

		for(int i = 0; i <= 100; i++)sche[i] = 0;

		for(int i = 1; i <= N; i++){
			scanf("%d %d",&tmp_day,&tmp_time);
			if(sche[tmp_day] != 0){
				sche[tmp_day] = min(sche[tmp_day],tmp_time);
			}else{
				sche[tmp_day] = tmp_time;
			}
		}

		for(int i = 0; i <= 100; i++){
			for(int k = 0; k < T; k++)dp[i][k] = BIG_NUM;
		}

		dp[1][0] = 0;

		for(int day = 2; day <= 100; day++){
			for(int cicle = 0; cicle < T; cicle++){
				if(dp[day-1][cicle] == BIG_NUM)continue;

				if(sche[day] >= sleep[(cicle+1)%T] || sche[day] == 0){
					dp[day][(cicle+1)%T] = min(dp[day][(cicle+1)%T],dp[day-1][cicle]);
					dp[day][0] = min(dp[day][0],dp[day-1][cicle]+1);
				}else{
					dp[day][0] = min(dp[day][0],dp[day-1][cicle]+1);
				}
			}
		}

		minimum = 200;
		for(int i = 0; i < T; i++){
			minimum = min(minimum,dp[100][i]);
		}

		printf("%d\n",minimum);
	}

	return 0;
}