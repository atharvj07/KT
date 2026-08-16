import java.util.HashMap;
import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        HashMap<Integer, Integer> setH = new HashMap<Integer, Integer>();
        HashMap<Integer, Integer> setA = new HashMap<Integer, Integer>();
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        for (int i = 0; i < n; i++) {
            int h = s.nextInt();
            int a = s.nextInt();
            if (!setH.containsKey(h)) {
                setH.put(h, 1);
            } else {
                setH.put(h, setH.get(h) + 1);
            }
            if (!setA.containsKey(a)) {
                setA.put(a, 1);
            } else {
                setA.put(a, setA.get(a) + 1);
            }
        }
        int ans = 0;
        for (Integer i : setH.keySet()) {
            if (setA.containsKey(i)) {
                ans += setH.get(i) * setA.get(i);
            }
        }
        System.out.println(ans);
    }
}
