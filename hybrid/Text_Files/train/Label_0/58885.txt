import java.util.Scanner;


public class C_RoadsInBerland {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        int n = s.nextInt();
        
        int[][] md = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                md[i][j] = s.nextInt();
        
        int k = s.nextInt();

        for (int t = 0; t < k; t++) {
            
                long sum = 0;
                int a=s.nextInt()-1, b=s.nextInt()-1, c=s.nextInt(); 
                
                for (int i = 0; i < n; i++) {
                    for (int j = i+1; j < n; j++) {

                        md[i][j] = md[j][i] = Math.min(md[i][j],
                                Math.min(md[i][a] + c + md[b][j], 
                                         md[i][b] + c + md[a][j])
                                );

                        sum += md[i][j];
                    }
                }
            
            System.out.print(String.format("%s ", sum));
        }
        
        
    }

}
