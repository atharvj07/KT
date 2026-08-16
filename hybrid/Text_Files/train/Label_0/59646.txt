import java.util.*;
import java.io.*;

class Graph {
    public ArrayList<Integer>[] adjacency;

    Graph(int n){
        adjacency = new ArrayList[n];
        for(int i = 0; i < n; i++){
            adjacency[i] = new ArrayList<Integer>();
        }
    }

    public void add_edge(int from, int to, boolean is_directed){
        adjacency[from].add(to);
        if(!is_directed){
            adjacency[to].add(from);
        }        
    }
}

public class Main {
    
    static Graph graph;
    static List<Integer> u_to_v_path = new LinkedList<Integer>();
    
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] in1 = br.readLine().split(" ");
        int N = Integer.parseInt(in1[0]);
        int u = Integer.parseInt(in1[1]);
        int v = Integer.parseInt(in1[2]);
        u--; v--;
        graph = new Graph(N);
        for(int i = 0; i < N-1; i++){
            in1 = br.readLine().split(" ");
            int A = Integer.parseInt(in1[0]);
            int B = Integer.parseInt(in1[1]);
            graph.add_edge(A-1, B-1, false);
        }
        br.close();
        find_u_to_v_path(u, v, -1);

        int u_v_length = u_to_v_path.size();

        int start_point = u_to_v_path.get(u_v_length / 2 - 1);
        int start_parent = u_to_v_path.get(u_v_length / 2);

        int ans = u_v_length / 2 + dfs(start_point, start_parent) - 1;
        if(u_v_length % 2 == 1){
            ans++;
        }
        System.out.println(ans);
    }

    public static boolean find_u_to_v_path(int u, int v, int parent){
        if(u == v) {
            u_to_v_path.add(u);
            return true;
        }

        for(int next : graph.adjacency[v]){
            if(next == parent) continue;
            if(find_u_to_v_path(u, next, v)){
                u_to_v_path.add(v);
                return true;
            }
        }

        return false;
    }

    public static int dfs(int now, int parent){
        if(graph.adjacency[now].size() == 1 && graph.adjacency[now].get(0) == parent){
            return 0;
        }

        int ret = 0;

        for(int next : graph.adjacency[now]){
            if(next == parent) continue;
            ret = Math.max(ret, dfs(next, now));
        }

        return ret + 1;
    }
}