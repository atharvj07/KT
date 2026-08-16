import java.util.PriorityQueue;
import java.util.Scanner;
  
public class Main {
      
    static class State implements Comparable<State>{
        int x, y, l, r, money, oxygen;
        State(int x, int y, int l, int r, int money, int oxygen){
            this.x=x;
            this.y=y;
            this.l=l;
            this.r=r;
            this.money=money;
            this.oxygen=oxygen;
        }
        public int compareTo(State s) {
            if(this.money==s.money) {
                return s.oxygen-this.oxygen;
            }
            return this.money-s.money;
        }
    }
      
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)){
            while(sc.hasNext()) {
                int w=sc.nextInt();
                int h=sc.nextInt();
                if(w+h==0) break;
                int f=sc.nextInt();
                int m=sc.nextInt();
                int o=sc.nextInt();
                int[][] ox=new int[h+1][w+1];
                int[][] cost=new int[h+1][w+1];
                int[][][][][] dis=new int[51][11][11][11][11];
                int[] dx= {1, 0, -1};
                int[] dy= {0, 1, 0};
                int INF=Integer.MAX_VALUE;
                  
                for(int i=1; i<=h; i++) {
                    for(int j=1; j<=w; j++) {
                        int k=sc.nextInt();
                        if(k<0) {
                            cost[i][j]=-k;
                        }else {
                            ox[i][j]=k;
                            cost[i][j]=0;
                        }
                    }
                }
                for(int i=0; i<51; i++) {
                    for(int y=1; y<=h; y++) {
                        for(int x=1; x<=w; x++) {
                            for(int y1=1; y1<=w; y1++) {
                                for(int x1=1; x1<=w; x1++) {
                                    dis[i][y][x][y1][x1]=INF;
                                }
                            }
                        }
                    }
                }
                PriorityQueue<State> pq=new PriorityQueue<>();
                for(int j=1; j<=w; j++) {
                    if(o-1<=0) continue;
                    pq.add(new State(j, 1, j, j, cost[1][j], Math.min(o-1+ox[1][j], m)));
                }
                int ans=INF;
                while(!pq.isEmpty()) {
                    State state=pq.poll();
                    if(dis[state.oxygen][state.y][state.x][state.l][state.r]<=state.money) continue;
                    if(state.oxygen<=0) continue;
                    if(state.money>f) break;
                    if(state.y==h) {
                        ans=state.money;
                        break;
                    }
                    dis[state.oxygen][state.y][state.x][state.l][state.r]=state.money;
                    //System.out.println(state.y+", "+state.x+" ox="+state.oxygen+" m="+state.money);
                    for(int i=0; i<3; i++) {
                        int nx=state.x+dx[i], ny=state.y+dy[i];
                        if(nx<1 || nx>w || ny<1 || ny>h) continue;
                        int nl=Math.min(state.l, nx), nr=Math.max(state.r, nx);
                        int no=state.oxygen-1, ncost=state.money;
                        if(no<=0) continue;
                        if(i==1) {
                            nl=nx; nr=nx;
                        }
                        if(i==1 || nx<state.l || state.r<nx) {
                            ncost+=cost[ny][nx];
                            no=Math.min(m, no+ox[ny][nx]);
                        }
                        pq.add(new State(nx, ny, nl, nr, ncost, no));
                    }
                }
                System.out.println(ans==INF? "NA":ans);
                pq.clear();
            }
              
        }
    }
}
