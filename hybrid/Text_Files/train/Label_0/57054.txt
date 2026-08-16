import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a;
        a = scan.nextInt(); 
        if(a <= 999)
            System.out.println("ABC");
        else
            System.out.println("ABD");
    }
}
