import java.util.*;
import java.io.*;

    class Main{
        static final int n = 8;
        static boolean[] row = new boolean[n];
        static boolean[] col = new boolean[n];
        static boolean[] dpos = new boolean[2*n -1];
        static boolean[] dneg = new boolean[2*n -1];
        static boolean[][] X = new boolean[n][n];
        static void print_Board(){
          int i,j;
            for(i=0;i<n;i++){
                for(j=0;j<n;j++){
                    if(X[i][j]){
                        if(j==n-1)
                            System.out.println("Q");
                        else
                            System.out.print("Q");
                    }
                    else{
                        if(j==n-1)
                            System.out.println(".");
                        else System.out.print(".");
                    }
                }
            }
        }
        static void putQueen(int i){
          int j;
            if(i==n){
                print_Board();
                return;
            }
            else{
                for(j=0;j<n;j++){
                    if(X[i][j])
                        putQueen(i+1);
                    else if(col[j] || dpos[i+j] || dneg[i-j+n-1]){
                        continue;
                    }
                    else{
                        row[i] = true;
                        col[j] = true;
                        dpos[i+j] = true;
                        dneg[i-j+n-1] = true;
                        X[i][j] = true;
                        putQueen(i+1);
                        row[i] = false;
                        col[j] = false;
                        dpos[i+j] = false;
                        dneg[i-j+n-1] = false;
                        X[i][j] = false;
                    }
                }
                return;
            }
        }
        public static void main(String[] args){
            Scanner scan = new Scanner(System.in);
            int k = scan.nextInt();
            int i,j;
            for(i=0;i<n;i++){
                row[i] = false;
                col[i] = false;
            }
            for(i=0;i<2*n-1;i++){
                dpos[i] = false;
                dneg[i] = false;
            }
            for(i=0;i<n;i++)
                for(j=0;j<n;j++)
                    X[i][j] = false;
            for(i=0;i<k;i++){
                int x = scan.nextInt();
                int y = scan.nextInt();
                X[x][y] = true;
                row[x] = true;
                col[y] = true;
                dpos[x+y] = true;
                dneg[x-y+n-1] = true;
            }
            putQueen(0);
        }
    }

