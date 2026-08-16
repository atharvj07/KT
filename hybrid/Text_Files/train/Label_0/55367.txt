import java.io.*;
import java.util.*;

public class Solution {

    StreamTokenizer in;
    PrintWriter out;

    public static void main(String[] args) throws Exception {
        new Solution().run();
    }

    int nextInt() throws Exception {
        in.nextToken();
        return (int) in.nval;
    }

    public void run() throws Exception {
        in = new StreamTokenizer (new BufferedReader(new InputStreamReader(System.in)));
        out = new PrintWriter(new OutputStreamWriter(System.out));
        int n = nextInt();
        int m = nextInt();
        int k = nextInt();
        if (n==1 && Math.pow(2,m)>=k)
        {
        out.println("Missing");
        out.flush();
        return;
        }
        int B[] = new int[100];
                B[1] = k-1;
                int p = (int)Math.sqrt(k);
                if (p*p == k)
                        p--;
                B[2] = p;
                for (int i=3; i<=30; i++)
                        for (int j=p; j>=2; j--)
                                if (Math.pow(j, i) < k){
                                        B[i] = j;
                                        p = j;
                                        break;
                                }

                int x = 1000000000,
                        y = 1000000000;
                for (int i=m; i<=30; i++)
                        if (B[i]!=B[i+1] && B[i]>=n){
                                if (i-m == B[i]-n){
                                        out.println("Stas");
                                        out.flush();
                                        return;
                                }
                                else{
                                        if (i-m > B[i]-n)
                                                x = Math.min(x, i-m-(B[i]-n));
                                        else
                                                y = Math.min(y, B[i]-n-(i-m));
                                }
                        }

                if (x%2==0 && y%2==0){
                        out.println("Stas");
                        out.flush();
                        return;
                }
                else if (x%2==1 && y%2==1){
                        out.println("Masha");
                        out.flush();
                        return;
                }

                int u = n, v = m;
                while (Math.pow(u, v) < k){
                        u++;
                        v++;
                }

                u--;
                v--;
                if (x%2==1 && Math.pow(u, v+1)<k || y%2==1 && Math.pow(u+1, v)<k){
                        out.println("Masha");
                        out.flush();
                        return;
                }
                else{
                        out.println("Stas");
                        out.flush();
                        return;
                    }

                }
}