import java.io.InputStreamReader;
import java.util.*;

/**
 * Created by Nika on 4/30/2015.
 */
public class Main {
    private static Scanner sc = new Scanner(new InputStreamReader(System.in));
    public static void main(String[] args) {
        Set<Character> set = new HashSet<>();
        int n = sc.nextInt();
        String q = sc.next();
        List<String> result = new ArrayList<>();
        for (int i=0; i<q.length(); i++) {
            Character c = new Character(q.charAt(i));
            if (!set.contains(c)) {
                if (result.size() == (n-1)){
                    result.add(q.substring(i));
                    set.add(c);
                    break;
                }

                int index = i+1;
                if (index>=q.length()) break;
                Character c1 = q.charAt(index);
                set.add(c);
                while (index+1<q.length() && set.contains(c1)) {
                    index++;
                    c1 = q.charAt(index);
                }
                result.add(q.substring(i, index));
                i = index-1;
            }
        }

        if (set.size() >= n) {
            System.out.println("YES");
            result.forEach(System.out::println);
        } else {
            System.out.println("NO");
        }
    }
}
