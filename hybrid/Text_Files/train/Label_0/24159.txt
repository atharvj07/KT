#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define HUGE_NUM 99999999999999999
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;


#define SIZE 35

enum DIR{
	North,
	West,
	East,
	South,
	STOP,
};

struct LOC{
	LOC(){

		row = col = 0;
	}
	LOC(int arg_row,int arg_col){
		row = arg_row;
		col = arg_col;
	}

	int row,col;
};

int H,W;
LOC start,goal;
int diff_row[4] = {-1,0,0,1},diff_col[4] = {0,-1,1,0};
int back_row[4] = {1,0,0,-1},back_col[4] = {0,1,-1,0};
char base_map[SIZE][SIZE];
bool visited[SIZE][SIZE][5];
bool FLG;
DIR dir[5] = {North,West,East,South,STOP};


bool rangeCheck(LOC loc){

	return loc.row >= 0 && loc.row <= H-1 && loc.col >= 0 && loc.col <= W-1;
}

void init(){

	for(int row = 0; row < H; row++){
		for(int col = 0; col < W; col++){
			for(int i = 0; i < 5; i++){
				visited[row][col][i] = false;
			}
		}
	}
}

bool did_visit(LOC loc){

	for(int i = 0; i < 5; i++){

		if(visited[loc.row][loc.col][dir[i]]){
			return true;
		}
	}

	return false;
}


void recursive(LOC loc,DIR current_dir,int used_num,int max_num){

	if(FLG == true || used_num > max_num)return;

	if(current_dir != STOP){

		LOC next;

		next.row = loc.row+diff_row[current_dir];
		next.col = loc.col+diff_col[current_dir];

		if(rangeCheck(next) == false || base_map[next.row][next.col] == '^')return;


		if(base_map[next.row][next.col] == '#'){ //これ以上進めないので止まらざるを得ない

			if(!visited[loc.row][loc.col][STOP]){

				visited[loc.row][loc.col][STOP] = true;
				recursive(loc,STOP,used_num,max_num);
				visited[loc.row][loc.col][STOP] = false;
			}

		}else if(next.row == goal.row && next.col == goal.col){

			FLG = true; //脱出成功
			return;

		}else{ //mase_map[next.row][next.col] == '_'

			//雪だるまを作らない
			if(!visited[next.row][next.col][current_dir]){
				visited[next.row][next.col][current_dir] = true;
				recursive(next,current_dir,used_num,max_num);
				visited[next.row][next.col][current_dir] = false;
			}

			//雪だるまを作って止まる
			if(used_num < max_num && did_visit(next) == false && visited[loc.row][loc.col][STOP] == false){
				base_map[next.row][next.col] = '#';
				visited[loc.row][loc.col][STOP] = true;
				recursive(loc,STOP,used_num+1,max_num);
				base_map[next.row][next.col] = '_';
				visited[loc.row][loc.col][STOP] = false;
			}
		}

	}else{ //curretn_dir == STOP

		for(int i = 0; i < 4; i++){

			LOC back_pos; //背中にあるセル

			back_pos.row = loc.row+back_row[i];
			back_pos.col = loc.col+back_col[i];

			if(rangeCheck(back_pos) == false)continue; //移動したい方向の背中側に壁が必要

			if(base_map[back_pos.row][back_pos.col] != '#'){
				if(base_map[back_pos.row][back_pos.col] == '_' && used_num < max_num && did_visit(back_pos) == false &&
						current_dir == STOP){ //壁を作って再帰

					base_map[back_pos.row][back_pos.col] = '#';
					recursive(loc,STOP,used_num+1,max_num);
					base_map[back_pos.row][back_pos.col] = '_';
					continue;

				}else{

					continue; //壁を作れないのでSKIP
				}
			}

			LOC next;

			next.row = loc.row+diff_row[i];
			next.col = loc.col+diff_col[i];

			if(rangeCheck(next) == false || base_map[next.row][next.col] == '^')continue;

			if(base_map[next.row][next.col] == '#'){ //これ以上進めないので止まらざるを得ない

				if(visited[loc.row][loc.col][STOP] == false){

					visited[loc.row][loc.col][STOP] = true;
					recursive(loc,STOP,used_num,max_num);
					visited[loc.row][loc.col][STOP] = false;
				}
				continue;
			}

			if(next.row == goal.row && next.col == goal.col){

				FLG = true; //脱出成功
				return;

			}else{ //mase_map[next.row][next.col] == '_'

				//雪だるまを作らない
				if(visited[next.row][next.col][dir[i]] == false){
					visited[next.row][next.col][dir[i]] = true;
					recursive(next,dir[i],used_num,max_num);
					visited[next.row][next.col][dir[i]] = false;
				}

				//雪だるまを作って止まる
				if(used_num < max_num && did_visit(next) == false && visited[loc.row][loc.col][STOP] == false){
					base_map[next.row][next.col] = '#';
					visited[loc.row][loc.col][STOP] = true;
					recursive(loc,STOP,used_num+1,max_num);
					base_map[next.row][next.col] = '_';
					visited[loc.row][loc.col][STOP] = false;
				}
			}

		}
	}
}


bool is_OK(int max_num){

	init();

	FLG = false;
	visited[start.row][start.col][STOP] = true; //同じマスを2度以上通過する場合あり:向きも考慮
	recursive(start,STOP,0,max_num);

	return FLG;
}

void func(){

	scanf("%d %d",&H,&W);

	for(int row = 0; row < H; row++){

		scanf("%s",base_map[row]);
		for(int col = 0; col < W; col++){
			if(base_map[row][col] == 'A'){

				start.row = row;
				start.col = col;
				base_map[row][col] = '_';

			}else if(base_map[row][col] == '>'){

				goal.row = row;
				goal.col = col;
			}
		}
	}

	int ans = 10;

	for(int i = 0; i <= 9; i++){
		if(is_OK(i)){
			ans = i;
			break;
		}
	}

	printf("%d\n",ans);
}

int main(){

	int num_case;
	scanf("%d",&num_case);

	for(int loop = 0; loop < num_case; loop++){

		func();
	}

	return 0;
}

