#include<iostream>
#include<functional>
#include<algorithm>

const int N = 11;
const int inf = 1<<27;
const int di[] = {-1,1,1,-1};
const int dj[] = {1,1,-1,-1};

using namespace std;

int H,W;
static int M[N][N];
static int maxSizes[N][N][4];
int oneCount;
int minHW;
int ans;
int greedy_ans;
int depth;
int maxSize;

inline int getHeuristic();
void calc();
void solve(int pos);

inline int getHeuristic()
{
  int msz=maxSize;
  msz *= msz;
  return oneCount/msz + (oneCount%msz>0);
}

struct Cand{
  int i,j;
  Cand():i(0),j(0){}
  Cand(int ci, int cj):i(ci),j(cj){}
  bool operator<(const Cand& t)const{
    return (i==t.i)?(j<t.j):(i<t.i);
  }
};

int cand_num;
Cand cands[N*N];

void calc(){
  for(int i = 0; i < H; ++i){
    for(int j = 0; j < W; ++j){
      if(M[i][j] == 1){
	oneCount++;
	cands[cand_num++] = Cand(i,j);
      }
      for(int k = 0; k < 4; ++k){
	int size = 0;
	for(size = 1; size <= minHW; ++size){
	  for(int m = i; (k==0||k==3)?(m>i-size):(m<size+i); m+=di[k]){
	    for(int n = j; (k==2||k==3)?(n>j-size):(n<size+j); n+=dj[k]){
	      if( m<0||n<0||m>=H||n>=W||M[m][n]==0 ){
		--size;
		goto next;
	      }
	    }
	  }
	  if(k==0){
	    if(i-size<0||j+size>=W)break;
	  }else if(k==1){
	    if(i+size>=H||j+size>=W)break;
	  }else if(k==2){
	    if(i+size>=H||j-size<0)break;
	  }else{
	    if(i-size<0||j-size<0)break;
	  }
	}
      next:;
	maxSizes[i][j][k] = size;
	if(k==1){
	  if(size>1){
	    maxSize = max( maxSize, size );
	  }
	}
      }
    }
  }
  sort(cands,cands+cand_num);
  return ;
}

void solve_greedy()
{
  // completed.
  if(oneCount==0){
    greedy_ans = min(greedy_ans, depth);
    return ;
  }

  // embed carpet greedy
  int maxOneCount = -1;
  int maxp,maxk,maxsz;
  for(int p = 0; p < cand_num; ++p){
    int i = cands[p].i;
    int j = cands[p].j;
    if( M[i][j] == 1 ){
      for(int k = 0; k < 4; ++k){
	int cnt = 0;
	int size = maxSizes[i][j][k];
	for(int m = i; (k==0||k==3)?(m>i-size):(m<size+i); m+=di[k]){
	  for(int n = j; (k==2||k==3)?(n>j-size):(n<size+j); n+=dj[k]){
	    if(M[m][n]==1){
	      ++cnt;
	    }
	  }
	}
	if(maxOneCount<cnt){
	  maxp = p;
	  maxk = k;
	  maxsz = size;
	  maxOneCount = cnt;
	}
      }
    }
  }
  int i = cands[maxp].i;
  int j = cands[maxp].j;
  int k = maxk;
  int size = maxsz;
  for(int m = i; (k==0||k==3)?(m>i-size):(m<size+i); m+=di[k]){
    for(int n = j; (k==2||k==3)?(n>j-size):(n<size+j); n+=dj[k]){
      if(M[m][n]==1){
	M[m][n]=depth;
	--oneCount;
      }
    }
  }
  ++depth;
  solve_greedy();
  --depth;
  for(int m = i; (k==0||k==3)?(m>i-size):(m<size+i); m+=di[k]){
    for(int n = j; (k==2||k==3)?(n>j-size):(n<size+j); n+=dj[k]){
      if( M[m][n] == depth ){
	M[m][n]=1;
	++oneCount;
      }
    }
  }
  return ;
}

void solve(int pos){
  /*
    printf("now i = %d, now j = %d, h = %d\n", pos/W, pos%W, getHeuristic());
    for(int k = 0; k < H; ++k){
      for(int l = 0; l < W; ++l){
	if(l>0)putchar(' ');
	printf("%2d", M[k][l]);
      }
      putchar('\n');
    }
    putchar('\n');
  */

  // completed.
  if(oneCount==0){
    ans = min(ans, depth);
    return ;
  }

  // back
  if(depth+getHeuristic()>=ans){
    return ;
  }

  // embed carpet
  for(int p = pos; p < cand_num; ++p){
    int i = cands[p].i;
    int j = cands[p].j;
    int size = maxSizes[i][j][1];
    int valid=0;
    for(int m = i; m<size+i; m++){
      for(int n = j; n<size+j; n++){
	if(M[m][n]==1){
	  valid=1;
	  --oneCount;
	  M[m][n]=depth;
	}
      }
    }
    if( valid ){
      ++depth;
      solve(p+1);
      --depth;
    }
    for(int m = i; m<size+i; m++){
      for(int n = j; n<size+j; n++){
	if( M[m][n] == depth ){
	  ++oneCount;
	  M[m][n]=1;
	}
      }
    }
    if( M[i][j] > 1 )
      solve(p+1);
    return ;
  }
}

int main()
{
  while(true){
    scanf("%d%d", &W, &H);
    if(W==H&&H==0)break;
    for(int i = 0; i < H; ++i){
      for(int j = 0; j < W; ++j){
	scanf("%d", &M[i][j]);
      }
    }

    minHW = min(H,W);
    oneCount = 0;
    cand_num = 0;
    ans=inf;
    greedy_ans = inf;
    depth=2;
    maxSize = 1;

    calc();

    solve_greedy();
    ans = greedy_ans;
    solve(0);

    printf("%d\n", ans-2);
  }
  return 0;
}