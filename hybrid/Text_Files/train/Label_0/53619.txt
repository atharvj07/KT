import java.util.ArrayList;
import java.util.Scanner;
import java.lang.StringBuilder;
import java.util.Arrays;
import java.util.Stack;
import java.util.TreeMap;
public class Test10   {  
    //suppose: a[0] black
    //maintain: array a[i][j]: number of coloring w/ pointer on i with j black vertices to right:
    //if a[i] black: a[i][j] = a[i - 1][j + 1];
    //if a[i] white:a[i][j] = total possible / 4(2 if j = 0) + 2 ^ (i + j - 1) * a[i - 1][j];
    //total possible = 2 ^ (undecided + (i + j + 1) * (i + j) / 2)
    //if a[i] ambiguous: a[i][j] = sum of two
    //maintain on i
    public static void main(String[] Args)   {
        long huge = 1000000007;
        long[][] a = new long[51][51];
        long ans = 0;
        long[] pw2 = new long[5001];
        pw2[0] = 1;
        for (int i = 0; i <= 4999; i++)
            pw2[i + 1] = (pw2[i] * 2)%huge;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
                int p = sc.nextInt();
        int[] cl = new int[n];
        for (int i = 0; i < n; i++) cl[i] = sc.nextInt();

        if (cl[0] == -1 || cl[0] == 0)   {
            for (int i = 0; i <= 50; i++)  {
                if (i % 2 != p) a[0][i] = pw2[(i *(i + 1))/2];
                else a[0][i] = 0;
            }    
            int undecided = 0;
            for (int i = 1; i <= n - 1; i++)  {
                for (int j = 0; j <= n - 1 - i; j++)   {
                    a[i][j] = 0;
                    if (cl[i] == 0 || cl[i] == -1)   {
                        a[i][j] += a[i - 1][j + 1];
                    }   
                    if (cl[i] == 1 || cl[i] == -1)   {
                        if (j == 0) a[i][j] += pw2[undecided + ((i + j + 1) * (i + j)) / 2 - 1];
                        else { 
                            a[i][j] += pw2[undecided + ((i + j + 1) * (i + j)) / 2 - 2];
                            a[i][j] += pw2[i + j - 1] * a[i - 1][j];
                        }
                    }    
                    a[i][j] = a[i][j] % huge;
                }    
                if (cl[i] == -1) undecided++;
            }
            ans += a[n - 1][0];
        }    
        a = new long[51][51];
        if (cl[0] == -1 || cl[0] == 1)   {
            for (int i = 0; i <= 50; i++)  {
                if (i % 2 != p) a[0][i] = pw2[(i *(i + 1))/2];
                else a[0][i] = 0;
            }    
            int undecided = 0;
            for (int i = 1; i <= n - 1; i++)  {
                for (int j = 0; j <= n - 1 - i; j++)   {
                    a[i][j] = 0;
                    if (cl[i] == 1 || cl[i] == -1)   {
                        a[i][j] += a[i - 1][j + 1];
                    }   
                    if (cl[i] == 0 || cl[i] == -1)   {
                        if (j == 0)  {
                            a[i][j] += pw2[undecided + ((i + j + 1) * (i + j)) / 2 - 1];
                        }    
                        else  { 
                            a[i][j] += pw2[undecided + ((i + j + 1) * (i + j)) / 2 - 2];
                            a[i][j] += pw2[i + j - 1] * a[i - 1][j];
                        }
                    }    
                    a[i][j] = a[i][j] % huge;
                }    
                if (cl[i] == -1) undecided++;
            }
            ans += a[n - 1][0];
        }    
        System.out.println(ans % huge);
   }
}