
import java.util.Scanner;


public class cf1 {
    
    static boolean winning(int[][] mat, int i, int j){
        int col = 0;
        int row = 0;
        
        for(int k = 0; k < mat.length; k++){
            row += mat[i][k];
            col += mat[k][j];
        }
        
        return col > row;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        
        int[][] mat = new int[n][n];
        
        for(int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                mat[i][j] = sc.nextInt();
        
        int res = 0;
        
        for(int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if(winning(mat, i, j)) res++;
        
        System.out.println(res);
                
        
    }
    
}
