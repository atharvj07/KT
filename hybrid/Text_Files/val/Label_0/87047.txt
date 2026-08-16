import java.io.*;
import java.util.*;

public class Solution {

    BufferedReader br;
    PrintWriter out;
    StringTokenizer st;
    boolean eof;

    static final int P = 1000000007;

    void solve() throws IOException {
        int n=nextInt();
        int m=nextInt();
        int w=nextInt();
        long a[]=new long[n];
        for(int i=0;i<n;i++) a[i]=nextInt();
        long low=0,high=2010000000,mid=0;
        while(high-low>0) {
            mid=(low+high+1)/2;
            long cur=0,cnt=0;
            long s[]=new long[n];
            for(int i=0;i<n;i++) {
                cur-=s[i];
                long x=mid-a[i]-cur;
                if(x>0) {
                    cur+=x;
                    cnt+=x;
                    if(i+w<n) s[i+w]+=x;
                }
            }
            if(cnt<=m) low=mid;
            else high=mid-1;
        }
        out.println(low);
    }

    Solution() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        solve();
        out.close();
    }

    public static void main(String[] args) throws IOException {
        new Solution();
    }

    String nextToken() {
        while (st == null || !st.hasMoreTokens()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (Exception e) {
                eof = true;
                return null;
            }
        }
        return st.nextToken();
    }

    String nextString() {
        try {
            return br.readLine();
        } catch (IOException e) {
            eof = true;
            return null;
        }
    }

    int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }
}