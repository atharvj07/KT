import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;




public class Main{
    public static void main(String[] args) throws IOException, InterruptedException {

        Scanner sc = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        int t = sc.nextInt();

        for (int m = 0; m < t; m++) {
            int n = sc.nextInt();
            int zero = 0;
            int sum = 0;

            for (int i = 0; i < n; i++) {
                int cur = sc.nextInt();

                if (cur == 0) zero++;
                sum += cur;
            }
            int ans = zero;
            sum+= zero;
            if (sum == 0)  ans ++;
            out.println(ans);
        }

        out.flush();


    }


}

class Scanner{
    StringTokenizer st;
    BufferedReader br;
    public Scanner(InputStream s){
        br = new BufferedReader(new InputStreamReader(s));
    }
    public Scanner (String s) throws FileNotFoundException { br = new BufferedReader(new FileReader(s));}

    public String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine());
        return st.nextToken();
    }

    public int[] nextIntArray(int n) throws IOException {
        int[] temp = new int[n];

        for (int i = 0; i < n; i++) {
            temp[i] = nextInt();
        }

        return temp;
    }

    public int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    public long nextLong() throws IOException {
        return  Long.parseLong(next());
    }

    public String nextLine() throws IOException {
        return br.readLine();
    }

    public double nextDouble() throws IOException {
        return Double.parseDouble(next());
    }

    public boolean ready() throws IOException {
        return br.ready();
    }
}
