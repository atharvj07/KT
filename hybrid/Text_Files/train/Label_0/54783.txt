import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        boolean hasY = false;
        for (int i = 0; i < n; i++) {
            char ch = sc.next().charAt(0);
            if (ch == 'Y') {
                hasY = true;
                break;
            }
        }
        
        System.out.println(hasY ? "Four" : "Three");
    }
}