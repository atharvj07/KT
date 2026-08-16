


import java.io.BufferedInputStream;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner input = new Scanner(new BufferedInputStream(System.in));
        int t = input.nextInt();
        int[] result = new int[t];
        int p = 0;
        for (int i = 0; i < t; i++) {
            int n = input.nextInt();
            int[] temp = new int[n];
            for (int j = 0; j < n; j++) {
                temp[j] = input.nextInt();
            }
            int count = 0;
            for (int j = 1; j < n; j++) {
                if (temp[0] == temp[j]){
                    count++;
                }
            }
            if (count>0){
                for (int j = 1; j < n; j++) {
                    if ((float)(temp[0]+temp[j])/2!=(float)temp[0]){
                        result[p++] = j;
                    }
                }
            }else {
                result[p++] = 0;
            }
        }
        for (int i = 0; i < p; i++) {
            System.out.print(result[i]+1);
            if (i<p-1){
                System.out.println();
            }
        }

    }
}


  		 	 	 			 	  								