import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        FastScanner scanner = new FastScanner();
        PrintWriter out = new PrintWriter(System.out,false);
        char[] s = scanner.next().toCharArray();
        char[] t = scanner.next().toCharArray();
        int n = s.length;
        int m = t.length;
        int[][] next = new int[n][26];
        for(int i= 0; i < 26; i++) {
            next[n-1][i] = -1;
            if (i == s[n-1]-'a') next[n-1][i] = n-1;
        }
        for(int i = n-2; i >= 0; i--) {
            for(int j = 0; j < 26; j++) {
                next[i][j] = next[i+1][j];
                if (s[i]-'a' == j) next[i][j] = i;
            }
        }
        long ans = 0;
        int cur = 0;
        for(int i = 0; i < m; i++) {
            int c = t[i]-'a';
            if (next[0][c] == -1) {
                System.out.println(-1);
                return;
            }
            if (next[cur][c] != -1) {
                ans += next[cur][c] - cur + 1;
                cur = next[cur][c] + 1;
            }
            else {
                ans += n - cur;
                ans += next[0][c] + 1;
                cur = next[0][c] + 1;
            }
            if (cur == n) cur = 0;
        }
        out.println(ans);
        out.flush();
    }
    
    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;
        
        public FastScanner(Reader in) {
            br = new BufferedReader(in);
        }
        
        public FastScanner() {
            this(new InputStreamReader(System.in));
        }
        
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
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
        
        String readNextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
