#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<complex>
#include<string>
#include<cmath>

using namespace std;

#define reps(i,f,n) for(int i=f;i<int(n);i++)
#define rep(i,n) reps(i,0,n)

const int H = 50;
const int D = 30;
const int W = 100;

const double EPS = 0.00000001;

class Tank{
	public:
	int w,h;
	int flow;
	double sum;
	bool used;
	Tank(int w,int h):w(w),h(h){
		flow = 0;
		sum = 0;
		used = false;
	}
	double getheight(){
		double size = w*D;
		return sum/size;
	}
};

class Event{
	public:
	int kind;
	double time;
	int pos;
	int cnum;
	int tank;
	Event(int kind,double time,int pos,int cnum,int tank):
		kind(kind),time(time),pos(pos),cnum(cnum),tank(tank){}
	bool operator<(const Event a)const{
		return time<a.time;
	}
};

typedef pair<int,int> pii;

int n,m,r;
vector<Tank> tank;
vector<pii> check;
double checkans[100];

int getpos(int w){
	int ret = 0;
	int sum = 0;
	rep(i,tank.size()){
		if(sum >= w)break;
		ret = i;
		sum += tank[i].w;
	}
	return ret;
}

void print(){
	printf("Tank\n");
	rep(i,tank.size()){
		double size = tank[i].w*D;
		double height = tank[i].sum/size;
		printf("w=%d h=%d flow=%d sum=%lf used=%d height=%lf\n",
			tank[i].w,tank[i].h,tank[i].flow,tank[i].sum,tank[i].used,height);
	}puts("");
}

void printevent(vector<Event>& event){
	printf("Event\n");
	rep(i,event.size()){
		if(event[i].kind)printf("tank  ");
		else printf("watch ");
		printf("time=%lf pos=%d tank=%d\n",event[i].time, event[i].pos, event[i].tank);
	}puts("");
}

void addcheck(double time, vector<Event>& event){
	rep(i,check.size()){
		if(checkans[i]+EPS>=0)continue;
		event.push_back(Event(0, check[i].second-time, check[i].first, i, -1));
	}
}

int leftwall(int pos){
	if(pos==0)return H;
	return tank[pos-1].h;
}
int rightwall(int pos){
	return tank[pos].h;
}

void addtank(vector<Event>& event){
	if(tank.size()==1 && tank[0].getheight()+EPS>H)return;
	
	rep(i,tank.size()){
		if(tank[i].used)continue;
		if(tank[i].flow==0)continue;
		
		int under = tank[i].w * D;
		
		int left = leftwall(i);
		int right = rightwall(i);
		
		int mini = min(left,right);
		
		int size = under*mini;
		double rest = size - tank[i].sum;
		
		double time = rest/tank[i].flow;
		
		event.push_back(Event(1, time, -1, -1, i));
	}
}

void flowtank(double time){
	rep(i,tank.size()){
		tank[i].sum += tank[i].flow*time;
		tank[i].sum = min((double)H*D*tank[i].w, tank[i].sum);
	}
}

void margetank(){
	rep(i,tank.size()){
		int right = rightwall(i);
		int left = leftwall(i);
		
		double height = tank[i].sum / (tank[i].w * D);
		
		if(right==left){
			
		}else if(right<left){
			if(height+EPS>right){
				double opheight = tank[i+1].sum/(tank[i+1].w*D);
				if(opheight+EPS>right){
					tank[i].h = tank[i+1].h;
					tank[i].w += tank[i+1].w;
					tank[i].flow += tank[i+1].flow;
					tank[i].sum += tank[i+1].sum;
					
					tank.erase(tank.begin()+i+1);
					i=0;
				}else{
					tank[i+1].flow += tank[i].flow;
					tank[i].flow = 0;
					
				}
			}
		}else{
			if(height+EPS>left){
				double opheight = tank[i-1].sum/(tank[i-1].w*D);
				if(opheight+EPS>left){
					tank[i].h = tank[i-1].h;
					tank[i].w += tank[i-1].w;
					tank[i].flow += tank[i-1].flow;
					tank[i].sum += tank[i-1].sum;
					tank.erase(tank.begin()+i-1);
					i=0;
				}else{
					tank[i-1].flow += tank[i].flow;
					tank[i].flow = 0;
				}
			}
		}
	}
}

void solve(){
	cin>>n;
	
	rep(i,100)checkans[i]=-1;
	
	int befb = 0;
	tank.clear();
	rep(i,n){
		int b,h;
		cin>>b>>h;
		tank.push_back(Tank(b-befb, h));
		befb = b;
	}
	tank.push_back(Tank(W-befb, H));
	
	cin>>m;
	rep(i,m){
		int f,a;
		cin>>f>>a;
		tank[ getpos(f) ].flow += a;
	}
	
	check.clear();
	cin>>r;
	rep(i,r){
		int p,t;
		cin>>p>>t;
		check.push_back(pii(p,t));
	}
	
	//print();
	
	double time = 0;
	while(1){
		
		vector<Event> event;
		addcheck(time, event);
		addtank(event);
		
		if(event.size()==0)break;
		
		sort(event.begin(), event.end());
		
		//printf("i=%d time=%lf\n",pp,time);
		//printevent(event);
		flowtank(event[0].time);
		time += event[0].time;
		margetank();
		//print();
		
		if(event[0].kind==false){
			int pos = getpos(event[0].pos);
			double under = tank[pos].w * D;
			//printf("!!!!!!!!!!!!!!!!!!!! %lf\n", tank[pos].sum/under);
			
			checkans[event[0].cnum] = tank[pos].sum/under;
		}
		//break;
	}
	
	rep(i,check.size()){
		printf("%.14lf\n",checkans[i]);
	}
}

int main(){
	
	int d;
	cin>>d;
	
	rep(i,d){
		solve();
	}
}

/*
1
5
15 40
35 20
50 45
70 30
80 10
2
60 4
75 1
3
60 6000
75 6000
85 6000

*/