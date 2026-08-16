
import java.lang.Math;
import java.util.*;



public class R_499_d2_B {
	

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

    	String[] vals = scanner.nextLine().split(" ");

    	int n = Integer.parseInt(vals[0].trim());
    	int m = Integer.parseInt(vals[1].trim());

    	String[] types = scanner.nextLine().split(" ");

        if (m < n) {
            System.out.println(0);
            return;
        }

        if (m == n) {
            System.out.println(1);
            return;
        }        

        HashMap<String, Integer> hits = new HashMap<>();
        for (int i = 0; i < types.length; i++) {
            Integer v = hits.get(types[i]);
            hits.put(types[i], v == null ? 1 : v + 1);
        }




        Integer max = Collections.max(hits.values());

        boolean flag = false;
        while (max > 0 && ! flag) {
            int units = 0;

            for (Integer e : hits.values()) {
                units += (e / max);
            }

            if (units >= n) {
                flag = true;
            }

            max--;
        }

        System.out.println(flag ? max + 1 : 0);
        

        
	}
}