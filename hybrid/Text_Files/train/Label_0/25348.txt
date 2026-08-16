#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define HUGE_NUM 99999999999999999
//#define MOD 1000000007
#define EPS 0.000000001
using namespace std;



#define MOD 10007


enum Type{
	N,
	E,
	S,
	W,
	NE,
	SE,
	NW,
	SW,
};

struct Info{

	int x,y;
};


int SIZE,K;
int POW[9],dp[18][33][4];
bool check_X[32],check_Y[32];
vector<int> STATE;
vector<Info> V;
Info info[8];

void mod_add(int &A,int B){

	A += B;
	A %= MOD;
}


int func(){

	for(int i = 0; i <= SIZE/2+1; i++){
		for(int k = 0; k <= SIZE; k++){
			for(int a = 0; a < POW[2]; a++){

				dp[i][k][a] = 0;
			}
		}
	}

	for(int i = 0; i < SIZE; i++){
		check_X[i] = false;
		check_Y[i] = false;
	}

	int first_cross = 0;

	for(int i = 0; i < V.size(); i++){

		if(check_X[V[i].x] || check_Y[V[i].y]){

			return 0;
		}
		check_X[V[i].x] = true;
		check_Y[V[i].y] = true;

		if(V[i].x == V[i].y){ //右上がり

			first_cross |= POW[0];
		}
		if(V[i].x+V[i].y == SIZE-1){ //右下がり

			first_cross |= POW[1];
		}
	}

	int first = 0;
	dp[first][0][first_cross] = 1;
	int last;
	if(SIZE%2 == 0){

		last = SIZE/2-1;
	}else{

		last = SIZE/2;
	}

	int LU = (SIZE-1)/2;
	int RD = SIZE/2;


	int num_X,num_Y;
	int work[8];
	int next_state,mult_X,mult_Y,add,tmp;

	int num_fix = V.size();

	for(int range = first; range <= last; range++){

		num_X = 0;
		num_Y = 0;

		for(int k = LU+1; k <= RD-1; k++){
			if(!check_X[k]){
				num_X++;
			}
			if(!check_Y[k]){

				num_Y++;
			}
		}

		for(int i = 0; i <= SIZE-num_fix; i++){
			for(int state = 0; state < POW[2]; state++){
				if(dp[range][i][state] == 0)continue;

				if(range == first && SIZE%2 == 1){

					mod_add(dp[range+1][i][state],dp[range][i][state]);
					if(!check_X[LU] && !check_Y[LU] && i+1 <= SIZE-num_fix){

						mod_add(dp[range+1][i+1][POW[2]-1],dp[range][i][state]);
					}

				}else{

					for(int k = 0; k < STATE.size(); k++){

						add = 0;

						int ST = STATE[k];
						for(int loop = 0; loop < 8; loop++){
							if(ST & (POW[loop])){

								work[loop] = 1;
								add++;

							}else{

								work[loop] = 0;
							}
						}

						if(i+add > SIZE-num_fix)continue;

						if(range == first && SIZE%2 == 0){
							if(work[N]+work[E]+work[S]+work[W] != 0){

								continue;
							}
						}

						if((check_Y[LU] && (work[SW]+work[S]+work[SE] != 0)) ||
								(check_Y[RD] && (work[NW]+work[N]+work[NE] != 0))){

							continue;
						}
						if((check_X[LU] && (work[NW]+work[W]+work[SW] != 0)) ||
								(check_X[RD] && (work[NE]+work[E]+work[SE] != 0))){

							continue;
						}

						next_state = state;
						if(work[SW] == 1 || work[NE] == 1){

							next_state |= POW[0];
						}
						if(work[NW] == 1 || work[SE] == 1){

							next_state |= POW[1];
						}

						switch(work[N]+work[S]){
						case 2:
							mult_X = (num_X-i)*(num_X-i-1);
							break;
						case 1:
							mult_X = (num_X-i);
							break;
						case 0:
							mult_X = 1;
							break;
						}

						switch(work[E]+work[W]){
						case 2:
							mult_Y = (num_Y-i)*(num_Y-i-1);
							break;
						case 1:
							mult_Y = (num_Y-i);
							break;
						case 0:
							mult_Y = 1;
							break;
						}

						tmp = mult_X*mult_Y;
						tmp *= dp[range][i][state];
						tmp %= MOD;

						mod_add(dp[range+1][i+add][next_state],tmp);
					}
				}
			}
		}

		LU--;
		RD++;
	}

	return dp[last+1][SIZE-num_fix][POW[2]-1];
}

void calc_state(){

	int check[8];

	for(int state = 0; state < POW[8]; state++){
		for(int loop = 0; loop < 8; loop++){
			if(state & (POW[loop])){

				check[loop] = 1;

			}else{

				check[loop] = 0;
			}
		}

		if((check[NW]+check[N]+check[NE] > 1)||(check[NE]+check[E]+check[SE] > 1)||
				(check[SE]+check[S]+check[SW] > 1)||(check[SW]+check[W]+check[NW] > 1)){
			continue;
		}
		STATE.push_back(state);
	}
}


int main(){

	POW[0] = 1;
	for(int i = 1; i <= 8; i++){

		POW[i] = POW[i-1]*2;
	}

	calc_state();

	scanf("%d %d",&SIZE,&K);

	for(int i = 0; i < K; i++){

		scanf("%d %d",&info[i].x,&info[i].y);
	}

	int ans = 0;
	int count,tmp;

	for(int state = 0; state < POW[K]; state++){

		V.clear();
		count = 0;

		for(int loop = 0; loop < K; loop++){
			if(state & POW[loop]){
				V.push_back(info[loop]);
				count++;
			}
		}

		tmp = func();

		if(count%2 == 0){

			ans += tmp;
			ans %= MOD;

		}else{

			ans = (ans-tmp+MOD)%MOD;
		}
	}

	printf("%d\n",ans);

	return 0;
}

