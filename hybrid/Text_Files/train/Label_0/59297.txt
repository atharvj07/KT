//package hashing;

import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class ORinMatrix {

    public static int orOperation(int [][] A, int row, int col)
    {
        for(int i=0; i<A[0].length; i++)
        {
            if(A[row][i] == 1)
            {
                return 1;
            }
        }
        for (int[] ints : A) {
            if (ints[col] == 1) {
                return 1;
            }
        }
         return 0;
    }

    public static void change(int [][] A, int row, int col)
    {
       for(int i=0; i<A[0].length; i++)
       {
           A[row][i] = 0;
       }
       for(int i=0; i<A.length; i++)
       {
           A[i][col] = 0;
       }
    }

    public static void print(int [][] A)
    {
        for (int[] ints : A) {
            for (int j = 0; j < A[0].length; j++) {
                System.out.print(ints[j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String [] args)throws java.io.IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = Arrays.stream(br.readLine().split("\\s+")).mapToInt(Integer::valueOf).toArray();
        int m = arr[0];
        int n = arr[1];
////        System.out.println(m + " " + n);
        int [][] B = new int[m][n];
        for(int i=0; i<m; i++)
        {
            int[] input = Arrays.stream(br.readLine().split("\\s+")).mapToInt(Integer::valueOf).toArray();
            B[i] = input;
        }

        int [][] A = new int[m][n];
        for(int i=0; i<m; i++)
        {
            Arrays.fill(A[i], 1);
        }

        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                if(B[i][j] == 0)
                {
                    change(A, i, j);
                }
            }
        }

        boolean yes = true;
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                if(B[i][j] != orOperation(A, i, j))
                {
                    yes = false;
                    break;
                }
            }
        }
        if(yes)
        {
            System.out.println("YES");
            print(A);
        }
        else
        {
            System.out.println("NO");
        }
    }
}
