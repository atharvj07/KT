import java.util.*;
import java.io.*;

public class task610B {
    FastScanner in;
    PrintWriter out;
    
    
    void solve(){
        int n = in.nextInt();
        int min=2000000001;
        int[] a = new int[n];
        for (int i=0; i<n; i++) {
            a[i]=in.nextInt();
            min = Math.min(min, a[i]);
        }
        ArrayList<Integer> m = new ArrayList<Integer>();
        for (int i=0; i<n; i++) {
            if (a[i]==min)
                m.add(i);
        }
        m.add(m.get(0)+n);
        int max=0;
        for (int i=0; i<m.size()-1; i++){
            if (m.get(i+1)-m.get(i)>max)
                max=m.get(i+1)-m.get(i);
        }
        long ans = (long)min*n+max-1;
        out.println(ans);

    }
    
    void run() {
        try {
            in = new FastScanner(new File("CF.in"));
            out = new PrintWriter(new File("CF.out"));

            solve();

            out.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    void runIO() {

        in = new FastScanner(System.in);
        out = new PrintWriter(System.out);

        solve();

        out.close();
    }
    
    class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner(File f) {
            try {
                br = new BufferedReader(new FileReader(f));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        public FastScanner(InputStream f) {
            br = new BufferedReader(new InputStreamReader(f));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                String s = null;
                try {
                    s = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (s == null)
                    return null;
                st = new StringTokenizer(s);
            }
            return st.nextToken();
        }

        boolean hasMoreTokens() {
            while (st == null || !st.hasMoreTokens()) {
                String s = null;
                try {
                    s = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (s == null)
                    return false;
                st = new StringTokenizer(s);
            }
            return true;
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
    }
    
    public static void main(String[] args) {
        new task610B().runIO();
    }

}
