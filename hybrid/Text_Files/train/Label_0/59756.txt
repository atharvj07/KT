import java.io.*;
import java.lang.reflect.Array;
import java.security.cert.TrustAnchor;
import java.util.*;

/**
 * Created by noureldin on 2/20/17.
 */

public class main {

    private static int m,n;
    private static long k;
    private static int [] [] G;
    private static int [] dx = {0,-1,0,1},dy = {-1,0,1,0};
    private static boolean [] [] vis;
    private static int rootX,rootY;

    private static int dfs(int x,int y,int div){
        vis[x][y] = true;
        int ret = 1;
        for (int i = 0;i < 4;i++){
            int nx = x + dx[i],ny = y + dy[i];
            if(nx < 0 || nx >= m || ny < 0 || ny >= n || vis[nx][ny] || G[nx][ny] < div) continue;
            ret += dfs(nx,ny,div);
        }
        return ret;
    }


    private static void getAnswer(int div,long target){
        for (int i = 0;i < m;i++)
            for (int j = 0;j < n;j++)
                vis[i][j] = false;

        Queue<node> Q = new LinkedList<node>();
        Q.add(new node(rootX,rootY));
        vis[rootX][rootY] = true;
        for (int t = 0;t < target;t++){
            assert !Q.isEmpty();
            node cur = Q.poll();
            int x = cur.x,y = cur.y;
            G[x][y] = div;
            for (int i = 0;i < 4;i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n || vis[nx][ny] || G[nx][ny] < div) continue;
                vis[nx][ny] = true;
                Q.add(new node(nx, ny));
            }
        }
        while (!Q.isEmpty()){
            node cur = Q.poll();
            int x = cur.x,y = cur.y;
            vis[x][y] = false;
        }
        for (int i = 0;i < m;i++)
            for (int j = 0;j < n;j++)
                if(!vis[i][j])
                    G[i][j] = 0;
    }
    private static boolean valid(int div,long target){
        for (int i = 0;i < m;i++)
            for (int j = 0;j < n;j++)
                vis[i][j] = false;
        for (int i = 0;i < m;i++)
            for (int j = 0;j < n;j++)
                if(!vis[i][j] && G[i][j] == div){
                    rootX = i;
                    rootY = j;
                    if(dfs(i,j,div) >= target) return true;
                }
        return false;
    }
    public static void main(String[] args) throws Exception{
        IO io = new IO(null,null);
        m = io.getNextInt();
        n = io.getNextInt();
        k = io.getNextLong();
        G = new int[m][n];
        vis = new boolean[m][n];
        TreeSet<Integer> TS = new TreeSet<>();
        for (int i = 0;i < m;i++)
            for (int j = 0;j < n;j++) {
                G[i][j] = io.getNextInt();
                if(k%G[i][j] == 0)
                    TS.add(G[i][j]);
            }
        boolean done = false;
        for (int div : TS)
            if(valid(div,k/div)){
                getAnswer(div,k/div);
                io.println("YES");
                for (int i = 0;i < m;i++) {
                    for (int j = 0; j < n; j++)
                        io.print(G[i][j] + " ");
                    io.println("");
                }
                done = true;
                break;
            }
        if(!done) io.println("NO");

        io.close();
    }
}


class node{
    int x,y;
    public node(int x,int y){
        this.x = x;
        this.y = y;
    }
}


class IO{
    private BufferedReader br;
    private StringTokenizer st;
    private PrintWriter writer;
    private String inputFile,outputFile;

    public String getNext() throws FileNotFoundException, IOException{
        while(st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
        return st.nextToken();
    }

    public String getNextLine() throws FileNotFoundException, IOException{
        return br.readLine();
    }

    public int getNextInt() throws FileNotFoundException, IOException{
        return Integer.parseInt(getNext());
    }
    public long getNextLong() throws FileNotFoundException, IOException{
        return Long.parseLong(getNext());
    }

    public void print(double x,int num_digits) throws  IOException{
        writer.printf("%." + num_digits + "f" ,x);
    }
    public void println(double x,int num_digits) throws  IOException{
        writer.printf("%." + num_digits + "f\n" ,x);
    }
    public void print(Object o) throws  IOException{
        writer.print(o.toString());
    }

    public void println(Object o) throws  IOException{
        writer.println(o.toString());
    }
    public IO(String x,String y) throws FileNotFoundException, IOException{
        inputFile = x;
        outputFile = y;
        if(x != null) br = new BufferedReader(new FileReader(inputFile));
        else br = new BufferedReader(new InputStreamReader(System.in));
        if(y != null) writer = new PrintWriter(new BufferedWriter(new FileWriter(outputFile)));
        else writer = new PrintWriter(new OutputStreamWriter(System.out));
    }

    protected void close() throws IOException{
        br.close();
        writer.close();
    }
}