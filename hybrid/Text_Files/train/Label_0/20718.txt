#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <cfloat>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <map>
#include <time.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;


#define NULL_VAL -1
#define UNKNOWN 2000000000
#define Error 999999999
#define NoReturn 888888888


enum Type{
	None,
	Malloc,
	Free,
	Clone,
};

struct Info{
	int size;
	bool deleted;
};

int value_table[26],heap_room,info_index,max_room;
Info info[10000];
char buf[301];

int parse(int left,int right){

	int index = left;
	int depth,close_pos,tmp;

	Type pre = None;

	while(index <= right){

		switch(buf[index]){
		case '(':

			depth = 0;
			for(int i = index; i <= right; i++){
				if(buf[i] == '('){
					depth++;
				}else if(buf[i] == ')'){
					depth--;
					if(depth == 0){
						close_pos = i;
						break;
					}
				}
			}
			tmp = parse(index+1,close_pos-1);

			if(tmp == Error){
				return Error;
			}

			switch(pre){
			case Malloc:
				if(tmp <= heap_room){

					info[info_index].size = tmp;
					heap_room -= tmp;
					info_index++;
					return info_index-1;

				}else{
					return NULL_VAL;
				}
				break;
			case Free:

				if(tmp == NULL_VAL){
					return NoReturn;
				}else if(tmp == UNKNOWN || tmp >= info_index || info[tmp].deleted == true){

					return Error;
				}else{

					info[tmp].deleted = true;
					heap_room += info[tmp].size;

					return NoReturn;
				}
				break;
			case Clone:

				if(tmp == NULL_VAL){
					return NULL_VAL;
				}else if(tmp == UNKNOWN || tmp >= info_index || info[tmp].deleted == true){

					return Error;
				}else{
					if(info[tmp].size <= heap_room){

						info[info_index].size = info[tmp].size;
						heap_room -= info[info_index].size;
						info_index++;
						return info_index-1;

					}else{
						return NULL_VAL;
					}
				}
				break;
			case None:
				return tmp;
				break;
			}
			index = close_pos+1;
			pre = None;
			break;
		case 'm':
			pre = Malloc;
			index += 6;
			break;
		case 'f':
			pre = Free;
			index += 4;
			break;
		case 'c':
			pre = Clone;
			index += 5;
			break;
		default:

			if(buf[index] >= 'A' && buf[index] <= 'Z'){

				if(buf[index] == 'N' && buf[index+1] == 'U'){
					return NULL_VAL;
				}

				int loc = buf[index]-'A';

				if(buf[index+1] == '='){

					tmp = parse(index+2,right);
					value_table[loc] = tmp;

					return value_table[loc];

				}else if(index == right){
					return value_table[loc];
				}
			}else{

				tmp = 0;
				for(int i = index; i <= right && buf[i] >= '0' && buf[i] <= '9'; i++){
					tmp = 10*tmp+(buf[i]-'0');
					if(tmp > max_room){
						return max_room+1;
					}
				}
				return tmp;
			}
			break;
		}
	}
	return NULL_VAL; //must not reach here
}

int main(){

	for(int i = 0; i < 10000; i++){
		info[i].size = -1;
		info[i].deleted = false;
	}

	for(int i = 0; i < 26; i++){
		value_table[i] = UNKNOWN;
	}

	scanf("%d",&heap_room);
	max_room = heap_room;

	int length;

	info_index = 0;

	while(scanf("%s",buf) != EOF){

		for(length = 0; buf[length] != 0; length++);

		if(parse(0,length-1) == Error){
			printf("Error\n");
			return 0;
		}
	}

	int ans = 0;
	bool FLG;

	for(int i = 0; i < info_index; i++){

		if(info[i].deleted == false){

			FLG = false;
			for(int k = 0; k < 26; k++){
				if(value_table[k] == i){
					FLG = true;
					break;
				}
			}

			if(!FLG){
				ans += info[i].size;
			}
		}
	}

	printf("%d\n",ans);

	return 0;
}

