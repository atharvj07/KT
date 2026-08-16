#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define HUGE_NUM 99999999999999999
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;


#define NUM 205
#define SIZE 12


enum Type{
	Open_Curve,
	Close_Curve,
	Open_Rect,
	Close_Rect,
	Expression,
	Operator,
	Op_Exp,
	Exp_Op,
	Exp_Close_Curve,
	Exp_Close_Rect,
	Open_Curve_Exp,
	Open_Rect_Exp,
};

struct Info{
	Info(int arg_from,int arg_to,Type arg_type){
		from = arg_from;
		to = arg_to;
		type = arg_type;
	}
	int from,to;
	Type type;
};


int V,E;
int start,goal;
bool dp[SIZE][NUM][NUM]; //dp[構成部品][from][to] = その構成部品が成り立つか

void func(){

	start--;
	goal--;

	for(int i = 0; i < SIZE; i++){
		for(int from = 0; from < V; from++){
			for(int to = 0; to < V; to++){
				dp[i][from][to] = false;
			}
		}
	}

	int from,to;
	char buf[2];

	queue<Info> Q;
	Type type;

	for(int loop = 0; loop < E; loop++){

		scanf("%d %d %s",&from,&to,buf);
		from--;
		to--;

		switch(buf[0]){
		case '(':
			type = Open_Curve;
			break;
		case ')':
			type = Close_Curve;
			break;
		case '[':
			type = Open_Rect;
			break;
		case ']':
			type = Close_Rect;
			break;
		case 'a':
			type = Expression;
			break;
		case '+':
			type = Operator;
			break;
		case '*':
			type = Operator;
			break;
		}

		dp[type][from][to] = true;
		Q.push(Info(from,to,type));
	}

	while(!Q.empty()){

		switch(Q.front().type){
		case Open_Curve:

			//Expを探す
			for(int next = 0; next < V; next++){
				if(dp[Expression][Q.front().to][next] == true && dp[Open_Curve_Exp][Q.front().from][next] == false){
					dp[Open_Curve_Exp][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Open_Curve_Exp));
				}
			}

			//Exp)を探す
			for(int next = 0; next < V; next++){
				if(dp[Exp_Close_Curve][Q.front().to][next] == true && dp[Expression][Q.front().from][next] == false){
					dp[Expression][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Expression));
				}
			}

			break;
		case Close_Curve:

			//Expを探す
			for(int pre = 0; pre < V; pre++){
				if(dp[Expression][pre][Q.front().from] == true && dp[Exp_Close_Curve][pre][Q.front().to] == false){
					dp[Exp_Close_Curve][pre][Q.front().to] = true;
					Q.push(Info(pre,Q.front().to,Exp_Close_Curve));
				}
			}

			//(Expを探す
			for(int pre = 0; pre < V; pre++){
				if(dp[Open_Curve_Exp][pre][Q.front().from] == true && dp[Expression][pre][Q.front().to] == false){
					dp[Expression][pre][Q.front().to] = true;
					Q.push(Info(pre,Q.front().to,Expression));
				}
			}

			break;
		case Open_Rect:

			//Expを探す
			for(int next = 0; next < V; next++){
				if(dp[Expression][Q.front().to][next] == true && dp[Open_Rect_Exp][Q.front().from][next] == false){
					dp[Open_Rect_Exp][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Open_Rect_Exp));
				}
			}

			//Exp]を探す
			for(int next = 0; next < V; next++){
				if(dp[Exp_Close_Rect][Q.front().to][next] == true && dp[Expression][Q.front().from][next] == false){
					dp[Expression][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Expression));
				}
			}

			break;
		case Close_Rect:

			//Expを探す
			for(int pre = 0; pre < V; pre++){
				if(dp[Expression][pre][Q.front().from] == true && dp[Exp_Close_Rect][pre][Q.front().to] == false){
					dp[Exp_Close_Rect][pre][Q.front().to] = true;
					Q.push(Info(pre,Q.front().to,Exp_Close_Rect));
				}
			}

			//[Expを探す
			for(int pre = 0; pre < V; pre++){
				if(dp[Open_Rect_Exp][pre][Q.front().from] == true && dp[Expression][pre][Q.front().to] == false){
					dp[Expression][pre][Q.front().to] = true;
					Q.push(Info(pre,Q.front().to,Expression));
				}
			}

			break;
		case Expression:

			//(を探す
			for(int pre = 0; pre < V; pre++){
				if(dp[Open_Curve][pre][Q.front().from] == true && dp[Open_Curve_Exp][pre][Q.front().to] == false){
					 dp[Open_Curve_Exp][pre][Q.front().to] = true;
					 Q.push(Info(pre,Q.front().to,Open_Curve_Exp));
				}
			}

			//[を探す
			for(int pre = 0; pre < V; pre++){
				if(dp[Open_Rect][pre][Q.front().from] == true && dp[Open_Rect_Exp][pre][Q.front().to] == false){
					 dp[Open_Rect_Exp][pre][Q.front().to] = true;
					 Q.push(Info(pre,Q.front().to,Open_Rect_Exp));
				}
			}

			//)を探す
			for(int next = 0; next < V; next++){
				if(dp[Close_Curve][Q.front().to][next] == true && dp[Exp_Close_Curve][Q.front().from][next] == false){
					dp[Exp_Close_Curve][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Exp_Close_Curve));
				}
			}

			//]を探す
			for(int next = 0; next < V; next++){
				if(dp[Close_Rect][Q.front().to][next] == true && dp[Exp_Close_Rect][Q.front().from][next] == false){
					dp[Exp_Close_Rect][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Exp_Close_Rect));
				}
			}

			//Op_Expを探す
			for(int next = 0; next < V; next++){
				if(dp[Op_Exp][Q.front().to][next] == true && dp[Expression][Q.front().from][next] == false){
					dp[Expression][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Expression));
				}
			}

			//Exp_Opを探す
			for(int pre = 0; pre < V; pre++){
				if(dp[Exp_Op][pre][Q.front().from] == true && dp[Expression][pre][Q.front().to] == false){
					dp[Expression][pre][Q.front().to] = true;
					Q.push(Info(pre,Q.front().to,Expression));
				}
			}

			//Opを探す(Op_Expを作る)
			for(int pre = 0; pre < V; pre++){
				if(dp[Operator][pre][Q.front().from] == true && dp[Op_Exp][pre][Q.front(),to] == false){
					dp[Op_Exp][pre][Q.front(),to] = true;
					Q.push(Info(pre,Q.front().to,Op_Exp));
				}
			}

			//Opを探す(Exp_Opを作る)
			for(int next = 0; next < V; next++){
				if(dp[Operator][Q.front().to][next] == true && dp[Exp_Op][Q.front().from][next] == false){
					dp[Exp_Op][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Exp_Op));
				}
			}

			break;
		case Operator:

			//Expを探す(Op_Expを作る)
			for(int next = 0; next < V; next++){
				if(dp[Expression][Q.front().to][next] == true && dp[Op_Exp][Q.front().from][next] == false){
					dp[Op_Exp][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Op_Exp));
				}
			}

			//Expを探す(Exp_Opを作る)
			for(int pre = 0; pre < V; pre++){
				if(dp[Expression][pre][Q.front().from] == true && dp[Exp_Op][pre][Q.front().to] == false){
					dp[Exp_Op][pre][Q.front().to] = true;
					Q.push(Info(pre,Q.front().to,Exp_Op));
				}
			}

			break;
		case Op_Exp:

			//Expを探す
			for(int pre = 0; pre < V; pre++){
				if(dp[Expression][pre][Q.front().from] == true && dp[Expression][pre][Q.front().to] == false){
					dp[Expression][pre][Q.front().to] = true;
					Q.push(Info(pre,Q.front().to,Expression));
				}
			}

			break;
		case Exp_Op:

			//Expを探す
			for(int next = 0; next < V; next++){
				if(dp[Expression][Q.front().to][next] == true && dp[Expression][Q.front().from][next] == false){
					dp[Expression][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Expression));
				}
			}

			break;
		case Exp_Close_Curve:

			//(を探す
			for(int pre = 0; pre < V; pre++){
				if(dp[Open_Curve][pre][Q.front().from] == true && dp[Expression][pre][Q.front().to] == false){
					dp[Expression][pre][Q.front().to] = true;
					Q.push(Info(pre,Q.front().to,Expression));
				}
			}

			break;
		case Exp_Close_Rect:

			//[を探す
			for(int pre = 0; pre < V; pre++){
				if(dp[Open_Rect][pre][Q.front().from] == true && dp[Expression][pre][Q.front().to] == false){
					dp[Expression][pre][Q.front().to] = true;
					Q.push(Info(pre,Q.front().to,Expression));
				}
			}

			break;
		case Open_Curve_Exp:

			//)を探す
			for(int next = 0; next < V; next++){
				if(dp[Close_Curve][Q.front().to][next] == true && dp[Expression][Q.front().from][next] == false){
					dp[Expression][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Expression));
				}
			}

			break;
		case Open_Rect_Exp:

			//]を探す
			for(int next = 0; next < V; next++){
				if(dp[Close_Rect][Q.front().to][next] == true && dp[Expression][Q.front().from][next] == false){
					dp[Expression][Q.front().from][next] = true;
					Q.push(Info(Q.front().from,next,Expression));
				}
			}

			break;
		}

		Q.pop();
	}

	if(dp[Expression][start][goal]){

		printf("Yes\n");

	}else{

		printf("No\n");
	}
}

int main(){

	while(true){
		scanf("%d %d %d %d",&V,&E,&start,&goal);
		if(V == 0)break;

		func();
	}

	return 0;
}

