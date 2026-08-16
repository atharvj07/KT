import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Sol2 {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char[][] board = new char[n][n];
        for(int i=0;i<n;i++) {
            String l = br.readLine();
            for(int j=0;j<l.length();j++)
                board[i][j] = l.charAt(j);
        }
        if(check(board, n) && checkBoundary(board, n))
            System.out.println("YES");
        else
            System.out.println("NO");
    }

    private static boolean check(char[][] board, int n) {
        boolean res = false;
        boolean dotFound = false;
        for(int i=1;i<n-1;i++) {
            for(int j=1;j<n-1;j++) {
                if(board[i][j] == '.') {
                    dotFound = true;
                    if(checkOtherLoc(board, i, j, n)) {
                        res = true;
                        board[i][j] = '#';
                        board[i+1][j] = '#';
                        board[i][j+1] = '#';
                        board[i-1][j] = '#';
                        board[i][j-1] = '#';
                        res = res & check(board, n);
                    }
                }
            }
        }
        if(!dotFound)
            return true;

        return res;
    }

    private static boolean checkOtherLoc(char [][] board, int i, int j, int n) {
        if(board[i-1][j] == '.' && board[i+1][j] == '.' && board[i][j-1] == '.' && board[i][j+1] == '.') {
           return true;
        }
        return false;
    }

    private static boolean checkBoundary(char[][] board, int n) {
        for(int i=0;i<n;i++) {
            if(board[0][i] == '.' || board[i][0] == '.' || board[n-1][i] == '.' || board[i][n-1] == '.')
                return false;
        }
        return  true;
    }
}