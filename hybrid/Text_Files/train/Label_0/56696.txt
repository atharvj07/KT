import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;


public class Bdevu {
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int x = sc.nextInt();
        List<Integer> nums = new LinkedList<Integer>();
        for (int i = 0; i < n; i++) {
            nums.add(sc.nextInt());
        }
        Collections.sort(nums);
        long result = 0;
        for (Integer val : nums) {
            result += (long) x * (long) val;
            if (x != 1)
                x--;
        }
        System.out.println(result);
    }

  
    }