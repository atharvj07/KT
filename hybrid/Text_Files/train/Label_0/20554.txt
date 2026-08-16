#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define HUGE_NUM 99999999999999999
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;


#define NUM 105

enum Type{
	START,
	SERVER_CHECK,
	FINISH,
	SUBMIT,
};

struct Info{
	Info(){
		type = START;
		event_time = 0;
		player_id = 0;
	}
	Info(Type arg_type,int arg_event_time,int arg_player_id){
		type = arg_type;
		event_time = arg_event_time;
		player_id = arg_player_id;
	}
	bool operator<(const struct Info &arg) const{
		if(event_time != arg.event_time){
			return event_time > arg.event_time;
		}else{
			return type > arg.type;
		}
	}
	Type type;
	int event_time,player_id;
};

int case_num;
int num_player,num_problem;
int num_submit;
int sum_submit[NUM],sum_receive[NUM];
int data_size[NUM],delay[NUM];
bool is_this_time[NUM],submit_check[NUM];
priority_queue<Info> Q;

int get_len(char buf[20]){

	int ret;

	for(ret = 0; buf[ret] != '\0'; ret++);

	return ret;
}

void func(){

	for(int i = 0; i < num_player; i++){
		scanf("%d",&delay[i]);
	}

	for(int i = 0; i < num_player; i++){
		sum_submit[i] = 0;
		sum_receive[i] = 0;
	}

	int tmp_id,tmp_time,tmp_len;
	char buf[20];

	for(int a = 0; a < num_problem; a++){

		scanf("%d",&num_submit);

		for(int i = 0; i < num_player; i++){
			data_size[i] = -1;
			is_this_time[i] = false;
			submit_check[i] = false;
		}

		Q.push(Info(START,0,-1));
		Q.push(Info(FINISH,20000,-1));

		for(int i = 1000; i <= 20000; i += 1000){
			Q.push(Info(SERVER_CHECK,i,-1));
		}

		for(int loop = 0; loop < num_submit; loop++){

			scanf("%d %d %s",&tmp_id,&tmp_time,buf);
			tmp_len = get_len(buf);
			data_size[tmp_id] = tmp_len;
			Q.push(Info(SUBMIT,tmp_time+2*delay[tmp_id],tmp_id));
		}

		Info info;
		int num_this_time,num_total = 0,size_this_time,size_total = 0;

		while(!Q.empty()){
			info = Q.top();
			Q.pop();

			switch(info.type){
			case START:

				for(int i = 0; i < num_player; i++){
					sum_receive[i] += 3;
				}
				break;

			case SUBMIT:

				is_this_time[info.player_id] = true;
				submit_check[info.player_id] = true;
				sum_submit[info.player_id] += (data_size[info.player_id]+5);

				break;
			case SERVER_CHECK:

				num_this_time = 0;
				size_this_time = 0;

				for(int i = 0; i < num_player; i++){
					if(is_this_time[i]){
						num_this_time++;
						size_this_time += data_size[i];
					}
				}

				num_total += num_this_time;
				size_total += size_this_time;

				for(int i = 0; i < num_player; i++){

					if(!submit_check[i]){

						if(num_this_time > 0){

							sum_receive[i] += (num_this_time+4);
						}

					}else{

						if(is_this_time[i]){

							if(num_total > 1){

								sum_receive[i] += (2*(num_total-1)+(size_total-data_size[i])+4);
							}

						}else{

							if(num_this_time > 0){

								sum_receive[i] += (2*num_this_time+size_this_time+4);
							}
						}
					}
				}

				for(int i = 0; i < num_player; i++){

					is_this_time[i] = false;
				}

				break;
			case FINISH:

				for(int i = 0; i < num_player; i++){

					sum_receive[i] += 4;
				}
				break;
			}
		}
	}

	int total_submit = 0,total_receive = 0;

	for(int i = 0; i < num_player; i++){
		total_submit += sum_submit[i];
		total_receive += sum_receive[i];
	}

	if(case_num > 0)printf("\n");

	printf("%d %d\n",total_receive,total_submit);

	for(int i = 0; i < num_player; i++){

		printf("%d %d\n",sum_submit[i],sum_receive[i]);
	}

	case_num++;
}


int main(){

	case_num = 0;

	while(true){

		scanf("%d %d",&num_player,&num_problem);
		if(num_player == 0 && num_problem == 0)break;

		func();
	}

	return 0;
}

