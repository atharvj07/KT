import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.io.UncheckedIOException;
import java.util.List;
import java.nio.charset.Charset;
import java.util.StringTokenizer;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author mikit
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        LightScanner in = new LightScanner(inputStream);
        LightWriter out = new LightWriter(outputStream);
        ETourism solver = new ETourism();
        solver.solve(1, in, out);
        out.close();
    }

    static class ETourism {
        public void solve(int testNumber, LightScanner in, LightWriter out) {
            WithMoreStack.run(() -> {
                int n = in.ints(), m = in.ints();
                ETourism.City[] cities = new ETourism.City[n];
                for (int i = 0; i < n; i++) {
                    cities[i] = new ETourism.City(i, in.longs());
                }
                for (int i = 0; i < m; i++) {
                    int x = in.ints() - 1, y = in.ints() - 1;
                    cities[x].neighbor.add(cities[y]);
                    cities[y].neighbor.add(cities[x]);
                }
                int s = 0;
                cities[s].dfs(null);
                long base = 0;
                for (int i = 0; i < n; i++) {
                    cities[i].visited = false;
                    if (cities[i].cyclic) base += cities[i].value;
                }
                out.ans(base + cities[s].solve(null)).ln();
            });
        }

        private static class City {
            int index;
            long value;
            List<ETourism.City> neighbor = new ArrayList<>();
            boolean visited;
            boolean cyclic;

            City(int index, long value) {
                this.index = index;
                this.value = value;
            }

            boolean dfs(ETourism.City from) {
                visited = true;
                for (ETourism.City city : neighbor) {
                    if (city == from) continue;
                    if (city.visited || city.dfs(this)) cyclic = true;
                }
                return cyclic;
            }

            long solve(ETourism.City from) {
                long max = 0;
                visited = true;
                for (ETourism.City city : neighbor) {
                    if (city == from || city.visited) continue;
                    max = Math.max(max, city.solve(this));
                }
                if (!cyclic) max += value;
                return max;
            }

        }

    }

    static class LightWriter implements AutoCloseable {
        private final Writer out;
        private boolean autoflush = false;
        private boolean breaked = true;

        public LightWriter(Writer out) {
            this.out = out;
        }

        public LightWriter(OutputStream out) {
            this(new BufferedWriter(new OutputStreamWriter(out, Charset.defaultCharset())));
        }

        public LightWriter print(char c) {
            try {
                out.write(c);
                breaked = false;
            } catch (IOException ex) {
                throw new UncheckedIOException(ex);
            }
            return this;
        }

        public LightWriter print(String s) {
            try {
                out.write(s, 0, s.length());
                breaked = false;
            } catch (IOException ex) {
                throw new UncheckedIOException(ex);
            }
            return this;
        }

        public LightWriter ans(String s) {
            if (!breaked) {
                print(' ');
            }
            return print(s);
        }

        public LightWriter ans(long l) {
            return ans(Long.toString(l));
        }

        public LightWriter ln() {
            print(System.lineSeparator());
            breaked = true;
            if (autoflush) {
                try {
                    out.flush();
                } catch (IOException ex) {
                    throw new UncheckedIOException(ex);
                }
            }
            return this;
        }

        public void close() {
            try {
                out.close();
            } catch (IOException ex) {
                throw new UncheckedIOException(ex);
            }
        }

    }

    static class LightScanner {
        private BufferedReader reader = null;
        private StringTokenizer tokenizer = null;

        public LightScanner(InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
        }

        public String string() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new UncheckedIOException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int ints() {
            return Integer.parseInt(string());
        }

        public long longs() {
            return Long.parseLong(string());
        }

    }

    static class WithMoreStack {
        private static final long STACK_SIZE = 64L * 1000 * 1000;

        private WithMoreStack() {
        }

        public static void run(Runnable task) {
            try {
                Thread thread = new Thread(null, task, "run", STACK_SIZE);
                thread.start();
                thread.join();
            } catch (InterruptedException ignored) {
            }
        }

    }
}


