import java.util.Arrays;
import java.util.Scanner;

public class Test {




    public static void main(String args[] ) throws Exception {

        Scanner s = new Scanner(System.in);

        int  n = s.nextInt();

        long a[][] = new long[n][n];


        int c = 0;
        for(int i=0;i<n/2;i++){
            for(int j=0;j<n/2;j++){

                a[i][j] = 4*c;
                a[i][j+n/2] = 4*c + 1;
                a[i+n/2][j] = 4*c + 2;
                a[i+n/2][j+n/2] = 4*c + 3;


                c++;
            }

        }

        StringBuilder sb = new StringBuilder();
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                sb.append(a[i][j]+" ");
            }
            sb.append("\n");
        }
       System.out.println(sb);

    }

}
