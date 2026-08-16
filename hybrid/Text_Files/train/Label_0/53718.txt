import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while (T-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            
            int[][] arr = new int[n][m];
            
            int[] row = new int[n];
            int[] col = new int[m];
            
            for (int i=0; i<n; i++) {
                for (int j=0; j<m; j++) {
                    int temp = sc.nextInt();
                    arr[i][j] = temp;
                    if (temp == 1) {
                        row[i] = 1;
                        col[j] = 1;
                    }
                }
            }

            int countRow = 0;
            for (int val : row) {
                if (val == 0) {
                    countRow += 1;
                }
            }
            

            int countCol = 0;
            for (int val : col) {
                if (val == 0) {
                    countCol += 1;
                }
            }

            System.out.println((Math.min(countRow, countCol) % 2 != 0) ? "Ashish" : "Vivek");
        }
	}
}
