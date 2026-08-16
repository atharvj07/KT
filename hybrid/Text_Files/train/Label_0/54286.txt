import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(in, out);
        out.close();
    }
}



class TaskD {

    private static final int N = 200000;

    private int left[] = new int[N];
    private int right[] = new int[N];
    private int val[] = new int[N];

    private int sum[][] = new int[30][N];
    private int add[][] = new int[30][N];

    private int answer[] = new int[N];

    private int MAX_BIT = 30;

    public void solve(InputReader in, OutputWriter out) {
        int n = in.nextInt();
        int m = in.nextInt();

        for (int i = 0; i < m; i++) {
            left[i] = in.nextInt() - 1;
            right[i] = in.nextInt() - 1;
            val[i] = in.nextInt();

            for (int bit = 0; bit < MAX_BIT; bit++) {
                if(isBitSet(val[i], bit)) {
                    add[bit][left[i]]++;
                    add[bit][right[i]+1]--;
                }
            }
        }

        for (int bit = 0; bit < MAX_BIT; bit++) {
            int current = 0;
            for (int i = 0; i < n; i++) {
                current += add[bit][i];
                sum[bit][i+1] = sum[bit][i] + (current > 0 ? 1 : 0);
            }
        }


        for (int i = 0; i < m; i++) {
            for (int bit = 0; bit < MAX_BIT; bit++) {
                if(!isBitSet(val[i], bit) && ((sum[bit][right[i]+1] - sum[bit][left[i]]) == (right[i] + 1 - left[i]))) {
                    out.printLine("NO");
                    return;
                }
            }
        }

        out.printLine("YES");

        for (int bit = 0; bit < MAX_BIT; bit++) {
            for (int i = 0; i < n; i++) {
                if(sum[bit][i+1] != sum[bit][i]) {
                    answer[i] |= (1 << bit);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            out.print(answer[i] + " ");
        }


    }

    private boolean isBitSet(int val, int bit) {
        return ((val >> bit) & 1) !=0;
    }


}



class InputReader {
    public BufferedReader reader;
    public StringTokenizer tokenizer;

    public InputReader(InputStream stream) {
        reader = new BufferedReader(new InputStreamReader(stream), 32768);
        tokenizer = null;
    }

    public String next() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                tokenizer = new StringTokenizer(reader.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken();
    }

    public boolean hasNext() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                String line = reader.readLine();
                if (line == null) {
                    return false;
                }
                tokenizer = new StringTokenizer(line);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return true;
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }
    public long nextLong() {
        return Long.parseLong(next());
    }

}

class OutputWriter {
    private final PrintWriter writer;

    public OutputWriter(OutputStream outputStream) {
        writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
    }

    public OutputWriter(Writer writer) {
        this.writer = new PrintWriter(writer);
    }

    public void print(Object... objects) {
        for (int i = 0; i < objects.length; i++) {
            if (i != 0) {
                writer.print(' ');
            }
            writer.print(objects[i]);
        }
    }

    public void printLine(Object... objects) {
        print(objects);
        writer.println();
    }

    public void close() {
        writer.close();
    }

}