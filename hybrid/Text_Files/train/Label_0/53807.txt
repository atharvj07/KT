import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        
        int N = Integer.parseInt(line);
        Map<String, Integer> map = new HashMap<>();
        long count = 0;
        for (int i = 0; i < N; i++) {
            String input = sc.nextLine();
            char[] chars = input.toCharArray();
            Arrays.sort(chars);
            String sorted = String.valueOf(chars);
            if (map.containsKey(sorted)) {
                count += map.get(sorted);
                map.put(sorted, map.get(sorted) + 1);
            } else {
                map.put(sorted, 1);
            }
        }
        System.out.println(count);
    }
}