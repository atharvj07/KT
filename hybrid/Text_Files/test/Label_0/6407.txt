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

int* parent,*height;

struct Info{
	Info(){
		cost = -1;
	}
	char name[11];
	int cost;
};

bool strCmp(char* base, char* comp){
	int length1 = 0,length2 = 0;
	for(int i=0;base[i] != '\0'; i++)length1++;
	for(int i=0;comp[i] != '\0'; i++)length2++;
	if(length1 != length2)return false;

	for(int i=0;base[i] != '\0'; i++){
		if(base[i] != comp[i])return false;
	}
	return true;
}

int getParent(int id){
	if(parent[id] == id)return id;
	else{
		return parent[id] = getParent(parent[id]);
	}
}

bool isSame(int left,int right){
	return getParent(left) == getParent(right);
}

void unite(int left,int right){
	int left_parent = getParent(left);
	int right_parent = getParent(right);

	if(left_parent == right_parent)return;

	if(height[left_parent] >= height[right_parent]){
		if(height[left_parent] == height[right_parent]){
			height[left_parent]++;
		}
		parent[right_parent] = left_parent;
	}else{
		parent[left_parent] = right_parent;
	}
}


int main(){

	int N,M;
	scanf("%d",&N);
	parent = new int[N];
	height = new int[N];

	int* min_cost = new int[N];

	Info info[N];

	for(int i = 0; i < N; i++){
		parent[i] = i;
		height[i] = 0;
	}

	for(int i = 0; i < N; i++){
		scanf("%s %d",info[i].name,&info[i].cost);
		min_cost[i] = info[i].cost;
	}

	char left[11],right[11];
	int left_id,right_id;

	scanf("%d",&M);

	for(int loop = 0; loop < M; loop++){
		scanf("%s %s",left,right);

		for(int i = 0; i < N; i++){
			if(strCmp(left,info[i].name)){
				left_id = i;
				break;
			}
		}

		for(int i = 0; i < N; i++){
			if(strCmp(right,info[i].name)){
				right_id = i;
				break;
			}
		}

		unite(left_id,right_id);
	}

	for(int i = 0; i < N; i++){
		for(int k = 0; k < N; k++){
			if(isSame(i,k)){
				min_cost[i] = min(min_cost[i],info[k].cost);
			}
		}
	}

	int sum = 0;
	for(int i = 0; i < N; i++)sum += min_cost[i];

	printf("%d\n",sum);

	return 0;
}