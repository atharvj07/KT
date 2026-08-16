import java.util.*;
import java.io.*;
import java.lang.*;
import java.math.*;
public class B {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
        // int n = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());
        // int[] a = new int[n]; for(int i=0; i<n; i++) a[i] = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder();
        for(int i=1; i<=n-1; i++) {
          double val = Math.sqrt(i*1.0/(n))*h;
          sb.append(val + " ");

        }
        out.println(sb.toString());
        out.close(); System.exit(0);
    }
}
