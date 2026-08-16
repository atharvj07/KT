
import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);
        int n;
        n = sc.nextInt();
        out.println(n);
        for(int i = 0;i < n;i++)
            out.print("1 ");
        out.flush();
        out.close();
    }
}
