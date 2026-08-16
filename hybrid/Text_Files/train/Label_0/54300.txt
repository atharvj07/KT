
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];   //a_max = 10^9
        int XORsum = 0;
        for(int i=0;i<n;i++){
            a[i] = sc.nextInt();
            XORsum ^= a[i];
        }
        for(int i=0;i<n;i++){
            if(i != 0){
                System.out.print(" ");
            }
            System.out.print(XORsum ^ a[i]);
        }
        System.out.println();
    }
}
