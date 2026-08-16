import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.StreamTokenizer;
import java.util.Arrays;


public class C {

    static StreamTokenizer st;
    public static void main(String[] args) throws IOException{
        st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n = nextInt();
        byte[][]a = new byte[n+1][n+1];
        int k = nextInt();
        for (int i = 1; i <= k; i++) {
            int v1 = nextInt();
            int v2 = nextInt();
            a[v1][v2] = a[v2][v1] = 1;
        }
        int m = nextInt();
        for (int i = 1; i <= m; i++) {
            int v1 = nextInt();
            int v2 = nextInt();
            a[v1][v2] = a[v2][v1] = -1;
        }
        boolean[]used = new boolean[n+1];
        boolean[]current = new boolean[n+1];
        int[]q = new int[n+1];
        int max = 0;
        for (int i = 1; i <= n; i++) {
            Arrays.fill(current, false);
            if (!used[i]) {
                int head = 0, tail = 1;
                used[i] = true;
                q[1] = i;
                boolean f = true;
                current[i] = true;
                while (head < tail) {
                    int v = q[++head];
                    for (int j = 1; j <= n; j++) {
                        if (a[v][j]==1) {
                            if (!used[j]) {
                                used[j] = true;
                                current[j] = true;
                                q[++tail] = j;
                            }
                        }
                        else if (a[v][j]==-1) {
                            if (current[j]) {
                                f = false;
                            }
                        }
                    }
                }
                if (f)
                    max = Math.max(max, tail);
            }
        }
        pw.print(max);
        pw.close();
    }
     
    private static int nextInt() throws IOException{
        st.nextToken();
        return (int) st.nval;
    }

}
