import java.util.Scanner;
public class main {
    public static void main(String args[]) throws Exception {
        Scanner in = new Scanner(System.in);
        int x = in.nextInt();
        int i=0;
        int sum=0;
        int max=0;
        for (i=0;i<x;i++){
            int g = in.nextInt();
             sum=sum+g;
            max = Math.max(g,max);


        }
        System.out.println(2*max-sum+1);

    }
}