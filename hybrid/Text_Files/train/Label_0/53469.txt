import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x=sc.nextInt()*2,y=sc.nextInt();
        int count=0;
        for(int i=2;i<x;i+=2) {
            if(y*i%x==0) {
                count++;
            }
        }
        System.out.println(x/2+y-count);
    }
}
