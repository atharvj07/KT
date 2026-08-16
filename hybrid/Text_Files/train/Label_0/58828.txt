import java.util.*;
import java.io.*;
import java.util.LinkedList; 
import java.util.Queue; 
public class test{

    static boolean[] visited;
    static ArrayList<Integer>[] adja;

    public static void main(String[] args) {
        FastReader in=new FastReader();
        int n=in.nextInt();
        adja=new ArrayList[n+1];
        visited=new boolean[n+1];
        for(int i=0;i<=n;i++) adja[i]=new ArrayList<>();
        for(int i=0;i<n-1;i++){
            int a=in.nextInt(), b=in.nextInt();
            adja[a].add(b);
            adja[b].add(a);
        }
       System.out.println(dfs(1));
    }
    
    public static double bfs(int n){
        Queue<Integer> q = new LinkedList<>(); 
        double res=0;
        int num=0;
        int[] dist=new int[n+1];
        q.add(1);
        dist[1]=0;
        while(!q.isEmpty()){
            int e=q.poll();
            visited[e]=true;
            Iterator<Integer> itr=adja[e].iterator();
            int isLeaf=0;
            while(itr.hasNext()){
                isLeaf++;
                int v=itr.next();
                if(!visited[v]){
                    dist[v]=dist[e]+1;
                    q.add(v);
                }
            }
            if(isLeaf<=1){
                res+=dist[e];
                num++;
            }
        }
        return (double) res/num;
    }

    public static double dfs(int s){
        
        visited[s]=true;
        double ans=0 , n=0;
        for(int i=0;i<adja[s].size();i++){
            int v=adja[s].get(i);
            if(!visited[v]){
                ans+=dfs(v)+1;
                n++;
            }
        }
        if(ans==0) return 0;
        return (double) (ans/n) ;
        }

    public static void pirntArray(Object[] a){
        System.out.print("{");
        for(int i=0;i<a.length-1;i++)
            System.out.print(a[i]+", ");
        System.out.println(a[a.length-1]+"}");
    }

    static class FastReader{
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new
                   InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException  e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}