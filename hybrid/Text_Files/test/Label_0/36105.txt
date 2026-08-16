import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter printWriter = new PrintWriter(System.out);
        Solve TaskSolve = new Solve();
        TaskSolve.main(bufferedReader, printWriter);
        bufferedReader.close();
        printWriter.close();
    }

	static class Solve {

        public void main(BufferedReader bufferedReader, PrintWriter printWriter) throws IOException {

            StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

            int n = Integer.parseInt(stringTokenizer.nextToken());
            int m = Integer.parseInt(stringTokenizer.nextToken());
            int k = Integer.parseInt(stringTokenizer.nextToken());

            int table[][] = new int[n][m];
            int query[][] = new int[k][3];

            for(int i = 0; i < k; i++) {
                stringTokenizer = new StringTokenizer(bufferedReader.readLine());
                query[i][0] = Integer.parseInt(stringTokenizer.nextToken());
                query[i][1] = Integer.parseInt(stringTokenizer.nextToken()) - 1;
                query[i][2] = Integer.parseInt(stringTokenizer.nextToken());
            }

            int string[] = new int[n];
            int column[] = new int[m];

            for(int i = k - 1; i >= 0; i--) {
                if(query[i][0] == 1) {
                    if (string[query[i][1]] == 0) {
                        string[query[i][1]] = 1;
                        for(int j = 0; j < m; j++) {
                            if(table[query[i][1]][j] == 0) {
                                table[query[i][1]][j] = query[i][2];
                            }
                        }
                    }
                }
                else {
                    if (column[query[i][1]] == 0) {
                        column[query[i][1]] = 1;
                        for(int j = 0; j < n; j++) {
                            if(table[j][query[i][1]] == 0) {
                                table[j][query[i][1]] = query[i][2];
                            }
                        }
                    }
                }
            }

            for(int i = 0; i < n; i++) {
                for(int j = 0; j < m; j++) {
                    if(j > 0) {
                        printWriter.print(" ");
                    }
                    printWriter.print(table[i][j]);
                }
                printWriter.print("\n");
            }

            bufferedReader.close();
            printWriter.close();
        }
    }
}