
import java.util.*;


/**
 * Created by shoya on 2017/04/12.
 */
public class Main {
    public static void main(String... args){
        Scanner sc = new Scanner(System.in);
        int V = sc.nextInt();
        int E = sc.nextInt();
        KruskalClass krus = new KruskalClass(V, E);
        //System.out.printf("%d %d \n", V, E);
        for (int i = 0; i < E; i++) {
            int s = sc.nextInt();
            int d = sc.nextInt();
            int c = sc.nextInt();
            //System.out.printf("%d %d %d\n", s, d, c);
            krus.addEdge(s, d, c);
        }
        System.out.println(krus.kruskal());
        return;
    }

    public static class KruskalClass {
        class edge {
            int node1, node2, cost;
            edge(int node1, int node2, int cost){
                this.node1 = node1;
                this.node2 = node2;
                this.cost = cost;
            }
        }

        private int V, E;
        List<edge> edges = new ArrayList<edge>();

        KruskalClass(int V, int E){
            this.V = V;
            this.E = E;
        }

        public void addEdge(int source, int dest, int cost){
            edges.add(new edge(source, dest, cost));
        }

        public int kruskal(){
            UFT uft = new UFT(V);
            edges.sort((a, b) -> a.cost - b.cost);
            //Collections.sort(edges);

            int res = 0;
            for (edge e : edges){
                if (!uft.same(e.node1, e.node2)) {
                    uft.unite(e.node1, e.node2);
                    res += e.cost;
                }
            }
            return res;
        }

    }

   public static class UFT {
        int size;
        int rootsOfNodes[];

        public UFT(int n){
            size = n;
            int i = 1;
            while (i < n) i *= 2;
            rootsOfNodes = new int[n];
            for (int j = 0; j < n; j++)
                rootsOfNodes[j] = j;
        }

        private int depth(int node, int depth){
            if (node == rootsOfNodes[node])
                return depth;
            return depth(rootsOfNodes[node], depth + 1);
        }

        public void unite(int x, int y){
            int lower;
            int root;
            if (depth(x, 0) > depth(y, 0)) {
                lower = x;
                root = root(y);
            }
            else {
                lower = y;
                root = root(x);
            }
            while(lower != rootsOfNodes[lower]){
                int next = rootsOfNodes[lower];
                rootsOfNodes[lower] = root;
                lower = next;
            }
            rootsOfNodes[lower] = root;
        }

        private int root(int node) {
            if (node == rootsOfNodes[node])
                return node;
            return root(rootsOfNodes[node]);
        }

        public boolean same(int x, int y){
            return root(x) == root(y);
        }

        void print(){
            for (int i = 0; i < size; i++)
                System.out.printf("%d <-- Root -- %d\n", rootsOfNodes[i], i);
        }

    }


}