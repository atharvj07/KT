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


struct Node{
	int table[26];
	bool finish_FLG;
};

Node nodes[200001];

int node_index = 1,N,length;
ll dp[100001];
char buf[100001];

ll recursive(int start_pos){

	if(dp[start_pos] != -1)return dp[start_pos];

	stack<int> S;

	int tmp_ch,tmp_node_index = 0,ch_loc = start_pos,depth = 0;

	while(true){
		tmp_ch = buf[ch_loc]-'a';

		if(nodes[tmp_node_index].table[tmp_ch] == -1)break;

		tmp_node_index = nodes[tmp_node_index].table[tmp_ch];
		depth++;

		if(nodes[tmp_node_index].finish_FLG){
			S.push(start_pos+depth);
		}

		ch_loc++;

		if(buf[ch_loc] == '\0')break;
	}

	dp[start_pos] = 0;

	while(!S.empty()){
		dp[start_pos] += recursive(S.top());
		dp[start_pos] %= MOD;
		S.pop();
	}

	dp[start_pos] %= MOD;

	return dp[start_pos];
}

int main(){

	for(int i = 0; i <= 200000; i++){
		for(int k = 0; k < 26; k++)nodes[i].table[k] = -1;
		nodes[i].finish_FLG = false;
	}

	scanf("%d",&N);

	int tmp_ch,tmp_node_index,ch_loc;

	for(int loop = 0; loop < N; loop++){
		scanf("%s",buf);

		tmp_node_index = 0;
		ch_loc = 0;

		while(true){
			tmp_ch = buf[ch_loc]-'a';

			if(nodes[tmp_node_index].table[tmp_ch] == -1){
				nodes[tmp_node_index].table[tmp_ch] = node_index;
				tmp_node_index = node_index;
				node_index++;
			}else{
				tmp_node_index = nodes[tmp_node_index].table[tmp_ch];
			}
			ch_loc++;
			if(buf[ch_loc] == '\0'){
				nodes[tmp_node_index].finish_FLG = true;
				break;
			}
		}
	}

	scanf("%s",buf);

	for(length = 0; buf[length] != '\0'; length++);
	for(int i = 0; i < length; i++)dp[i] = -1;
	dp[length] = 1;

	printf("%lld\n",recursive(0));

	return 0;
}