/**
 * File              : B.java
 * Author            : Bao To Hoai
 * Date              : 02.11.2020 13:56:25 UTC+7
 * Last Modified Date: 02.11.2020 14:04:25 UTC+7
 * Last Modified By  : Bao To Hoai
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B {

    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        String s1 = fs.next();
        String s2 = fs.next();
        int[] cnt1 = new int[26];
        int[] cnt2 = new int[26];
        for (char c : s1.toCharArray()) {
            cnt1[c - 'a']++;
        }
        for (char c : s2.toCharArray()) {
            cnt2[c - 'a']++;
        }
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (cnt2[i] > 0 && cnt1[i] == 0) {
                System.out.println("-1");
                return;
            }
            if (cnt2[i] > 0 && cnt1[i] > 0) {
                ans += Math.min(cnt1[i], cnt2[i]);
            }
        }
        System.out.println(ans);
    }
    
    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        
        String next() {
            while (!st.hasMoreTokens())
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }
        
        int nextInt() {
            return Integer.parseInt(next());
        }
        
        int[] readArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = nextInt();
            return a;
        }
        
        long nextLong() {
            return Long.parseLong(next());
        }
    }
}


