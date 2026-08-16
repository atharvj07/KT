import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int test  = sc.nextInt();
        int[] arr = new int[test];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        for (int i = 0; i < arr.length; i++){
            System.out.println(student(arr[i]));
        }

    }

   
    static String student(int n){
        int b = n/7;
        int a = 0;
        while(a*3 + b*7 != n){
            if(b < 0) return"NO";
            if(a*3 + b*7 > n) b--;
            else a++;
        }
        return ("YES");

    }
}
