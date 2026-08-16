#include<iostream>
#include<queue>
using namespace std;
typedef pair<pair<int,int>,int> pa;
#define ff first.first
#define fs first.second

int h,w,sx,sy,gx,gy;
int dx[4]={1,0,-1,0};
int dy[4]={0,-1,0,1};
int co[21][21];
char ma[21][21];
bool visited[21][21];
string pat;
int m = 999999;

int main(){
    while(cin>>h>>w,h){
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                co[i][j]=m;
                cin>>ma[i][j];
                if(ma[i][j]=='A')
                    sx=j,sy=i;
                else if(ma[i][j]=='B')
                    gx=j,gy=i;
            }
        }
        queue<pa>q;
        q.push(make_pair(make_pair(sx, sy), 0));
        while(q.size()){
            pa p = q.front();
            q.pop();
            if(co[p.fs][p.ff]!=m)
                continue;
            co[p.fs][p.ff]=p.second;
            for(int i=0;i<4;i++){
                int nx=p.ff+dx[i];
                int ny=p.fs+dy[i];
                if(nx>=0&&nx<w&&ny>=0&ny<h&&ma[ny][nx]!='#'&&co[ny][nx]==m)
                    q.push(make_pair(make_pair(nx, ny), p.second+1));
            }
        }
        cin>>pat;
        for(int j=0,go=0;;j++,go++){
            int i=j%pat.length();
            if(co[gy][gx]<=go){
                cout<<go<<" "<<gy<<" "<<gx<<endl;
                break;
            }
            if(go>1000){
                cout<<"impossible"<<endl;
                break;
            }
            if(pat[i]=='8')
                gy--;
            else if(pat[i]=='6')
                gx++;
            else if(pat[i]=='4')
                gx--;
            else if(pat[i]=='2')
                gy++;
            gy=max(0,min(h-1,gy));
            gx=max(0,min(w-1,gx));
        }
    }
}