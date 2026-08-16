import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        HashSet<String> hs = new HashSet<String>();
        for(int i = 0; i < n; i++) {
            hs.add(sc.next());
        }
        System.out.println(hs.size());
    }
}