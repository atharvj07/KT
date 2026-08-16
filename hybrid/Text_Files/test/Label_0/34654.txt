import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = Long.parseLong(sc.next());
        long min = Long.parseLong(sc.next());
        long tmp;
        for(int i=0;i<4;i++){
            tmp = Long.parseLong(sc.next());
            if(tmp < min){
                min = tmp;
            }
        }
        sc.close();
        long count = (n+min-1)/min;
        System.out.println(4+count);
    }
    
}