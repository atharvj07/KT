import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

class Main{

    static class Edge{
        int[] v=new int[2];
        int[] cnt=new int[2];
        long w;
        Edge(int u1,int u2){v[0]=u1;v[1]=u2;}
    }

    static List<Edge> edges[];
    static boolean[] used;
    static int dfs(int v){
        used[v]=true;
        int res =1;
        for(Edge e : edges[v]){
            int i = e.v[0]==v ? 1:0;
            if(used[e.v[i]])continue;
            e.cnt[i]=dfs(e.v[i]);
            res += e.cnt[i];
        }
        return res;
    }

    static long dfs2(int v){
        used[v]=true;
        long res =0;
        for(Edge e: edges[v]){
            int i = e.v[0]==v ? 1:0;
            if(used[e.v[i]])continue;
            res += dfs2(e.v[i]);
            res += e.w*(long)e.cnt[i];
        }
        return res;
    }
    

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        edges = new ArrayList[N];
        used = new boolean[N];
        List<Edge> edgeList = new ArrayList<>();
        for(int i=0;i<N;++i)edges[i]=new ArrayList<>();
        for(int i=0;i<N-1;++i){
            int a = scan.nextInt()-1;
            int b = scan.nextInt()-1;
            Edge e = new Edge(a, b);
            edgeList.add(e);
            edges[a].add(e);
            edges[b].add(e);
        }
        long[] s = new long[N];
        for(int i=0;i<N;++i)s[i]=scan.nextLong();
        dfs(0);
        for(Edge e: edgeList){
            if(e.cnt[0]==0)e.cnt[0]=N-e.cnt[1];
            else e.cnt[1]=N-e.cnt[0];
        }
        Edge equal=null;
        for(Edge e:edgeList){
            if(e.cnt[0]==e.cnt[1]){
                equal=e;
                e.w=0;
            }
            else e.w = ((s[e.v[0]] - s[e.v[1]])/((long)(e.cnt[1]-e.cnt[0])));
        }
        if(equal != null){
            Arrays.fill(used, false);
//            System.out.println(dfs2(equal.v[0]));
            equal.w = (s[equal.v[0]] - dfs2(equal.v[0])) / (equal.cnt[0]);
        }
        for(Edge e:edgeList)System.out.println(e.w);
    }
}