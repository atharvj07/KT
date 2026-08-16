import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class KefaAndPark {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Vertex[] v = new Vertex[n];
        
        int isCat;
        for(int i = 0; i < n; i++) {
            isCat = sc.nextInt();
            if(isCat == 1)
                v[i] = new Vertex(true);
            else
                v[i] = new Vertex(false);
        }
        
        for(int i = 0; i < n-1; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            
            v[x-1].adj.add(y-1);
            v[y-1].adj.add(x-1);
        }
        
        sc.close();
        System.out.println(dfs(0, -1, 0, m, v));
    }
    
    private static int dfs(int curr, int parent, int cats, int m, Vertex[] v) {
        if(v[curr].hasCat)
            cats++;
        
        if(cats > m)
            return 0;
        
        if(v[curr].adj.size() == 1 && v[curr].adj.get(0) == parent) {
            return 1;
        }
        
        int sum = 0;
        for(int next : v[curr].adj) {
            if(next == parent) continue;
            if(v[curr].hasCat)
                sum += dfs(next, curr, cats, m, v);
            else
                sum += dfs(next, curr, 0, m, v);
        }
        return sum;
    }

    private static class Vertex {
        boolean hasCat;
        List<Integer> adj;
        
        Vertex(boolean b) {
            hasCat = b;
            adj = new ArrayList<>();
        }
    }
}
