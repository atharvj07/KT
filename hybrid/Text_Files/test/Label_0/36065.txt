import org.omg.PortableServer.POA;

import java.awt.*;
import java.io.*;
import java.util.*;

public class Abc {
    public static void main(String[] args) throws IOException {
        FastReader sc = new FastReader();
        int t=sc.nextInt();
        while (t-->0) {
            char[] p = sc.next().toCharArray();
            int freq[] = new int[26];
            for (int i = 0; i < p.length; i++) {
                freq[p[i] - 'a']++;
            }
            boolean fo=false;
            char h[] = sc.next().toCharArray();
            for (int i = 0; i <=h.length - p.length; i++) {
                int freq2[] = new int[26];
                for (int j = i; j < i + p.length; j++) {
                    freq2[h[j] - 'a']++;
                }
                if (check(freq, freq2)) {
                    fo=true;
                    System.out.println("YES");
                    break;
                }
            }
            if (!fo) {
                System.out.println("NO");
            }
        }
    }
    static boolean check(int freq[],int freq2[]){
        for (int i=0;i<26;i++){
            if (freq[i]!=freq2[i])return false;
        }
        return true;
    }
    static class FastReader {
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

        String nextLine() {
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