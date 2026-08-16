import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) throws Exception {
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            String s = sc.next();
            HashMap<String, String> map = new HashMap<>();
            for (int j = 1; j < s.length(); j++) {
                String f = s.substring(0, j);
                String l = s.substring(j, s.length());
                map.put(f+l,"");
                map.put(f+r(l),"");
                map.put(r(f)+l,"");
                map.put(r(f)+r(l),"");
                map.put(l+f,"");
                map.put(l+r(f),"");
                map.put(r(l)+f,"");
                map.put(r(l)+r(f),"");
            }
            System.out.println(map.size());
        }
    }
    
    public static String r(String s) {
        return new StringBuffer(s).reverse().toString();
    }
}