//package Implementations;
import java.io.*;

/**
 * @author Tran Anh Tai
 */
public class LatinSquare implements Runnable
{
    public static void main(String[] args){
        new LatinSquare().run();
    }

    @Override
    public void run(){
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
        try{
            int n = Integer.parseInt(in.readLine());
            int result[][] = LatinSquareConstruct(n);
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    out.print(result[i][j] + " ");
                }
                out.println();
            }
        }
        catch (IOException e){
            out.println("IO Exception!");
        }
        out.close();
    }

    private int[][] LatinSquareConstruct(int n) {
        int result[][] = new int[n][n];
        for (int i = 0; i < n - 1; i++){
            int cur = i;
            for (int j = 0; j < n - 1; j++){
                cur = cur % (n - 1);
                result[i][j] = cur++;
                if (result[i][j] == 0 && i > 0){
                    result[i][j] = n - 1;
                }
            }
        }
        result[0][n - 1] = result[n - 1][0] = n - 1;
        for (int i = 1; i < n - 1; i++){
            result[i][n - 1] = result[n - 1][i] = result[i][i];
            result[i][i] = 0;
        }
        return result;
    }
}
