import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.ArrayList;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        AOJ2701 solver = new AOJ2701();
        solver.solve(1, in, out);
        out.close();
    }

    static class AOJ2701 {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            while (true) {
                int h = in.nextInt(), n = in.nextInt();
                int l = h + 30;
                if (h == 0 && n == 0) {
                    return;
                }
                AOJ2701.Plain[] board = new AOJ2701.Plain[l];
                for (int i = 0; i < l; i++) {
                    board[i] = new AOJ2701.Plain();
                }
                Arrays.fill(board[0].state[0], true);
                Arrays.fill(board[0].state[1], true);
                Arrays.fill(board[1].state[0], true);
                Arrays.fill(board[1].state[1], true);
                for (int i = 0; i < h; i++) {
                    board[i + 2].parse(in);
                }

            /*{
                System.out.println("INITIAL BORAD " + board[0].cnt());
                int idx = 0;
                while (board[idx].cnt() > 0) {
                    board[idx].print();
                    idx++;
                }
            }*/

                AOJ2701.Cube[] cubes = new AOJ2701.Cube[n];
                int[] cnt = new int[n];
                int m = 1;
                for (int i = 0; i < n; i++) {
                    cubes[i] = new AOJ2701.Cube();
                    cubes[i].parse(in);
                    cnt[i] = cubes[i].getCandidates().size();
                    m *= cnt[i];
                }

                int ans = 0;
                for (int i = 0; i < m; i++) {
                    //System.out.println("START m="+i);

                    int res = 0;

                    AOJ2701.Plain[] b = new AOJ2701.Plain[l];
                    for (int j = 0; j < l; j++) {
                        b[j] = board[j].myclone();
                    }

                    int t = i;
                    for (int j = 0; j < n; j++) {
                        int cand = t % cnt[j];
                        t /= cnt[j];

                        AOJ2701.Cube fall = cubes[j].getCandidates().get(cand);
                        int cur = l - 2;
                        while (!b[cur].collidesWith(fall, 0) && !b[cur + 1].collidesWith(fall, 1)) {
                            cur--;
                        }
                        cur++;

                        b[cur].merge(fall, 0);
                        b[cur + 1].merge(fall, 1);

                        if (cur + 1 >= 2 && b[cur + 1].cnt() == 4) {
                            res++;
                            for (int k = cur + 2; k < b.length; k++) {
                                b[k - 1] = b[k];
                            }
                            b[b.length - 1] = new AOJ2701.Plain();
                        }
                        if (cur >= 2 && b[cur].cnt() == 4) {
                            res++;
                            for (int k = cur + 1; k < b.length; k++) {
                                b[k - 1] = b[k];
                            }
                            b[b.length - 1] = new AOJ2701.Plain();
                        }
                    
                    /*
                    System.out.println("Board printing n="+j);
                    int idx = 0;
                    while (b[idx].cnt() > 0) {
                        b[idx].print();
                        idx++;
                    }*/
                    }
                    ans = Math.max(ans, res);
                }
                out.println(ans);
            }
        }

        private static class Plain {
            boolean[][] state = new boolean[2][2];

            void parse(Scanner in) {
                for (int j = 0; j < 2; j++) {
                    String s = in.next();
                    state[j][0] = s.charAt(0) == '#';
                    state[j][1] = s.charAt(1) == '#';
                }
            }

            boolean collidesWith(AOJ2701.Cube cube, int h) {
                for (int i = 0; i < 2; i++) {
                    for (int j = 0; j < 2; j++) {
                        if (state[i][j] && cube.state[h][i][j]) {
                            return true;
                        }
                    }
                }
                return false;
            }

            void merge(AOJ2701.Cube cube, int h) {
                for (int i = 0; i < 2; i++) {
                    for (int j = 0; j < 2; j++) {
                        if (cube.state[h][i][j]) {
                            state[i][j] = true;
                        }
                    }
                }
            }

            int cnt() {
                int c = 0;
                for (int i = 0; i < 2; i++) {
                    for (int j = 0; j < 2; j++) {
                        if (state[i][j]) {
                            c++;
                        }
                    }
                }
                return c;
            }

            AOJ2701.Plain myclone() {
                AOJ2701.Plain clone = new AOJ2701.Plain();
                clone.state = new boolean[2][2];
                for (int i = 0; i < 2; i++) {
                    System.arraycopy(state[i], 0, clone.state[i], 0, 2);
                }
                return clone;
            }

        }

        private static class Cube {
            boolean[][][] state = new boolean[2][2][2];
            List<AOJ2701.Cube> candidates;

            void parse(Scanner in) {
                for (int i = 0; i < 2; i++) {
                    for (int j = 0; j < 2; j++) {
                        String s = in.next();
                        state[i][j][0] = s.charAt(0) == '#';
                        state[i][j][1] = s.charAt(1) == '#';
                    }
                }
            }

            List<AOJ2701.Cube> getCandidates() {
                if (candidates != null) return candidates;
                List<AOJ2701.Cube> a = new ArrayList<>();
                for (int i = -1; i <= 1; i++) {
                    for (int j = -1; j <= 1; j++) {
                        try {
                            AOJ2701.Cube d = new AOJ2701.Cube();
                            for (int k = 0; k < 2; k++) {
                                for (int l = 0; l < 2; l++) {
                                    for (int m = 0; m < 2; m++) {
                                        if (state[k][l][m]) {
                                            d.state[k][l + i][m + j] = true;
                                        }
                                    }
                                }
                            }
                            a.add(d);
                        } catch (ArrayIndexOutOfBoundsException ex) {
                        }
                    }
                }
                return candidates = a;
            }

        }

    }
}


