import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class OracAndGameOfLife {
    private static final int[][] coordinates = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    private final long[][] distance;
    private final boolean[][] visited;

    public OracAndGameOfLife(int row, int column) {
        distance = new long[row][column];
        visited = new boolean[row][column];
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int row = in.nextInt();
        int column = in.nextInt();
        int query = in.nextInt();

        OracAndGameOfLife oracAndGameOfLife = new OracAndGameOfLife(row, column);
        int[][] board = new int[row][column];
        for (int i = 0; i < row; i++) {
            String temp = in.next();
            for (int j = 0; j < column; j++) {
                board[i][j] = temp.charAt(j) - '0';
            }
        }
        oracAndGameOfLife.bfs(board, row, column);
        for (int q = 0; q < query; q++) {
            int i = in.nextInt() - 1;
            int j = in.nextInt() - 1;
            long p = in.nextLong();

            if (oracAndGameOfLife.visited[i][j]) {
                System.out.println(board[i][j] ^ (Math.max(0, p - oracAndGameOfLife.distance[i][j]) & 1));
            } else {
                System.out.println(board[i][j]);
            }
        }
    }

    private boolean canChangeColor(int[][] board, int x, int y) {
        for (int[] coordinate : coordinates) {
            if (withinBoard(board.length, board[0].length, x + coordinate[0], y + coordinate[1])
                    && board[x + coordinate[0]][y + coordinate[1]] == board[x][y]) {
                return true;
            }
        }
        return false;
    }

    private void bfs(int[][] board, int row, int column) {
        Deque<Pair> queue = new LinkedList<>();
        for (int x = 0; x < row; x++) {
            for (int y = 0; y < column; y++) {
                if (canChangeColor(board, x, y)) {
                    visited[x][y] = true;
                    queue.addLast(new Pair(x, y));
                }
            }
        }

        while (!queue.isEmpty()) {
            Pair current = queue.pollFirst();

            for (int[] coordinate : coordinates) {
                int newX = current.x + coordinate[0];
                int newY = current.y + coordinate[1];

                if (withinBoard(row, column, newX, newY) && !visited[newX][newY]) {
                    distance[newX][newY] = distance[current.x][current.y] + 1L;
                    visited[newX][newY] = true;
                    queue.addLast(new Pair(newX, newY));
                }
            }
        }
    }

    private boolean withinBoard(int row, int column, int newX, int newY) {
        return newX >= 0 && newX < row && newY >= 0 && newY < column;
    }

    private static class Pair {
        public final int x;
        public final int y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
