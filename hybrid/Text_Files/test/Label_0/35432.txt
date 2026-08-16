import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        
        while (true) {
            String line = in.nextLine();
            if (line.equals("END OF INPUT")) break;
            
            String ans = "";
            
            String[] splat = line.split(" ");
            for (String str : splat) {
                int n = str.length();
                if (n < 10) ans += "" + n;
            }
            
            System.out.println(ans);
        }
    }
}

