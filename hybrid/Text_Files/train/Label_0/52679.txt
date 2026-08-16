import java.util.*;
import java.io.*;
import java.text.*;
public class Main{
    //SOLUTION BEGIN
    //Into the Hardware Mode
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int n = ni(), b = ni();
        int q = ni();
        int[][] p = new int[1+q][];
        for(int i = 0; i< q; i++)p[i] = new int[]{ni(), ni()};
        p[q] = new int[]{b, n};
        boolean yes = true;
        Arrays.sort(p, (int[] i1, int[] i2) -> Integer.compare(i1[0], i2[0]));
        for(int i = 1; i<= q; i++)yes &= p[i][1] >= p[i-1][1];
        if(!yes){
            pn("unfair");
            return;
        }
        q++;
        Dinic d = new Dinic(2+5+q);
        for(int i = 0, pr = 0, sum = 0; i< q; i++){
            d.addEdge(0, 2+5+i, p[i][1]-sum);
            sum = p[i][1];
            int[] f = new int[5];
            while(1+pr <= p[i][0]){
                pr++;
                f[pr%5]++;
            }
            for(int j = 0; j< 5; j++)
                d.addEdge(2+5+i, 2+j, f[j]);
        }
        for(int i = 0; i< 5; i++)d.addEdge(2+i, 1, n/5);
        long f = d.dinic(0, 1);
        yes &= f == n;
        pn(yes?"fair":"unfair");
    }
    class Dinic{
        final long IINF = (long)1e18;
        int V;
        int[] level;
        ArrayList<Edge>[] adj;
        public Dinic(int v){
            V = v;
            adj = new ArrayList[V];
            for(int i = 0; i< V; i++)adj[i] = new ArrayList<>();
            level = new int[V];
        }
        
        void addEdge(int u, int v, long w){
            Edge a = new Edge(v,0,w,adj[v].size());
            Edge b = new Edge(u,0,0,adj[u].size());
            adj[u].add(a);
            adj[v].add(b);
        }
        
        long dinic(int s, int t){
            if(s==t)return 0;
            long total = 0;
            while(bfs(s,t)){
                int[] start = new int[V];
                long flow = 0;
                while((flow = sendFlow(s,t,IINF, start)) >0)total+=flow;
            }
            return total;
        }
        
        long sendFlow(int u, int t, long flow, int[] start){
            if(u==t)return flow;
            for(; start[u]<adj[u].size(); start[u]++){
                Edge e = adj[u].get(start[u]);
                if(level[e.v] == level[u]+1 && e.flow<e.c){
                    long cur = Math.min(flow, e.c-e.flow);
                    long tmp_flow = sendFlow(e.v,t, cur, start);
                    if(tmp_flow>0){
                        e.flow+=tmp_flow;adj[e.v].get(e.rev).flow -= tmp_flow;
                        return tmp_flow;
                    }
                }
            }
            return 0;
        }
        
        boolean bfs(int s, int t){
            for(int i = 0; i< V; i++)level[i] = -1;
            level[s] = 0;
            Queue<Integer> q = new LinkedList<>();
            q.add(s);
            while(!q.isEmpty()){
                int x = q.poll();
                for(Edge e:adj[x]){
                    if(level[e.v] == -1 && e.flow<e.c){
                        level[e.v] = level[x]+1;
                        q.add(e.v);
                    }
                }
            }
            return level[t]>=0;
        }
        class Edge{
            int v, rev;
            long flow, c;
            public Edge(int V, long F, long C, int R){
                v = V;flow = F;c = C;rev = R;
            }
        }
    }
    //SOLUTION END
    void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
    long IINF = (long)1e18, mod = (long)1e9+7;
    final int INF = (int)1e9, MX = (int)2e5+5;
    DecimalFormat df = new DecimalFormat("0.00");
    double PI = 3.141592653589793238462643383279502884197169399, eps = 1e-6;
    static boolean multipleTC = false, memory = false, fileIO = false;
    FastReader in;PrintWriter out;
    void run() throws Exception{
        if(fileIO){
            in = new FastReader("input.txt");
            out = new PrintWriter("output.txt");
        }else {
            in = new FastReader();
            out = new PrintWriter(System.out);
        }
        //Solution Credits: Taranpreet Singh
        int T = (multipleTC)?ni():1;
        pre();for(int t = 1; t<= T; t++)solve(t);
        out.flush();
        out.close();
    }
    public static void main(String[] args) throws Exception{
        if(memory)new Thread(null, new Runnable() {public void run(){try{new Main().run();}catch(Exception e){e.printStackTrace();}}}, "1", 1 << 28).start();
        else new Main().run();
    }
    long gcd(long a, long b){return (b==0)?a:gcd(b,a%b);}
    int gcd(int a, int b){return (b==0)?a:gcd(b,a%b);}
    int bit(long n){return (n==0)?0:(1+bit(n&(n-1)));}
    void p(Object o){out.print(o);}
    void pn(Object o){out.println(o);}
    void pni(Object o){out.println(o);out.flush();}
    String n()throws Exception{return in.next();}
    String nln()throws Exception{return in.nextLine();}
    int ni()throws Exception{return Integer.parseInt(in.next());}
    long nl()throws Exception{return Long.parseLong(in.next());}
    double nd()throws Exception{return Double.parseDouble(in.next());}
 
    class FastReader{
        BufferedReader br;
        StringTokenizer st;
        public FastReader(){
            br = new BufferedReader(new InputStreamReader(System.in));
        }
 
        public FastReader(String s) throws Exception{
            br = new BufferedReader(new FileReader(s));
        }
 
        String next() throws Exception{
            while (st == null || !st.hasMoreElements()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch (IOException  e){
                    throw new Exception(e.toString());
                }
            }
            return st.nextToken();
        }
 
        String nextLine() throws Exception{
            String str = "";
            try{   
                str = br.readLine();
            }catch (IOException e){
                throw new Exception(e.toString());
            }  
            return str;
        }
    }
}