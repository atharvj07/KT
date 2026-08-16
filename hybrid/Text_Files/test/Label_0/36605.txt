import java.util.*;

public class Main{

    int w,h;
    char[][] l,r;
    int lx,ly,rx,ry;
    boolean found;
    boolean[][][][] v;
    int[] dx = {0,0,1,-1};
    int[] dy = {1,-1,0,0};

    void solve(){
        Scanner sc = new Scanner(System.in);

        while(true){
            w = sc.nextInt();
            h = sc.nextInt();
            if(w==0 && h==0) break;

            l = new char[h][w];
            r = new char[h][w];
            for(int i=0; i<h; i++){
                String s1 = sc.next();
                String s2 = sc.next();
                s2 = new StringBuffer(s2+"").reverse().toString();

                l[i] = s1.toCharArray();
                r[i] = s2.toCharArray();
                for(int j=0; j<w; j++){
                    if(l[i][j]=='L'){
                        lx = j; ly = i;
                    }
                    if(r[i][j]=='R'){
                        rx = j; ry = i;
                    }
                }
            }

            found = false;
            v = new boolean[w][h][w][h];
            bfs();

            if(found) System.out.println("Yes");
            else System.out.println("No");
        }
    }

    void bfs(){
        LinkedList<int[]> list = new LinkedList<int[]>();
        list.add(new int[]{lx,ly,rx,ry});
        
        while(list.size()>0){
            int[] lr = list.poll();
            int xl = lr[0], yl = lr[1], xr = lr[2], yr = lr[3];

            if(l[yl][xl]=='%' && r[yr][xr]=='%'){
                found = true;
                return;
            }
            if(l[yl][xl]=='%' || r[yr][xr]=='%') continue;

            if(v[xl][yl][xr][yr]) continue;
            v[xl][yl][xr][yr] = true;

            for(int i=0; i<4; i++){
                int nxl = xl+dx[i], nyl = yl+dy[i], nxr = xr+dx[i], nyr = yr+dy[i];
                if(nxl<0 || nxl>=w || nyl<0 || nyl>=h || l[nyl][nxl]=='#'){
                    nxl = xl; nyl = yl;
                }
                if(nxr<0 || nxr>=w || nyr<0 || nyr>=h || r[nyr][nxr]=='#'){
                    nxr = xr; nyr = yr;
                }
                if(nxl==xl && nyl==yl && nxr==xr && nyr==yr) continue;
                list.add(new int[]{nxl,nyl,nxr,nyr});
            }
        }
    }

    public static void main(String[] args){
        new Main().solve();
    }
}