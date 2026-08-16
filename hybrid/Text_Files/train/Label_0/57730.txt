import java.io.*;
import java.util.*;

public class D2{        
    
        class node{
            
            int num;
            long dist;
            public node(int a,long b){
                num = a;
                dist = b;
            }
        }
        private BufferedReader in;  
        private StringTokenizer st;
        
        ArrayList<node>[] g;
        int[][]taxies;
        long[][]map;
        long[]sp;
        long inf = 1l<<45;                 
        
        void bfs(int src){
            
            Queue<node> q = new LinkedList<node>();
            node st = new node(src, taxies[src][0]);
            q.add(st);
            long c = taxies[src][1];
            boolean[]visited = new boolean[map.length];
            while(!q.isEmpty()){
                                
                node curr = q.remove();
                if(visited[curr.num]) continue;
                visited[curr.num] = true;
                for (int i = 0; i < g[curr.num].size(); i++) {
                    
                    node tmp = g[curr.num].get(i);
                    long diff = curr.dist - tmp.dist;
                    if(diff >= 0){
                        map[src][tmp.num] = c;
                        node nxt = new node(tmp.num, diff);
                        q.add(nxt);
                    }
                }
            }
        }
        
        void dijkstra(int src){
            
            boolean []visited = new boolean[map.length];
            for(int i = 0;i<map.length;++i){
                
                long min = inf;
                int node = -1;
                for (int j = 0; j < visited.length; j++) {
                    if(!visited[j]){
                        if(sp[j] < min){
                            min = sp[j];
                            node = j;
                        }
                    }
                }
                if(node == -1) break;
                visited[node] = true;
                for (int j = 0; j < visited.length; j++) {
                    if(visited[j]) continue;
                    sp[j] = Math.min(sp[j], sp[node] + map[node][j]);
                }
            }
            
        }
        void solve() throws IOException{
            
            int n = nextInt();
            int m = nextInt();
            int st = nextInt() - 1;
            int end = nextInt() - 1;
            g = new ArrayList[n];
            for (int i = 0; i < g.length; i++) {
                g[i] = new ArrayList<node>();               
            }
            for (int i = 0; i < m; i++) {
                int a = nextInt() - 1;
                int b = nextInt() - 1;
                int c = nextInt();
                g[a].add(new node(b,c));
                g[b].add(new node(a, c));
            }
            taxies = new int[n][2];
            for (int i = 0; i < n; i++) {
                taxies[i][0] = nextInt();
                taxies[i][1] = nextInt();
            }
            map = new long[n][n];
            for (int i = 0; i < map.length; i++) {
                Arrays.fill(map[i], inf);
                map[i][i] = 0;
            }
            sp = new long[n];
            for (int i = 0; i < n; i++) {
                bfs(i);
            }
            Arrays.fill(sp, inf);
            sp[st] = 0;
            dijkstra(st);
            if(sp[end] < inf){
                System.out.println(sp[end]);
            }
            else System.out.println(-1);
                        
        }
            

        D2() throws IOException {
            in = new BufferedReader(new InputStreamReader(System.in));          
            eat("");
            solve();            
        }

        private void eat(String str) {
            st = new StringTokenizer(str);
        }

        String next() throws IOException {
            while (!st.hasMoreTokens()) {
                String line = in.readLine();
                if (line == null) {
                    return null;
                }
                eat(line);
            }
            return st.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        public static void main(String[] args) throws IOException {
            new D2();
        }

        int gcd(int a,int b){
            if(b>a) return gcd(b,a);
            if(b==0) return a;
            return gcd(b,a%b);
        }

}
