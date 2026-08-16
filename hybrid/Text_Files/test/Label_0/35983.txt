import java.io.*;
import java.util.Arrays;
import java.util.Random;
import java.util.StringTokenizer;

public class Main {
    FastScanner in;
    PrintWriter out;

    public void solve() throws IOException {

        int result = 0;
        int n = in.nextInt();
        int k = in.nextInt();
        int[] array = new int[n];
        Random rng = new Random();
        int count = 0;
        for (int i=0; i<n; i++){
            count += (in.nextInt() - in.nextInt()) * (-1) + 1;
        }
        result = (k - count%k)%k;
//        for (int i=0; i<n; i++){
//            int j = rng.nextInt(i + 1);
//            long tmp = array[j];
//            array[j] = array[i];
//            array[i] = tmp;
//        }
//        Arrays.sort(array);

        out.print(result);

//        out.flush();
    }

    private boolean check(int turns, int x, int y, int x0, int y0) {
        if (x0==x && y0==y){
            out.println(turns);
            return true;
        }
        return false;
    }

    public void run() {
        try {
//            in = new FastScanner(new File("Proba2.in"));
            in = new FastScanner();
//            out = new PrintWriter(new File(".out"));
            out = new PrintWriter(System.out);

            solve();

            out.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        FastScanner(File f) {
            try {
                br = new BufferedReader(new FileReader(f));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
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
    }

    public static void main(String[] arg) {
        new Main().run();
    }
}