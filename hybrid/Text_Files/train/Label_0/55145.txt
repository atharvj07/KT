import java.util.*;
import java.io.*;
 
public class Main {
    static char[][] map;
    static boolean[][] arrived;
    public static void main(String[] args) throws Exception {
        FastScanner sc = new FastScanner(System.in);
        int h = sc.nextInt();
        int w = sc.nextInt();
        map = new char[h][w];
        for(int i = 0; i < h; i++){
            map[i] = sc.next().toCharArray();
        }
        arrived = new boolean[h][w];
        long ans = 0;
        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; j++){
                if(!arrived[i][j]){
                    arrived[i][j] = true;
                    ans += bfs(i, j, h, w);
                }
            }
        }
        System.out.println(ans);
    }
    
    public static long bfs(int iy, int jx, int h, int w){
        long dot = 0;
        long sharp = 0;
        int[] my = {-1,0,0,1};
        int[] mx = {0,-1,1,0};
        Deque<Panel> dq = new ArrayDeque<Panel>();
        dq.add(new Panel(iy,jx));
        while(dq.size() > 0){
            Panel p = dq.poll();
            int y = p.y;
            int x = p.x;
            if(map[y][x] == '#'){
                sharp++;
            }else{
                dot++;
            }
            for(int ii = 0; ii < 4; ii++){
                int ny = y + my[ii];
                int nx = x + mx[ii];
                if(checkPanel(ny,nx,h,w) && !arrived[ny][nx] && map[y][x] != map[ny][nx]){
                    arrived[ny][nx] = true;
                    dq.add(new Panel(ny,nx));
                }
            }
        }
        return sharp*dot;
    }
    
    public static boolean checkPanel(int y, int x, int h, int w){
        return (0 <= y && y < h && 0 <= x && x < w);
    }
}

class Panel{
    int x,y;
    public Panel(int y, int x){
        this.x = x;
        this.y = y;
    }
}

class FastScanner {
    private BufferedReader reader = null;
    private StringTokenizer tokenizer = null;
    public FastScanner(InputStream in) {
        reader = new BufferedReader(new InputStreamReader(in));
        tokenizer = null;
    }

    public String next() {
        if (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                tokenizer = new StringTokenizer(reader.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken();
    }

    public String nextLine() {
        if (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                return reader.readLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken("\n");
    }

    public long nextLong() {
        return Long.parseLong(next());
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }

    public double nextDouble() {
         return Double.parseDouble(next());
    }
    
    public String[] nextArray(int n) {
        String[] a = new String[n];
        for (int i = 0; i < n; i++)
            a[i] = next();
        return a;
    }

    public int[] nextIntArray(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = nextInt();
        return a;
    }

    public long[] nextLongArray(int n) {
        long[] a = new long[n];
        for (int i = 0; i < n; i++)
            a[i] = nextLong();
        return a;
    } 
}
