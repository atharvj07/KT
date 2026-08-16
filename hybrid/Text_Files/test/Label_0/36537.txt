import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static Map<Integer, Integer> source = new HashMap<Integer, Integer>();
    static Map<Integer, Integer> destination = new HashMap<Integer, Integer>();

    public static void buildMap(Map<Integer, Integer> map, int[] array) {
        for (int i : array) {
            if (map.get(i) == null)
                map.put(i, 1);
            else
                map.put(i, map.get(i) + 1);
        }
    }

    public static boolean solution(){
        for (Integer integer : destination.keySet()) {
            if (source.get(integer) == null)
                return false;
            if (source.get(integer) < destination.get(integer))
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] array1 = new int[n];
        for (int i = 0; i < n; i++) {
            array1[i] = in.nextInt();
        }
        int m = in.nextInt();
        int[] array2 = new int[m];
        for (int i = 0; i < m; i++) {
            array2[i] = in.nextInt();
        }
        buildMap(source, array1);
        buildMap(destination, array2);
        System.out.println(solution()? "YES": "NO");
    }
}
