import java.io.*;
import java.util.*;

public class Main {
    public static void main(final String[] args) {
        final FastReader s=new FastReader();
        int h = s.nextInt();
        int w = s.nextInt();
        int m = s.nextInt();
        
        // Map<Integer, Integer> xc = new HashMap<Integer, Integer>();
        // Map<Integer, Integer> yc = new HashMap<Integer, Integer>();
        int[] xc = new int[h+1];
        int[] yc = new int[w+1];
        // Set<String> b = new HashSet<>();
        Set<Long> b = new HashSet<>();
        int mx = 0;
        int my = 0;
        // boolean[][] b = new boolean[h][w];
        // Map<Integer, Set<Integer>> b =  new HashMap<>();

        for(int i=0; i<m; i++) {
            int x = s.nextInt();
            int y = s.nextInt();
            // if(!xc.containsKey(x)) xc.put(x, 0);
            // if(!yc.containsKey(y)) yc.put(y, 0);
            // xc.put(x, xc.get(x)+1);
            xc[x]++;
            mx = Math.max(mx, xc[x]);
            // yc.put(y, yc.get(y)+1);
            yc[y]++;
            my = Math.max(my, yc[y]);
            b.add(gethash(x,y));
            // if(mx==xc.get(x) || my==yc.get(y))
            // b.add(getString(x, y));
            // b[x-1][y-1] = true;
            // if(mx==xc.get(x) || my==yc.get(y)) {
            //     if(!b.containsKey(x)) b.put(x, new HashSet<>());
            //     b.get(x).add(y);
            // }
        }

        List<Integer> vx = new ArrayList<>();
        List<Integer> vy = new ArrayList<>();
        for(int i=0;i<xc.length;i++) {
            if(xc[i]==mx)
                vx.add(i);
        }

        for(int i=0;i<yc.length;i++) {
            if(yc[i]==my)
                vy.add(i);
        }
     
        for(int x : vx) {
            for(int y : vy) {
                if(!b.contains(gethash(x,y))) {
                    System.out.println(mx+my);
                    return;
                }                
            }
        }
        System.out.println(mx+my-1);
    }

    private static long gethash(int x, int y) {
        return x*1_000_000l + y;
    }

    // private static String getString(int x, int y) {
    //     return Integer.toString(x) + "." + Integer.toString(y);
    // }

    static class FastReader
    {
        BufferedReader br;
        StringTokenizer st;
        public FastReader() { br = new BufferedReader(new InputStreamReader(System.in)); }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try { st = new StringTokenizer(br.readLine()); }
                catch (final IOException  e) { e.printStackTrace(); }
            }
            return st.nextToken();
        }
        int nextInt() { return Integer.parseInt(next()); }
        long nextLong() { return Long.parseLong(next()); }
        double nextDouble() { return Double.parseDouble(next()); }
        String nextLine() {
            String str = "";
            try { str = br.readLine(); }
            catch (final IOException e) { e.printStackTrace(); }
            return str;
        }
    }
}