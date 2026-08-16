import java.io.BufferedReader;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class A43 {
    public static void main(String [] args) {
        InputStream inputReader = System.in;
        OutputStream outputReader = System.out;
        InputReader in = new InputReader(inputReader);
        PrintWriter out = new PrintWriter(outputReader);
        Algorithm solver = new Algorithm();
        solver.solve(in, out);
        out.close();
    }
}

class Algorithm {
    void solve(InputReader ir, PrintWriter pw) {
        int n = ir.nextInt();
        int v = ir.nextInt();
        TreeSet<Integer> index = new TreeSet<>();
        for (int i = 0; i < n; i++) {
            int k = ir.nextInt();
            for (int j = 0; j < k;j++) {
                if (v > ir.nextInt()) index.add(i + 1);
            }
        }
        pw.println(index.size());
        for (Integer i : index) pw.print(i + " ");
    }
}

class InputReader {
    private BufferedReader reader;
    private StringTokenizer tokenizer;

    InputReader(InputStream stream) {
        reader = new BufferedReader(new InputStreamReader(stream), 32768);
        tokenizer = null;
    }

    private String next() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                tokenizer = new StringTokenizer(reader.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken();
    }

    int nextInt() {
        return Integer.parseInt(next());
    }

}