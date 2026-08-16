import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Collection;
import java.util.Scanner;
import java.util.Queue;
import java.util.ArrayDeque;

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
        private static final String YES = "Yes";
        private static final String NO = "No";

        public void solve(int testNumber, Scanner in, PrintWriter out) {
            outer:
            while (true) {
                int h = in.nextInt(), w = in.nextInt(), r = in.nextInt(), c = in.nextInt();
                if (h == 0 && w == 0 && r == 0 && c == 0) {
                    return;
                }
                AOJ2701.Cell[][] cell = new AOJ2701.Cell[h + 2][w + 2];
                for (int i = 0; i < h + 2; i++) {
                    for (int j = 0; j < w + 2; j++) {
                        cell[i][j] = new AOJ2701.Cell(i, j);
                    }
                }

                for (int i = 0; i < h + 2; i++) {
                    cell[i][0].goal = true;
                    cell[i][w + 1].goal = true;
                }
                for (int i = 0; i < w + 2; i++) {
                    cell[0][i].goal = true;
                    cell[h + 1][i].goal = true;
                }

                for (int i = 1; i <= w; i++) {
                    if (in.nextInt() == 1) {
                        cell[0][i].state[1] = true;
                        cell[1][i].state[3] = true;
                    }
                }
                for (int i = 1; i <= h; i++) {
                    for (int j = 0; j <= w; j++) {
                        if (in.nextInt() == 1) {
                            cell[i][j].state[0] = true;
                            cell[i][j + 1].state[2] = true;
                        }
                    }
                    for (int j = 1; j <= w; j++) {
                        if (in.nextInt() == 1) {
                            cell[i][j].state[1] = true;
                            cell[i + 1][j].state[3] = true;
                        }
                    }
                }

                {
                    AOJ2701.Cell start = cell[r][c];
                    for (int i = 0; i < 4; i++) {
                        int nx = start.x + AOJ2701.Cell.dx[i], ny = start.y + AOJ2701.Cell.dy[i];
                        if (cell[ny][nx].goal && !start.state[i]) {
                            out.println(YES);
                            continue outer;
                        }
                    }
                }

                Queue<AOJ2701.Cell> q = new ArrayDeque<>();
                for (int i = 1; i <= h; i++) {
                    q.offer(cell[i][1]);
                    q.offer(cell[i][w]);
                }
                for (int i = 1; i <= w; i++) {
                    q.offer(cell[1][i]);
                    q.offer(cell[h][i]);
                }

                while (!q.isEmpty()) {
                    AOJ2701.Cell cur = q.poll();
                    if (cur.goal) continue;

                    boolean[] accesibility = new boolean[2];
                    for (int i = 0; i < 4; i++) {
                        int nx = cur.x + AOJ2701.Cell.dx[i], ny = cur.y + AOJ2701.Cell.dy[i];
                        if (cell[ny][nx].goal) {
                            accesibility[cur.state[i] ? 0 : 1] = true;
                        }
                    }
                    if (!accesibility[0] || !accesibility[1]) {
                        continue;
                    }
                    cur.goal = true;
                    for (int i = 0; i < 4; i++) {
                        int nx = cur.x + AOJ2701.Cell.dx[i], ny = cur.y + AOJ2701.Cell.dy[i];
                        if (!cell[ny][nx].goal) {
                            q.offer(cell[ny][nx]);
                        }
                    }
                }

            /*
            System.out.println("===");
            for (int i = 0; i < h + 2; i++) {
                for (int j = 0; j < w + 2; j++) {
                    System.out.print(cell[i][j].goal ? '#' : '.');
                }
                System.out.println();
            }*/

                out.println(cell[r][c].goal ? YES : NO);
            }
        }

        private static class Cell {
            private static int[] dx = {1, 0, -1, 0};
            private static int[] dy = {0, 1, 0, -1};
            private boolean[] state = new boolean[4];
            private boolean goal;
            private final int x;
            private final int y;

            public Cell(int y, int x) {
                this.y = y;
                this.x = x;
            }

        }

    }
}


