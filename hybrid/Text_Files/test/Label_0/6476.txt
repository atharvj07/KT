#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<n;++i)
#define rep1(i,n) for(int i=1;i<=n;++i)
using namespace std;
int a[52][52]={};
int dx[4]={0,0,-1,1};
int dy[4]={-1,1,0,0};
int h,w;

//color 0=. 1=B -1=W 2=b -2=w 10=*

void paint(int y,int x,int color){
    if((fabs(a[y][x])!=2 && a[y][x]!=0) || a[y][x]==color)return;//
    if(fabs(a[y][x]-color)==4)color = 10;
    a[y][x] = color;
    rep(i,4)paint(y+dy[i],x+dx[i],color);
}

int main(void){
    char tmp;
    while(cin>>w>>h, w|h){
        int cntB=0,cntW=0;
        /*??\???*/
        rep1(y,h){
            rep1(x,w){
                cin>>tmp;
                if(tmp=='.')a[y][x] = 0;
                else if(tmp=='B')a[y][x] = 1;
                else a[y][x] = -1;
            }
        }

        /*?£??¨????*/
        rep(y,h+2)a[y][0]=a[y][w+1] = 100;
        rep(x,w+2)a[0][x]=a[h+1][x] = 100;

        /*????????????*/
        rep1(y,h){
            rep1(x,w){
                if(a[y][x] == 1)      rep(i,4)paint(y+dy[i],x+dx[i],2);
                else if(a[y][x] == -1)rep(i,4)paint(y+dy[i],x+dx[i],-2);
            }
        }

        rep1(y,h){
            rep1(x,w){
                if(a[y][x]==2)cntB++;
                else if(a[y][x]==-2)cntW++;
            }
        }
        cout<<cntB<<" "<<cntW<<endl;
    }

    return 0;
}