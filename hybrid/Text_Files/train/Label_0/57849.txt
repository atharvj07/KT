import java.util.*;
import java.io.*;

class Main {
    static class State implements Comparable<State> {
        int d;
        String r;
        State(int d, String r) {
            this.d = d;
            this.r = r;
        }
        public boolean equals(Object s) {
            if(s instanceof State) {
                return compareTo((State)s) == 0;
            }
            return false;
        }
        public int hashCode() {
            return 1023 * d + r.hashCode();
        }
        public int compareTo(State s) {
            int dd = d - s.d;
            return dd < 0 ? -1 : (dd > 0 ? 1 : r.compareTo(s.r));
        }
    }
    public static void main(String [] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int n = Integer.parseInt(br.readLine());
        String [] cs = new String[n];
        HashSet<String> edges2 = new HashSet<String>();
        for(int i = 0; i < n; i++) {
            cs[i] = br.readLine();
            edges2.add(cs[i]);
        }
        HashMap<String,ArrayList<String>> edges = new HashMap<String,ArrayList<String>>();
        for(String c : cs) {
            final int l = c.length();
            for(int i = 0; i < l; i++) {
                String pre = c.substring(0, l - i);
                String suf = c.substring(l - i);
                if(edges.get(pre) == null) {
                    edges.put(pre, new ArrayList<String>());
                }
                edges.get(pre).add(suf);
            }
        }
        PriorityQueue<State> que = new PriorityQueue<State>();
        for(String c : cs) {
            for(String d : cs) {
                if(c.equals(d)) continue;
                if(c.startsWith(d)) {
                    int rr = d.length();
                    que.add(new State(rr, c.substring(rr)));
                }
            }
        }
        HashSet<String> done = new HashSet<String>();
        while(que.size() > 0) {
            State s = que.poll();
            //System.out.println("pop " + s.r + " at " + s.d);
            if(s.r.length() == 0) {
                System.out.println(s.d);
                return;
            }
            if(done.contains(s.r)) continue;
            done.add(s.r);
            final int srl = s.r.length();
            for(int i = 1; i < srl; i++) {
                String sri = s.r.substring(0,i);
                if(edges2.contains(sri) && !done.contains(sri)) {
                    que.add(new State(s.d + i, s.r.substring(i)));
                }
            }
            ArrayList<String> es = edges.get(s.r);
            if(es == null) continue;
            for(String q : es) {
                if(done.contains(q)) continue;
                que.add(new State(s.d + srl, q));
            }
        }
        System.out.println(0);
    }
}

