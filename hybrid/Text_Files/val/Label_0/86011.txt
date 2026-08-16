#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
typedef long long int ll;

using namespace std;

int label_num = 0,N;

enum DIST{
	now_U_next_right,
	now_U_next_hidarishita,
	now_L_next_down,
	now_L_next_migiue,
	now_R_next_down,
	now_R_next_hidarishita,
	now_D_next_right,
	now_D_next_migiue,
	hidarishita_moving,
	migiue_moving,
};

bool rangeCheck(int row,int col){
	if(row >= 0 && row <= N-1 && col >= 0 && col <= N-1)return true;
	else{
		return false;
	}
}

void func(){

	if(N <= 2){
		printf("Case %d:\n",label_num);
		if(N == 0){
			printf("  0\n");
		}else if(N == 1){
			printf("  1\n");
		}else if(N == 2){
			printf("  1  2\n  3  4\n");
		}
		return;
	}

	int table[N][N],number = 1,limit,row = 0,col = 0;
	limit = N*N;

	DIST current = now_U_next_right;
	table[0][0] = number;

	number++;

	while(number <= limit){
		switch(current){
		case now_U_next_right:
			if(rangeCheck(row,col+1) == true){
				table[row][col+1] = number;
				col++;
				current = now_U_next_hidarishita;
			}else{
				table[row+1][col] = number;
				row++;
				current = now_R_next_hidarishita;
			}
			break;
		case now_U_next_hidarishita:
			table[row+1][col-1] = number;
			row++;
			col--;
			current = hidarishita_moving;
			break;
		case now_L_next_down:
			if(rangeCheck(row+1,col) == true){
				table[row+1][col] = number;
				row++;
				current = now_L_next_migiue;
			}else{
				table[row][col+1] = number;
				col++;
				current = now_D_next_migiue;
			}
			break;
		case now_L_next_migiue:
			table[row-1][col+1] = number;
			row--;
			col++;
			current = migiue_moving;
			break;
		case now_R_next_down:
			if(rangeCheck(row+1,col)){
				table[row+1][col] = number;
				row++;
				current = now_R_next_hidarishita;
			}else{
				//Do nothing
			}
			break;
		case now_R_next_hidarishita:
			if(rangeCheck(row+1,col-1)){
				table[row+1][col-1] = number;
				row++;
				col--;
				current = hidarishita_moving;
			}else{
				//Do nothing
			}
			break;
		case now_D_next_right:
			if(rangeCheck(row,col+1)){
				table[row][col+1] = number;
				col++;
				current = now_D_next_migiue;
			}else{
				//Do nothing
			}
			break;
		case now_D_next_migiue:
			if(rangeCheck(row-1,col+1)){
				table[row-1][col+1] = number;
				row--;
				col++;
				current = migiue_moving;
			}else{
				//Do nothing;
			}
			break;
		case hidarishita_moving:
			if(rangeCheck(row+1,col-1)){
				table[row+1][col-1] = number;
				row++;
				col--;
			}else{
				number--;
				if(row == N-1){
					current = now_D_next_right;
				}else{
					current = now_L_next_down;
				}
			}
			break;
		case migiue_moving:

			if(rangeCheck(row-1,col+1)){
				table[row-1][col+1] = number;
				row--;
				col++;
			}else{
				number--;
				if(col == N-1){
					current = now_R_next_down;
				}else{
					current = now_U_next_right;
				}
			}
			break;
		}
		number++;
	}

	printf("Case %d:\n",label_num);

	for(int i = 0; i < N; i++){
		for(int k = 0; k < N; k++){
			printf("%3d",table[i][k]);
		}
		printf("\n");
	}

}

int main(){

	while(true){
		scanf("%d",&N);
		if(N == 0)break;

		label_num++;

		func();

	}

    return 0;
}