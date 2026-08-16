import java.util.*;
public class Main
{
    public static void main(String [] args)
    {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt(); long constant = 0;
        TreeMap<Integer, Integer> map = new TreeMap<>(); int ptr = -1; int idx = -1; int total = 0;
        long val = 0;
        for (int i = 0; i < q; i++) {
            if (sc.nextInt() == 1) {
                int a = sc.nextInt(); int b = sc.nextInt();
                constant += b;
                map.put(a, map.getOrDefault(a, 0) + 1);
                if (ptr == -1) {
                    ptr = a; idx = 1;
                } else if (a < ptr) {
                    val += Math.abs(a - ptr);
                    if (total % 2 == 1) {
                        idx--;
                        if (idx == 0) {
                            ptr = map.lowerKey(ptr);
                            idx = map.get(ptr);
                        }
                    }
                } else if (a > ptr) {
                    val += Math.abs(a - ptr);
                    if (total % 2 == 0) {
                        idx++;
                        if (idx > map.get(ptr)) {
                            int newPtr = map.higherKey(ptr);
                            val -= (newPtr - ptr);
                            ptr = newPtr;
                            idx = 1;
                        }
                    }
                } else {
                    if (total % 2 == 0) {
                        idx++;
                    }
                    val += Math.abs(ptr - a);
                }
                total++;
            } else {
                System.out.println(ptr + " " + (val + constant));
            }
        }
    }


}