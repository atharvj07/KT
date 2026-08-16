#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;
#define BIG_NUM 2000000000
#define HUGE_NUM 99999999999999999
#define MOD 1000000007
#define EPS 0.000000001
using namespace std;



#define SIZE 8

struct Point{
	Point(double arg_x,double arg_y){
		x = arg_x;
		y = arg_y;
	}

	Point(){
		x = y = 0.0;
	}

	Point operator + (Point p){ return Point(x+p.x,y+p.y); }
	Point operator - (Point p){ return Point(x-p.x,y-p.y);}
	Point operator * (double a){ return Point(a*x,a*y); }
	Point operator / (double a){ return Point(x/a,y/a); }

	double abs(){ return sqrt(norm()); }
	double norm(){ return x*x + y*y; }

	bool operator<(const Point &p) const{
		return x != p.x? x < p.x: y < p.y;
	}

	bool operator == (const Point &p) const{
		return fabs(x-p.x) < EPS && fabs(y-p.y) < EPS;
	}

	double x,y;
};

typedef Point Vector;

struct Line{
	Line(){

	}
	Line(Point a,Point b){
		p[0] = a;
		p[1] = b;
	}
	Point p[2];
};

int N;
int boss[8],height[8],table[30];
int REFLECT[8][30];
double NUM = 10000;
Point info[8];
vector<Line> LINE;

int get_boss(int id){
	if(boss[id] == id)return id;
	else{
		return boss[id] = get_boss(boss[id]);
	}
}

void unite(int x,int y){
	int boss_x = get_boss(x);
	int boss_y = get_boss(y);

	if(boss_x == boss_y)return;

	if(height[x] > height[y]){

		boss[boss_y] = boss_x;

	}else if(height[x] < height[y]){

		boss[boss_x] = boss_y;

	}else{ //height[x] == height[y]

		boss[boss_y] = boss_x;
		height[x]++;
	}
}

void init(){

	for(int i = 0; i < N; i++){

		boss[i] = i;
		height[i] = 0;
	}
}


double norm(Vector a){
	return a.x*a.x+a.y*a.y;
}

double abs(Vector a){
	return sqrt(norm(a));
}

double cross(Vector a,Vector b){
    return a.x*b.y-a.y*b.x;
}

double dot(Vector a,Vector b){
    return a.x*b.x + a.y*b.y;
}

Point calc_Reflection_Point(double x1,double y1,double x2,double y2,double xp,double yp){

	Point ret;

	bool X_FLG = false,Y_FLG = false;
	double slope;

	if(y1 == y2){
		X_FLG = true;
	}else if(x1 == x2){
		Y_FLG = true;
	}else{
		slope = (y2-y1)/(x2-x1);
	}

	if(X_FLG){
		ret.x = xp,ret.y=y1;
	}else if(Y_FLG){
		ret.x = x1,ret.y = yp;
	}else{
		ret.x = (yp*(x2-x1)*(y2-y1)+xp*(x2-x1)*(x2-x1)-y1*(y2-y1)*(x2-x1)+x1*(y2-y1)*(y2-y1))/((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1));
		ret.y = ((x1-x2)*ret.x+yp*(y2-y1)+xp*(x2-x1))/(y2-y1);
	}
	ret.x = 2*ret.x-xp;
	ret.y = 2*ret.y-yp;

	return ret;
}

Point calc_Reflection_Point(Line line,Point point){

	return calc_Reflection_Point(line.p[0].x,line.p[0].y,line.p[1].x,line.p[1].y,point.x,point.y);
}

bool equals(Point A,Point B){

	return abs(A-B) < EPS;
}

double calc_slope(Line A){

	if(fabs(A.p[0].x-A.p[1].x) < EPS){

		return DBL_MAX;

	}else if(fabs(A.p[0].y-A.p[1].y) < EPS){

		return 0;

	}else{

		return (A.p[0].y-A.p[1].y)/(A.p[0].x-A.p[1].x);
	}
}

//点Aと点Bの垂直二等分線を求める
void calc_Vertical_Bisector(Point A,Point B){

	double first_slope = calc_slope(Line(A,B));
	Point mid_Point = Point((A.x+B.x)/2,(A.y+B.y)/2);

	Point another;

	if(fabs(first_slope) < EPS){ //AとBが水平に位置している場合

		another.x = mid_Point.x;
		another.y = mid_Point.y+NUM;

	}else if(fabs(first_slope-DBL_MAX) < EPS){ //AとBが垂直に位置している場合

		another.x = mid_Point.x+NUM;
		another.y = mid_Point.y;

	}else{ //その他

		double slope = -1.0/first_slope;

		another.x = mid_Point.x+NUM;
		another.y = mid_Point.y+NUM*slope;
	}
	LINE.push_back(Line(mid_Point,another));
}

bool dfs(vector<int> LINE_TO_USE,int index,int num_line){

	if(index == LINE.size()){

		if(LINE_TO_USE.size() != num_line)return false;

		init();

		for(int i = 0; i < N; i++){
			for(int k = 0; k < num_line; k++){

				if(REFLECT[i][LINE_TO_USE[k]] == -1)continue;

				unite(i,REFLECT[i][LINE_TO_USE[k]]);
			}
		}

		int num_group = 0;
		for(int i = 0; i < N; i++){
			if(i == get_boss(i)){

				num_group++;
			}
		}

		return num_group == 1; //全てが互いに行き来可能になったらOK
	}

	bool ret = dfs(LINE_TO_USE,index+1,num_line); ////LINE[index]を使わない
	if(ret){

		return true;
	}

	if(LINE_TO_USE.size() == num_line)return false; //これ以上増やせないならfalseをreturn

	//LINE[index]を使う
	vector<int> next_LINE_TO_USE = LINE_TO_USE;
	next_LINE_TO_USE.push_back(index);

	return dfs(next_LINE_TO_USE,index+1,num_line);
}

bool is_OK(int num_line){

	vector<int> LINE_TO_USE; //使う直線の集合

	return dfs(LINE_TO_USE,0,num_line);
}

//対称移動を事前計算しておく
void calc_Reflect(){

	for(int i = 0; i < N; i++){
		for(int k = 0; k < LINE.size(); k++){

			REFLECT[i][k] = -1;
		}
	}

	for(int i = 0; i < N; i++){
		for(int k = 0; k < LINE.size(); k++){

			Point tmp = calc_Reflection_Point(LINE[k],info[i]);

			for(int a = 0; a < N; a++){
				if(a == i)continue;

				if(equals(info[a],tmp)){

					REFLECT[i][k] = a;
				}
			}
		}
	}
}

int main(){

	scanf("%d",&N);

	for(int i = 0; i < N; i++){

		scanf("%lf %lf",&info[i].x,&info[i].y);
	}

	for(int i = 0; i < N-1; i++){
		for(int k = i+1; k < N; k++){
			calc_Vertical_Bisector(info[i],info[k]); //垂直二等分線をあらかじめ全計算しておく
		}
	}

	calc_Reflect();

	int minimum = N-1; //少なくともN-1本あればクリア可能

	for(int num_line = 1; num_line < minimum; num_line++){
		if(is_OK(num_line)){

			minimum = num_line;
			break;
		}
	}

	printf("%d\n",minimum);

	return 0;
}


