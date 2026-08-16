import java.util.*;
 
public class Main{
 
    int[] v;
    int[] dx = {0,0,1,-1};
    int[] dy = {1,-1,0,0};
 
    void solve(){
        Scanner sc = new Scanner(System.in);

        calc();
 
        while(sc.hasNext()){
            String pzl = "";
            for(int i=0; i<2; i++)
                for(int j=0; j<4; j++) pzl += sc.next();

            System.out.println(v[Integer.parseInt(pzl)/10]);
        }
    }
 
    void calc(){
        Queue<int[]> q = new LinkedList<int[]>();
        q.add(new int[]{1234567,0,0,0});

        v = new int[7654322];
        Arrays.fill(v,-1);
 
        while(q.size()>0){
            int[] pp = q.poll();
            int pzz = pp[0], x = pp[1], y = pp[2], cnt = pp[3];
  
            if(v[pzz/10]!=-1) continue;
            v[pzz/10] = cnt;
 
            String pzzs = String.valueOf(pzz);
            if(pzzs.length()==7) pzzs = "0" + pzzs;
            char[] c = pzzs.toCharArray();
 
            for(int i=0; i<4; i++){
                int nx = x+dx[i], ny = y+dy[i];
                if(nx<0 || nx>=4 || ny<0 || ny>=2) continue;
                c[y*4+x] = c[ny*4+nx];
                c[ny*4+nx] = '0';
                int ns = Integer.parseInt(String.valueOf(c));
                q.add(new int[]{ns,nx,ny,cnt+1});
                c[ny*4+nx] = c[y*4+x];
                c[y*4+x] ='0';
            }
        }
    }
 
    public static void main(String[] args){
        new Main().solve();
    }
}