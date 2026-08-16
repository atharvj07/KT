import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.OutputStream;
import java.util.HashMap;
import java.util.LinkedList;
public class C {
    private static class Node {
        LinkedList<Node> childs = new LinkedList<>();
        int col;
        boolean visited = false;
        public Node(int col) {
            this.col = col;
        }
    }
    public static void main(String args[]) {
        Sc sc = new Sc(System.in);
        int n = sc.nI();
        int m = sc.nI();
        int k = sc.nI();
        Node[] socks = new Node[n];
        for(int i = 0; i<n; i++) {
            socks[i] = new Node(sc.nI());
        }
        for(int i = 0; i<m; i++) {
            int l = sc.nI() - 1;
            int r = sc.nI() - 1;
            socks[l].childs.add(socks[r]);
            socks[r].childs.add(socks[l]);
        }
        int change = 0;
        for(int i = 0; i<n; i++) {
            if(socks[i].visited) continue;
            HashMap<Integer, Integer> map = new HashMap<>();
            int sum = 1;
            int max = 1;
            map.put(socks[i].col,1);
            LinkedList<Node> active = new LinkedList<>();
            active.add(socks[i]);
            socks[i].visited = true;
            while(!active.isEmpty()) {
                Node nod = active.pollFirst();
                for(Node ch: nod.childs) {
                    if(ch.visited) continue;
                    ch.visited = true;
                    active.addLast(ch);
                    if(map.containsKey(ch.col)) map.put(ch.col, map.get(ch.col) + 1);
                    else map.put(ch.col,1);
                    sum++;
                    max = Math.max(max, map.get(ch.col));
                }
            }
            change += sum - max;
        }
        System.out.println(change);
    }
}
class Sc {
    public Sc(InputStream i) {
        r = new BufferedReader(new InputStreamReader(i));
    }

    public boolean hasM() {
        return peekToken() != null;
    }

    public int nI() {
        return Integer.parseInt(nextToken());
    }

    public double nD() { 
        return Double.parseDouble(nextToken());
    }

    public long nL() {
        return Long.parseLong(nextToken());
    }

    public String n() {
        return nextToken();
    }

    private BufferedReader r;
    private String line;
    private StringTokenizer st;
    private String token;

    private String peekToken() {
        if (token == null) 
            try {
                while (st == null || !st.hasMoreTokens()) {
                    line = r.readLine();
                    if (line == null) return null;
                    st = new StringTokenizer(line);
                }
                token = st.nextToken();
            } catch (IOException e) { }
        return token;
    }

    private String nextToken() {
        String ans = peekToken();
        token = null;
        return ans;
    }
}